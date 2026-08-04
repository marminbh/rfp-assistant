# UAE E-Invoicing RFP Assistant

Local RAG chatbot for RFP questions about Marmin’s **UAE** and **OMN** e-invoicing solutions.

- Knowledge base: in-repo [`knowledge/`](knowledge/) segregated as `uae/`, `omn/`, and `shared/`
- Default LLM: **Ollama** (local chat + embeddings)
- Optional: **Gemini** via `LLM_PROVIDER=gemini`
- UI: simple web chat with market selector at `http://127.0.0.1:8787`

## Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) installed and running (default provider)

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Setup

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.ingest
uvicorn app.main:app --reload --host 127.0.0.1 --port 8787
```

Open [http://127.0.0.1:8787](http://127.0.0.1:8787).

> Important: Use `127.0.0.1`, not `localhost`, and avoid port `8000` if OrbStack (or another proxy) is bound to it. `http://localhost:8000` can hit that proxy instead of this app — health may look fine while chat returns empty.

## Configuration

See [`.env.example`](.env.example).

| Variable | Default | Notes |
|----------|---------|-------|
| `LLM_PROVIDER` | `ollama` | `ollama` or `gemini` |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | |
| `OLLAMA_CHAT_MODEL` | `llama3.2` | |
| `OLLAMA_EMBED_MODEL` | `nomic-embed-text` | |
| `GEMINI_API_KEY` | _(empty)_ | Required for Gemini |
| `GEMINI_CHAT_MODEL` | `gemini-3-flash` | |
| `GEMINI_EMBED_MODEL` | `gemini-embedding-001` | |
| `KB_PATH` | `./knowledge` | |
| `CHROMA_PATH` | `./data/chroma` | gitignored |
| `TOP_K` | `5` | retrieval depth |

### Switch to Gemini

```bash
# in .env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key
python -m app.ingest   # required — embedding spaces differ by provider
```

Chroma collections are provider-scoped (`rfp_ollama`, `rfp_gemini`) so indexes can coexist.

## Knowledge base

Edit markdown under `knowledge/`, then re-index from the UI (**Re-index knowledge base**) or:

```bash
python -m app.ingest
```

Ingest is incremental (file content hash). Each chunk is tagged with `market` (`uae`, `omn`, or `shared`). Chat retrieval is filtered to the selected market plus `shared`.

### Knowledge layout

```text
knowledge/
  uae/       # UAE-only RFP content
  omn/       # Oman-only RFP content
  shared/    # Company-wide facts for both markets
```

## API

- `GET /api/health` — provider status, KB path, chunk count
- `POST /api/ingest` — re-index current provider collection
- `POST /api/chat` — SSE stream (`sources`, `token`, `done`)
