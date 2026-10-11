#!/bin/bash
# Downloads captions + metadata for the latest N videos of a YouTube channel,
# then organizes them into research/<channel>/ (see research/README.md).
#
# Usage:
#   scripts/fetch_channel.sh [channel_url] [count] [sub_langs]
#   scripts/fetch_channel.sh https://www.youtube.com/@bitcoinstrategy 50 "en.*"
#
# If YouTube answers "Sign in to confirm you're not a bot", re-run with your
# browser's YouTube cookies (read locally by yt-dlp, never uploaded):
#   YTDLP_BROWSER=chrome scripts/fetch_channel.sh ...
# Re-running is safe: already-downloaded videos are skipped.
set -euo pipefail

CHANNEL="${1:-https://www.youtube.com/@bitcoinstrategy}"
COUNT="${2:-50}"
LANGS="${3:-en.*}"
NAME=$(basename "$CHANNEL" | tr -d '@')
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/research/$NAME"
RAW="$DIR/raw"
mkdir -p "$RAW"

command -v yt-dlp >/dev/null || { echo "yt-dlp not found. Install it: brew install yt-dlp"; exit 1; }

COOKIES=()
if [ -n "${YTDLP_BROWSER:-}" ]; then
  COOKIES=(--cookies-from-browser "$YTDLP_BROWSER")
fi

yt-dlp "$CHANNEL/videos" \
  --playlist-end "$COUNT" \
  --skip-download --write-info-json --no-write-playlist-metafiles \
  --write-subs --write-auto-subs --sub-langs "$LANGS" --sub-format vtt \
  --sleep-requests 1 --sleep-subtitles 2 \
  --download-archive "$RAW/.archive.txt" \
  --ignore-errors \
  ${COOKIES[@]+"${COOKIES[@]}"} \
  -o "$RAW/%(upload_date>%Y-%m-%d)s_%(id)s.%(ext)s" || true

python3 "$ROOT/scripts/organize_captions.py" "$DIR"
