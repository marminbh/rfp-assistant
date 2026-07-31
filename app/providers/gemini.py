from __future__ import annotations

from collections.abc import AsyncIterator, Sequence

from google import genai
from google.genai import types

from app.providers.base import ChatMessage


class GeminiProvider:
    name = "gemini"

    def __init__(self, api_key: str, chat_model: str, embed_model: str) -> None:
        if not api_key:
            raise ValueError("GEMINI_API_KEY is required when LLM_PROVIDER=gemini")
        self.api_key = api_key
        self.chat_model = chat_model
        self.embed_model = embed_model
        self._client = genai.Client(api_key=api_key)

    async def embed(self, texts: Sequence[str]) -> list[list[float]]:
        vectors: list[list[float]] = []
        for text in texts:
            result = await self._client.aio.models.embed_content(
                model=self.embed_model,
                contents=text,
                config=types.EmbedContentConfig(output_dimensionality=768),
            )
            embeddings = result.embeddings or []
            if not embeddings or embeddings[0].values is None:
                raise RuntimeError("Gemini embedding response missing values")
            vectors.append(list(embeddings[0].values))
        return vectors

    async def chat_stream(self, messages: Sequence[ChatMessage]) -> AsyncIterator[str]:
        system_parts = [m.content for m in messages if m.role == "system"]
        history: list[types.Content] = []
        for message in messages:
            if message.role == "system":
                continue
            role = "model" if message.role == "assistant" else "user"
            history.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=message.content)],
                )
            )

        config = types.GenerateContentConfig(
            system_instruction="\n\n".join(system_parts) if system_parts else None,
        )

        stream = await self._client.aio.models.generate_content_stream(
            model=self.chat_model,
            contents=history,
            config=config,
        )
        async for chunk in stream:
            text = getattr(chunk, "text", None)
            if text:
                yield text

    async def health(self) -> dict:
        return {
            "ok": bool(self.api_key),
            "chat_model": self.chat_model,
            "embed_model": self.embed_model,
            "api_key_configured": bool(self.api_key),
        }