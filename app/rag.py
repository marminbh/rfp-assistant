from __future__ import annotations

from collections.abc import AsyncIterator

from app.config import Settings, get_settings
from app.models import ChatHistoryMessage, Source
from app.providers.base import ChatMessage, LLMProvider
from app.retriever import RetrievedChunk, retrieve

SYSTEM_PROMPT = """You are Marmin's UAE e-invoicing RFP assistant. Answer as a knowledgeable product expert.

Tone:
- Sound confident and direct. State facts as facts.
- Never use hedging or meta phrases such as "according to the knowledge base", "according to the provided context", "based on the context", "the context says", or "from the excerpts".
- Do not mention that you are using retrieved context or documents unless the user asks about sources.

Answering:
- Ground every claim in the supplied reference material. Prefer concrete details (protocols, algorithms, SLAs, RTO/RPO, processes).
- If the reference material supports the answer, give a clear RFP-ready response.
- If it does not contain the answer, say exactly: "I don't know the answer." Do not speculate or invent features, compliance claims, or legal advice.
- Keep answers concise and professional.
- You may cite source file paths when helpful, without framing them as "according to context".
- Ignore earlier assistant refusals if the current reference material has the answer.
"""

REFUSAL_MARKERS = (
    "do not have enough information",
    "don't have enough information",
    "couldn't find any relevant information",
    "no relevant information",
    "i don't know the answer",
    "i do not know the answer",
)


def build_context(chunks: list[RetrievedChunk]) -> str:
    if not chunks:
        return "No relevant knowledge-base excerpts were retrieved."
    parts: list[str] = []
    for i, chunk in enumerate(chunks, start=1):
        title = chunk.section_title or "Section"
        parts.append(
            f"[{i}] Source: {chunk.source_path} | {title}\n{chunk.text}"
        )
    return "\n\n---\n\n".join(parts)


def unique_sources(chunks: list[RetrievedChunk]) -> list[Source]:
    seen: set[str] = set()
    sources: list[Source] = []
    for chunk in chunks:
        key = chunk.source_path
        if key in seen:
            continue
        seen.add(key)
        sources.append(
            Source(path=chunk.source_path, section_title=chunk.section_title or None)
        )
    return sources


def _is_refusal(content: str) -> bool:
    lowered = content.lower()
    return any(marker in lowered for marker in REFUSAL_MARKERS)


async def chat_stream(
    message: str,
    history: list[ChatHistoryMessage],
    *,
    provider: LLMProvider,
    settings: Settings | None = None,
) -> tuple[list[Source], AsyncIterator[str]]:
    settings = settings or get_settings()
    chunks = await retrieve(message, provider=provider, settings=settings)
    sources = unique_sources(chunks)
    context = build_context(chunks)

    messages: list[ChatMessage] = [
        ChatMessage(role="system", content=SYSTEM_PROMPT),
    ]

    # Keep a short conversation window; drop prior refusals so they don't poison answers
    for item in history[-8:]:
        if item.role not in {"user", "assistant"} or not item.content.strip():
            continue
        if item.role == "assistant" and _is_refusal(item.content):
            continue
        messages.append(ChatMessage(role=item.role, content=item.content))

    # Put reference material with the user turn — more reliable for local models than a 2nd system message
    user_prompt = (
        f"Reference material (internal — do not mention this label in your reply):\n\n{context}\n\n"
        f"Question: {message}\n\n"
        "Answer confidently from the reference material. "
        "Do not say 'according to the context' or similar. "
        "If the material does not contain the answer, reply: I don't know the answer."
    )
    messages.append(ChatMessage(role="user", content=user_prompt))

    async def _stream() -> AsyncIterator[str]:
        async for token in provider.chat_stream(messages):
            yield token

    return sources, _stream()
