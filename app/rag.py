from __future__ import annotations

from collections.abc import AsyncIterator

from app.config import Settings, get_settings
from app.models import ChatHistoryMessage, Source
from app.providers.base import ChatMessage, LLMProvider
from app.retriever import RetrievedChunk, retrieve

SYSTEM_PROMPT = """You are an assistant that helps answer RFP questions about Marmin's UAE e-invoicing solution.

Rules:
- Use the knowledge-base context below the user question. If the context contains relevant facts, answer with those facts.
- Prefer concrete details from the context (algorithms, protocols, retention periods, RTO/RPO, processes).
- Only say you do not have enough information when the context truly has no relevant facts for the question.
- Do not invent product features, compliance guarantees, or legal advice beyond the context.
- Be concise, professional, and suitable for an RFP response.
- Cite supporting source file paths from the context when useful.
- Ignore prior assistant messages that said information was missing if the current context now has the answer.
"""

REFUSAL_MARKERS = (
    "do not have enough information",
    "don't have enough information",
    "couldn't find any relevant information",
    "no relevant information",
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

    # Put context with the user turn — more reliable for local models than a 2nd system message
    user_prompt = (
        f"Knowledge-base context:\n\n{context}\n\n"
        f"Question: {message}\n\n"
        "Answer using the knowledge-base context above."
    )
    messages.append(ChatMessage(role="user", content=user_prompt))

    async def _stream() -> AsyncIterator[str]:
        async for token in provider.chat_stream(messages):
            yield token

    return sources, _stream()
