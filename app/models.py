from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class ChatHistoryMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    history: list[ChatHistoryMessage] = Field(default_factory=list)
    market: Literal["uae", "omn"] = "uae"


class Source(BaseModel):
    path: str
    section_title: str | None = None
    market: str | None = None


class HealthResponse(BaseModel):
    ok: bool
    provider: str
    chat_model: str
    embed_model: str
    kb_path: str
    kb_exists: bool
    collection: str
    document_count: int
    markets: list[str]
    market_counts: dict[str, int]
    provider_health: dict


class IngestResponse(BaseModel):
    ok: bool
    provider: str
    collection: str
    files_scanned: int
    files_indexed: int
    chunks_upserted: int
    chunks_removed: int
    market_counts: dict[str, int] = Field(default_factory=dict)
    message: str
