from __future__ import annotations

from functools import lru_cache

from app.config import Settings, get_settings
from app.providers.base import LLMProvider
from app.providers.gemini import GeminiProvider
from app.providers.ollama import OllamaProvider


def build_provider(settings: Settings) -> LLMProvider:
    if settings.llm_provider == "gemini":
        return GeminiProvider(
            api_key=settings.gemini_api_key,
            chat_model=settings.gemini_chat_model,
            embed_model=settings.gemini_embed_model,
        )
    return OllamaProvider(
        base_url=settings.ollama_base_url,
        chat_model=settings.ollama_chat_model,
        embed_model=settings.ollama_embed_model,
    )


@lru_cache
def get_provider() -> LLMProvider:
    return build_provider(get_settings())


def reset_provider_cache() -> None:
    get_provider.cache_clear()
