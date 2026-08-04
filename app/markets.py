from __future__ import annotations

from typing import Literal

Market = Literal["uae", "omn"]
MARKETS: tuple[Market, ...] = ("uae", "omn")
MARKET_LABELS: dict[Market, str] = {
    "uae": "UAE",
    "omn": "OMN",
}


def normalize_market(value: str | None) -> Market:
    market = (value or "uae").strip().lower()
    if market not in MARKETS:
        raise ValueError(f"Invalid market '{value}'. Expected one of: {', '.join(MARKETS)}")
    return market  # type: ignore[return-value]


def market_from_source_path(relative_path: str) -> str:
    """Derive market tag from knowledge-relative path (uae/..., omn/..., shared/...)."""
    top = relative_path.replace("\\", "/").split("/", 1)[0].lower()
    if top in {"uae", "omn", "shared"}:
        return top
    # Legacy/unscoped files — treat as shared so they remain reachable
    return "shared"


def retrieval_markets(market: Market) -> list[str]:
    return [market, "shared"]
