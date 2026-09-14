#!/usr/bin/env python3
"""Generate the public RSS feed from the Tribune's static editions."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone, timedelta
from html import escape
from pathlib import Path

BASE_URL = "https://iqbalbhawana.github.io/bhawana-tribune/"
DESKS_RE = re.compile(r"const DESKS = (\[.*?\]);\s*let activeDeskId", re.S)


def parse_edition(path: Path) -> tuple[datetime, list[dict]]:
    html = path.read_text(encoding="utf-8")
    match = DESKS_RE.search(html)
    if not match:
        raise ValueError(f"could not find DESKS data in {path}")
    desks = json.loads(match.group(1))
    if not desks or not desks[0].get("date"):
        raise ValueError(f"edition has no date in {path}")
    local_date = datetime.strptime(desks[0]["date"], "%A, %B %d, %Y")
    return local_date.replace(tzinfo=timezone(timedelta(hours=5))), desks


def edition_paths(root: Path) -> list[Path]:
    dated = sorted(
        (p / "index.html" for p in root.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name)),
        reverse=True,
    )
    return [root / "index.html", *dated]


def item_description(desk: dict) -> str:
    parts = [str(desk.get("deck") or "")]
    body = desk.get("body")
    if isinstance(body, list):
        parts.extend(str(p) for p in body[:2])
    elif body:
        parts.append(str(body))
    text = " ".join(p.strip() for p in parts if p and p.strip())
    return text[:1800].rstrip() + ("…" if len(text) > 1800 else "")


def rfc822(dt: datetime) -> str:
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


def build_feed(root: Path) -> str:
    editions: dict[str, tuple[datetime, Path, list[dict]]] = {}
    for path in edition_paths(root):
        if not path.exists():
            continue
        edition_dt, desks = parse_edition(path)
        key = edition_dt.date().isoformat()
        editions.setdefault(key, (edition_dt, path, desks))

    if not editions:
        raise ValueError("no Tribune editions found")

    ordered = sorted(editions.values(), key=lambda item: item[0], reverse=True)
    latest_dt = ordered[0][0]
    items: list[str] = []
    for edition_dt, path, desks in ordered:
        date_path = edition_dt.date().isoformat()
        page_base = f"{BASE_URL}{date_path}/" if path.parent.name == date_path else BASE_URL
        for desk in sorted(desks, key=lambda item: int(item.get("id", 0))):
            desk_id = int(desk["id"])
            link = f"{page_base}?desk={desk_id}"
            title = f"Desk {desk_id:02d} • {desk.get('category') or desk.get('desk') or 'Tribune'} • {desk.get('headline') or 'Bhawana Tribune edition'}"
            items.append(
                "    <item>\n"
                f"      <title>{escape(title)}</title>\n"
                f"      <link>{escape(link)}</link>\n"
                f"      <guid isPermaLink=\"true\">{escape(link)}</guid>\n"
                f"      <pubDate>{rfc822(edition_dt)}</pubDate>\n"
                f"      <description>{escape(item_description(desk))}</description>\n"
                "    </item>"
            )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        "    <title>Bhawana Tribune</title>\n"
        f"    <link>{BASE_URL}</link>\n"
        "    <description>Daily web-magazine editions from Bhawana Tribune.</description>\n"
        "    <language>en</language>\n"
        f"    <lastBuildDate>{rfc822(latest_dt)}</lastBuildDate>\n"
        f"    <atom:link href=\"{BASE_URL}feed.xml\" rel=\"self\" type=\"application/rss+xml\" />\n"
        + "\n".join(items)
        + "\n  </channel>\n</rss>\n"
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    (root / "feed.xml").write_text(build_feed(root), encoding="utf-8")


if __name__ == "__main__":
    main()
