from __future__ import annotations

import asyncio
from pathlib import Path

from app.chunking import chunk_markdown, iter_knowledge_files
from app.config import Settings, get_settings
from app.models import IngestResponse
from app.providers.factory import build_provider
from app.store import (
    delete_by_source_paths,
    existing_file_hashes,
    get_collection,
    upsert_chunks,
)


async def ingest_knowledge(settings: Settings | None = None) -> IngestResponse:
    settings = settings or get_settings()
    kb_path: Path = settings.kb_path
    if not kb_path.exists():
        return IngestResponse(
            ok=False,
            provider=settings.llm_provider,
            collection=settings.collection_name,
            files_scanned=0,
            files_indexed=0,
            chunks_upserted=0,
            chunks_removed=0,
            message=f"Knowledge path does not exist: {kb_path}",
        )

    provider = build_provider(settings)
    collection = get_collection(settings)
    current_hashes = existing_file_hashes(collection)
    files = iter_knowledge_files(kb_path)

    seen_paths: set[str] = set()
    files_indexed = 0
    chunks_upserted = 0
    chunks_removed = 0

    for file_path in files:
        relative = str(file_path.relative_to(kb_path)).replace("\\", "/")
        seen_paths.add(relative)
        content = file_path.read_text(encoding="utf-8")
        chunks = chunk_markdown(
            content,
            relative,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )
        if not chunks:
            continue

        file_hash = chunks[0].file_hash
        if current_hashes.get(relative) == file_hash:
            continue

        removed = delete_by_source_paths(collection, [relative])
        chunks_removed += removed

        texts = [c.text for c in chunks]
        embeddings = await provider.embed(texts)
        upsert_chunks(
            collection,
            ids=[c.chunk_id for c in chunks],
            documents=texts,
            embeddings=embeddings,
            metadatas=[
                {
                    "source_path": c.source_path,
                    "section_title": c.section_title,
                    "file_hash": c.file_hash,
                    "provider": settings.llm_provider,
                }
                for c in chunks
            ],
        )
        files_indexed += 1
        chunks_upserted += len(chunks)

    stale_paths = [path for path in current_hashes if path not in seen_paths]
    chunks_removed += delete_by_source_paths(collection, stale_paths)

    return IngestResponse(
        ok=True,
        provider=settings.llm_provider,
        collection=settings.collection_name,
        files_scanned=len(files),
        files_indexed=files_indexed,
        chunks_upserted=chunks_upserted,
        chunks_removed=chunks_removed,
        message=(
            f"Indexed {files_indexed} changed file(s); "
            f"upserted {chunks_upserted} chunk(s); removed {chunks_removed} stale chunk(s)."
        ),
    )


def main() -> None:
    result = asyncio.run(ingest_knowledge())
    print(result.model_dump_json(indent=2))
    if not result.ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
