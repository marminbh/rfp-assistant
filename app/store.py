from __future__ import annotations

from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any

import chromadb
from chromadb.api.models.Collection import Collection

from app.config import Settings, get_settings


@lru_cache
def get_chroma_client(chroma_path: str) -> chromadb.PersistentClient:
    Path(chroma_path).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=chroma_path)


def get_collection(settings: Settings | None = None) -> Collection:
    settings = settings or get_settings()
    client = get_chroma_client(str(settings.chroma_path))
    return client.get_or_create_collection(
        name=settings.collection_name,
        metadata={"hnsw:space": "cosine", "provider": settings.llm_provider},
    )


def collection_count(settings: Settings | None = None) -> int:
    return get_collection(settings).count()


def market_counts(settings: Settings | None = None) -> dict[str, int]:
    collection = get_collection(settings)
    data = collection.get(include=["metadatas"])
    counter: Counter[str] = Counter()
    for metadata in data.get("metadatas") or []:
        if not metadata:
            continue
        counter[str(metadata.get("market") or "unknown")] += 1
    return dict(sorted(counter.items()))


def existing_file_hashes(collection: Collection) -> dict[str, str]:
    """Map source_path -> file_hash for currently indexed chunks."""
    result: dict[str, str] = {}
    data = collection.get(include=["metadatas"])
    for metadata in data.get("metadatas") or []:
        if not metadata:
            continue
        path = metadata.get("source_path")
        file_hash = metadata.get("file_hash")
        if path and file_hash:
            result[str(path)] = str(file_hash)
    return result


def delete_by_source_paths(collection: Collection, paths: list[str]) -> int:
    if not paths:
        return 0
    data = collection.get(include=["metadatas"])
    ids_to_delete: list[str] = []
    path_set = set(paths)
    for chunk_id, metadata in zip(data.get("ids") or [], data.get("metadatas") or []):
        if metadata and metadata.get("source_path") in path_set:
            ids_to_delete.append(chunk_id)
    if ids_to_delete:
        collection.delete(ids=ids_to_delete)
    return len(ids_to_delete)


def upsert_chunks(
    collection: Collection,
    *,
    ids: list[str],
    documents: list[str],
    embeddings: list[list[float]],
    metadatas: list[dict[str, Any]],
) -> None:
    if not ids:
        return
    # Chroma batch size safety
    batch_size = 100
    for start in range(0, len(ids), batch_size):
        end = start + batch_size
        collection.upsert(
            ids=ids[start:end],
            documents=documents[start:end],
            embeddings=embeddings[start:end],
            metadatas=metadatas[start:end],
        )
