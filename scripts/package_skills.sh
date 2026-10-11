#!/bin/bash
# Zips each skill in .claude/skills/ into dist/<name>.zip for upload to
# claude.ai (Settings > Capabilities > Skills > Upload skill).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for dir in .claude/skills/*/; do
  name=$(basename "$dir")
  rm -f "dist/$name.zip"
  (cd .claude/skills && zip -qr "../../dist/$name.zip" "$name" -x '*/__pycache__/*')
  echo "dist/$name.zip"
done
