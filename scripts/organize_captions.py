#!/usr/bin/env python3
"""Turn yt-dlp output in <dir>/raw/ into clean transcripts plus an index.

  <dir>/transcripts/YYYY-MM-DD_<id>_<slug>.txt   one per video, with a header
  <dir>/videos.csv                                 index of all videos
  <dir>/INDEX.md                                   same index, readable
"""
import csv
import json
import re
import sys
from pathlib import Path

# Preference when several caption tracks exist: manual English first, then auto.
LANG_ORDER = ["en", "en-US", "en-GB", "en-orig"]


def slugify(text, limit=60):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:limit].rstrip("-") or "video"


def vtt_to_text(vtt):
    lines, last = [], None
    for line in vtt.splitlines():
        if not line.strip() or "-->" in line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if line.strip().isdigit():
            continue
        clean = re.sub(r"<[^>]+>", "", line).replace("&nbsp;", " ").replace("&amp;", "&").strip()
        # Auto-captions repeat each line in the following cue; drop consecutive repeats.
        if clean and clean != last:
            lines.append(clean)
            last = clean
    text = " ".join(lines)
    # Break into ~120-word paragraphs for readability.
    words = text.split()
    return "\n\n".join(" ".join(words[i:i + 120]) for i in range(0, len(words), 120))


def pick_caption(raw, base):
    tracks = {p.name[len(base) + 1:-4]: p for p in raw.glob(f"{base}.*.vtt")}
    for lang in LANG_ORDER:
        if lang in tracks:
            return lang, tracks[lang]
    if tracks:
        lang = sorted(tracks)[0]
        return lang, tracks[lang]
    return None, None


def main():
    root = Path(sys.argv[1]).resolve()
    raw, out = root / "raw", root / "transcripts"
    out.mkdir(exist_ok=True)
    rows = []
    for info_path in sorted(raw.glob("*.info.json"), reverse=True):
        base = info_path.name[: -len(".info.json")]
        info = json.loads(info_path.read_text(encoding="utf-8"))
        date = base.split("_", 1)[0]
        lang, vtt = pick_caption(raw, base)
        row = {
            "date": date,
            "id": info.get("id", ""),
            "title": info.get("title", ""),
            "url": info.get("webpage_url") or f"https://www.youtube.com/watch?v={info.get('id', '')}",
            "duration_min": round((info.get("duration") or 0) / 60),
            "caption_lang": lang or "",
            "words": 0,
            "transcript": "",
        }
        if vtt:
            body = vtt_to_text(vtt.read_text(encoding="utf-8", errors="replace"))
            name = f"{date}_{row['id']}_{slugify(row['title'])}.txt"
            header = (
                f"Title: {row['title']}\nDate: {date}\nURL: {row['url']}\n"
                f"Duration: {row['duration_min']} min\nCaptions: {lang}\n"
                f"Description:\n{(info.get('description') or '').strip()[:1500]}\n"
                f"\n{'=' * 72}\n\n"
            )
            (out / name).write_text(header + body + "\n", encoding="utf-8")
            row["words"] = len(body.split())
            row["transcript"] = f"transcripts/{name}"
        rows.append(row)

    fields = list(rows[0].keys()) if rows else ["date", "id", "title", "url", "duration_min", "caption_lang", "words", "transcript"]
    with open(root / "videos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    with_caps = [r for r in rows if r["transcript"]]
    md = [f"# {root.name}: video index", "",
          f"{len(rows)} videos, {len(with_caps)} with captions, "
          f"{sum(r['words'] for r in rows):,} words total.", "",
          "| Date | Title | Min | Captions | Words | Transcript |", "|---|---|---|---|---|---|"]
    for r in rows:
        title = r["title"].replace("|", "/")
        link = f"[txt]({r['transcript']})" if r["transcript"] else "**missing**"
        md.append(f"| {r['date']} | [{title}]({r['url']}) | {r['duration_min']} | {r['caption_lang'] or '-'} | {r['words']:,} | {link} |")
    (root / "INDEX.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"{len(rows)} videos indexed, {len(with_caps)} with captions -> {root}/INDEX.md")
    missing = [r for r in rows if not r["transcript"]]
    if missing:
        print("No captions for:", ", ".join(f"{r['date']} {r['id']}" for r in missing))


if __name__ == "__main__":
    main()
