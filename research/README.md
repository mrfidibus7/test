# Research workspace

One folder per YouTube channel, created by `scripts/fetch_channel.sh`:

```
research/
└── bitcoinstrategy/
    ├── INDEX.md                 readable index: date, title, length, caption status, words
    ├── videos.csv               same index, for spreadsheets/scripts
    ├── transcripts/             one clean .txt per video (header: title, date, URL, description)
    │   └── 2026-10-01_<videoid>_<title-slug>.txt
    ├── raw/                     yt-dlp output (.info.json, .vtt); safe to delete
    └── analysis/                written by Claude from the transcripts
        ├── methods.md           his analysis methods, generalized, with cited examples
        ├── recap-table.md       every coin: angles, Buy/Hold/Sell, score /10, thesis
        └── recap-table.csv      same table for Excel/Numbers/Sheets
```

`raw/` and `transcripts/` are git-ignored because this repo is public. Everything else is
committed. To refresh, re-run the fetch script: it only downloads new videos and rebuilds
the index.
