from __future__ import annotations

from dataclasses import dataclass

from app.config import Settings, get_settings
from app.providers.base import LLMProvider
from app.store import get_collection


@dataclass(frozen=True)
class RetrievedChunk:
    text: str
    source_path: str
    section_title: str
    distance: float | None


def _is_useful_chunk(text: str) -> bool:
    body = text.strip()
    if len(body) < 40:
        return False
    # Drop heading-only leftovers
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    non_headings = [ln for ln in lines if not ln.startswith("#")]
    return bool(non_headings)


async def retrieve(
    query: str,
    *,
    provider: LLMProvider,
    settings: Settings | None = None,
) -> list[RetrievedChunk]:
    settings = settings or get_settings()
    collection = get_collection(settings)
    if collection.count() == 0:
        return []

    embeddings = await provider.embed([query])
    # Over-fetch then filter thin chunks
    fetch_n = min(max(settings.top_k * 3, settings.top_k), collection.count())
    result = collection.query(
        query_embeddings=embeddings,
        n_results=fetch_n,
        include=["documents", "metadatas", "distances"],
    )

    documents = (result.get("documents") or [[]])[0]
    metadatas = (result.get("metadatas") or [[]])[0]
    distances = (result.get("distances") or [[]])[0]

    chunks: list[RetrievedChunk] = []
    for doc, metadata, distance in zip(documents, metadatas, distances):
        if not doc or not metadata or not _is_useful_chunk(doc):
            continue
        chunks.append(
            RetrievedChunk(
                text=doc,
                source_path=str(metadata.get("source_path", "unknown")),
                section_title=str(metadata.get("section_title") or ""),
                distance=float(distance) if distance is not None else None,
            )
        )
        if len(chunks) >= settings.top_k:
            break
    return chunks
