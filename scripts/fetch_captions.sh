#!/bin/bash
# Downloads English captions (manual or auto-generated) for the latest N videos
# of a YouTube channel into captions/<channel>/, as plain-text transcripts.
#
# Usage: scripts/fetch_captions.sh [channel_url] [count]
#   scripts/fetch_captions.sh https://www.youtube.com/@bitcoinstrategy 50
#
# Needs yt-dlp (bundled with agent-reach, or: pipx install yt-dlp).
# If YouTube answers "Sign in to confirm you're not a bot", add
#   --cookies-from-browser chrome
# to the yt-dlp call below.
set -euo pipefail

CHANNEL="${1:-https://www.youtube.com/@bitcoinstrategy}"
COUNT="${2:-50}"
NAME=$(basename "$CHANNEL" | tr -d '@')
OUT="$(dirname "$0")/../captions/$NAME"
mkdir -p "$OUT"

yt-dlp "$CHANNEL/videos" \
  --playlist-end "$COUNT" \
  --skip-download --write-subs --write-auto-subs \
  --sub-langs "en.*,en" --sub-format vtt \
  --sleep-requests 1 --ignore-errors \
  -o "$OUT/%(upload_date)s_%(id)s_%(title).80B.%(ext)s"

# Strip VTT timing/markup and de-duplicate the rolling lines auto-captions produce.
for f in "$OUT"/*.vtt; do
  [ -e "$f" ] || continue
  txt="${f%.vtt}"; txt="${txt%.*}.txt"
  sed -e '/-->/d' -e '/^WEBVTT/d' -e '/^Kind:/d' -e '/^Language:/d' -e 's/<[^>]*>//g' -e '/^[[:space:]]*$/d' "$f" \
    | awk '!seen[$0]++' > "$txt"
  rm "$f"
done

echo "Transcripts: $(ls "$OUT"/*.txt 2>/dev/null | wc -l) files in $OUT"
