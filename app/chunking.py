from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


INCLUDE_SUFFIXES = {".md", ".txt", ".mdx"}
SKIP_DIR_NAMES = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "data",
    ".chroma",
}

# Bump when chunking logic changes so ingest reindexes unchanged files.
CHUNKER_VERSION = "2"


@dataclass(frozen=True)
class DocumentChunk:
    chunk_id: str
    text: str
    source_path: str
    section_title: str
    file_hash: str


def iter_knowledge_files(kb_path: Path) -> list[Path]:
    files: list[Path] = []
    if not kb_path.exists():
        return files
    for path in sorted(kb_path.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        if path.name.lower() == "readme.md":
            continue
        files.append(path)
    return files


def file_content_hash(content: str) -> str:
    payload = f"{CHUNKER_VERSION}\n{content}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def chunk_markdown(
    content: str,
    relative_path: str,
    *,
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
) -> list[DocumentChunk]:
    content = content.replace("\r\n", "\n").strip()
    if not content:
        return []

    file_hash = file_content_hash(content)
    sections = _split_by_headings(content)
    sections = _merge_thin_sections(sections)
    chunks: list[DocumentChunk] = []
    index = 0

    for section_title, section_body in sections:
        pieces = _window_text(section_body, chunk_size=chunk_size, overlap=chunk_overlap)
        for piece in pieces:
            text = piece.strip()
            if not text or _is_heading_only(text):
                continue
            chunk_id = hashlib.sha256(
                f"{relative_path}:{index}:{file_hash}:{text[:64]}".encode()
            ).hexdigest()[:24]
            chunks.append(
                DocumentChunk(
                    chunk_id=chunk_id,
                    text=text,
                    source_path=relative_path,
                    section_title=section_title,
                    file_hash=file_hash,
                )
            )
            index += 1
    return chunks


def _is_heading_only(text: str) -> bool:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return True
    return all(re.match(r"^#{1,6}\s+\S", ln) for ln in lines)


def _split_by_headings(content: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"(?m)^(#{1,6})\s+(.+)$")
    matches = list(pattern.finditer(content))
    if not matches:
        return [("Document", content)]

    sections: list[tuple[str, str]] = []
    preamble = content[: matches[0].start()].strip()
    if preamble:
        sections.append(("Document", preamble))

    for i, match in enumerate(matches):
        title = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end].strip()
        section_text = f"# {title}\n\n{body}".strip()
        sections.append((title, section_text))
    return sections


def _merge_thin_sections(
    sections: list[tuple[str, str]],
    *,
    min_chars: int = 120,
) -> list[tuple[str, str]]:
    """Merge title-only / very short sections into the following section."""
    if not sections:
        return sections

    merged: list[tuple[str, str]] = []
    pending_title: str | None = None
    pending_text = ""

    for title, text in sections:
        candidate_title = pending_title or title
        candidate_text = f"{pending_text}\n\n{text}".strip() if pending_text else text

        # Keep merging forward while content is too thin
        body_without_heading = re.sub(r"^#{1,6}\s+.+$", "", candidate_text, count=1, flags=re.M).strip()
        if len(body_without_heading) < min_chars:
            pending_title = candidate_title
            pending_text = candidate_text
            continue

        merged.append((candidate_title, candidate_text))
        pending_title = None
        pending_text = ""

    if pending_text:
        if merged:
            prev_title, prev_text = merged[-1]
            merged[-1] = (prev_title, f"{prev_text}\n\n{pending_text}".strip())
        else:
            merged.append((pending_title or "Document", pending_text))

    return merged


def _window_text(text: str, *, chunk_size: int, overlap: int) -> list[str]:
    if len(text) <= chunk_size:
        return [text]

    pieces: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        if end < len(text):
            split_at = text.rfind("\n\n", start, end)
            if split_at > start + chunk_size // 3:
                end = split_at
        pieces.append(text[start:end])
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return pieces
