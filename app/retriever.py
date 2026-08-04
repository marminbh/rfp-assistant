from __future__ import annotations

from dataclasses import dataclass

from app.config import Settings, get_settings
from app.markets import Market, retrieval_markets
from app.providers.base import LLMProvider
from app.store import get_collection


@dataclass(frozen=True)
class RetrievedChunk:
    text: str
    source_path: str
    section_title: str
    market: str
    distance: float | None


def _is_useful_chunk(text: str) -> bool:
    body = text.strip()
    if len(body) < 40:
        return False
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    non_headings = [ln for ln in lines if not ln.startswith("#")]
    return bool(non_headings)


async def retrieve(
    query: str,
    *,
    provider: LLMProvider,
    market: Market,
    settings: Settings | None = None,
) -> list[RetrievedChunk]:
    settings = settings or get_settings()
    collection = get_collection(settings)
    if collection.count() == 0:
        return []

    embeddings = await provider.embed([query])
    fetch_n = min(max(settings.top_k * 3, settings.top_k), collection.count())
    allowed = retrieval_markets(market)
    result = collection.query(
        query_embeddings=embeddings,
        n_results=fetch_n,
        where={"market": {"$in": allowed}},
        include=["documents", "metadatas", "distances"],
    )

    documents = (result.get("documents") or [[]])[0]
    metadatas = (result.get("metadatas") or [[]])[0]
    distances = (result.get("distances") or [[]])[0]

    chunks: list[RetrievedChunk] = []
    for doc, metadata, distance in zip(documents, metadatas, distances):
        if not doc or not metadata or not _is_useful_chunk(doc):
            continue
        chunk_market = str(metadata.get("market") or "unknown")
        if chunk_market not in allowed:
            continue
        chunks.append(
            RetrievedChunk(
                text=doc,
                source_path=str(metadata.get("source_path", "unknown")),
                section_title=str(metadata.get("section_title") or ""),
                market=chunk_market,
                distance=float(distance) if distance is not None else None,
            )
        )
        if len(chunks) >= settings.top_k:
            break
    return chunks
