from __future__ import annotations

import json
from collections.abc import AsyncIterator, Sequence
from typing import Any

import httpx

from app.providers.base import ChatMessage


class OllamaProvider:
    name = "ollama"

    def __init__(self, base_url: str, chat_model: str, embed_model: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.chat_model = chat_model
        self.embed_model = embed_model

    async def embed(self, texts: Sequence[str]) -> list[list[float]]:
        vectors: list[list[float]] = []
        async with httpx.AsyncClient(timeout=120.0) as client:
            for text in texts:
                embedding = await self._embed_one(client, text)
                vectors.append(embedding)
        return vectors

    async def _embed_one(self, client: httpx.AsyncClient, text: str) -> list[float]:
        # Prefer modern /api/embed; fall back to /api/embeddings
        response = await client.post(
            f"{self.base_url}/api/embed",
            json={"model": self.embed_model, "input": text},
        )
        if response.status_code == 404:
            response = await client.post(
                f"{self.base_url}/api/embeddings",
                json={"model": self.embed_model, "prompt": text},
            )
        response.raise_for_status()
        data = response.json()
        if "embeddings" in data and data["embeddings"]:
            return data["embeddings"][0]
        if "embedding" in data and data["embedding"]:
            return data["embedding"]
        raise RuntimeError(f"Ollama embeddings response missing vector: {data}")

    async def chat_stream(self, messages: Sequence[ChatMessage]) -> AsyncIterator[str]:
        payload: dict[str, Any] = {
            "model": self.chat_model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": True,
        }
        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream(
                "POST",
                f"{self.base_url}/api/chat",
                json=payload,
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if not line:
                        continue
                    chunk = json.loads(line)
                    message = chunk.get("message") or {}
                    content = message.get("content")
                    if content:
                        yield content
                    if chunk.get("done"):
                        break

    async def health(self) -> dict:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                response.raise_for_status()
                models = [m.get("name", "") for m in response.json().get("models", [])]
                return {
                    "ok": True,
                    "base_url": self.base_url,
                    "chat_model": self.chat_model,
                    "embed_model": self.embed_model,
                    "models_available": models,
                    "chat_model_present": any(m.startswith(self.chat_model) for m in models),
                    "embed_model_present": any(
                        m.startswith(self.embed_model) for m in models
                    ),
                }
        except Exception as exc:  # noqa: BLE001 - surfaced in health payload
            return {
                "ok": False,
                "base_url": self.base_url,
                "error": str(exc),
            }
