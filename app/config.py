from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ROOT_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    llm_provider: Literal["ollama", "gemini"] = "ollama"

    ollama_base_url: str = "http://localhost:11434"
    ollama_chat_model: str = "llama3.2"
    ollama_embed_model: str = "nomic-embed-text"

    gemini_api_key: str = ""
    gemini_chat_model: str = "gemini-3-flash"
    gemini_embed_model: str = "gemini-embedding-001"

    kb_path: Path = ROOT_DIR / "knowledge"
    chroma_path: Path = ROOT_DIR / "data" / "chroma"
    top_k: int = 8

    chunk_size: int = 1200
    chunk_overlap: int = 200

    @field_validator("kb_path", "chroma_path", mode="before")
    @classmethod
    def resolve_path(cls, value: str | Path) -> Path:
        path = Path(value)
        if not path.is_absolute():
            path = (ROOT_DIR / path).resolve()
        return path

    @property
    def collection_name(self) -> str:
        return f"rfp_{self.llm_provider}"

    @property
    def chat_model(self) -> str:
        if self.llm_provider == "gemini":
            return self.gemini_chat_model
        return self.ollama_chat_model

    @property
    def embed_model(self) -> str:
        if self.llm_provider == "gemini":
            return self.gemini_embed_model
        return self.ollama_embed_model


@lru_cache
def get_settings() -> Settings:
    return Settings()
