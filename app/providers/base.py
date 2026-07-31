from __future__ import annotations

from collections.abc import AsyncIterator, Sequence
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ChatMessage:
    role: str  # system | user | assistant
    content: str


class LLMProvider(Protocol):
    name: str

    async def embed(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one embedding vector per input text."""

    async def chat_stream(self, messages: Sequence[ChatMessage]) -> AsyncIterator[str]:
        """Yield response text chunks."""

    async def health(self) -> dict:
        """Provider-specific health details."""