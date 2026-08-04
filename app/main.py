from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from app.config import get_settings
from app.ingest import ingest_knowledge
from app.markets import MARKETS, normalize_market
from app.models import ChatRequest, HealthResponse, IngestResponse
from app.providers.factory import build_provider
from app.rag import chat_stream
from app.store import collection_count, market_counts

ROOT_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = ROOT_DIR / "static"

app = FastAPI(title="Marmin E-Invoicing RFP Assistant", version="1.1.0")


@app.get("/api/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    settings = get_settings()
    try:
        provider = build_provider(settings)
        provider_health = await provider.health()
    except Exception as exc:  # noqa: BLE001
        provider_health = {"ok": False, "error": str(exc)}
        provider_ok = False
    else:
        provider_ok = bool(provider_health.get("ok", False))

    kb_exists = settings.kb_path.exists()
    try:
        doc_count = collection_count(settings)
        counts = market_counts(settings)
    except Exception:  # noqa: BLE001
        doc_count = 0
        counts = {}

    return HealthResponse(
        ok=provider_ok and kb_exists,
        provider=settings.llm_provider,
        chat_model=settings.chat_model,
        embed_model=settings.embed_model,
        kb_path=str(settings.kb_path),
        kb_exists=kb_exists,
        collection=settings.collection_name,
        document_count=doc_count,
        markets=list(MARKETS),
        market_counts=counts,
        provider_health=provider_health,
    )


@app.post("/api/ingest", response_model=IngestResponse)
async def ingest() -> IngestResponse:
    result = await ingest_knowledge()
    if not result.ok:
        raise HTTPException(status_code=400, detail=result.message)
    return result


def _sse(event: str, data: str) -> str:
    return f"event: {event}\ndata: {data}\n\n"


@app.post("/api/chat")
async def chat(request: ChatRequest) -> StreamingResponse:
    settings = get_settings()
    try:
        market = normalize_market(request.market)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    try:
        provider = build_provider(settings)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    if collection_count(settings) == 0:
        raise HTTPException(
            status_code=400,
            detail="Knowledge base is not indexed. Click Re-index or run: python -m app.ingest",
        )

    sources, token_stream = await chat_stream(
        request.message,
        request.history,
        provider=provider,
        market=market,
        settings=settings,
    )

    async def event_generator():
        yield _sse("sources", json.dumps([s.model_dump() for s in sources]))
        try:
            async for token in token_stream:
                yield _sse("token", json.dumps({"text": token}))
            yield _sse("done", "{}")
        except Exception as exc:  # noqa: BLE001
            yield _sse("error", json.dumps({"message": str(exc)}))

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
