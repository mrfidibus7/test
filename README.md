# Claude skills: public-apis + agent-reach

Two [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that let Claude use:

| Skill | Wraps | What Claude can do |
|---|---|---|
| `public-apis` | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Search ~1,900 free APIs offline (by keyword, category, auth, HTTPS, CORS), read their docs, then call them |
| `agent-reach` | [Panniantong/agent-reach](https://github.com/Panniantong/agent-reach) @ `94f06c1` | Read/search the web, YouTube transcripts, GitHub, RSS, Twitter/X, Reddit, Bilibili… through upstream CLIs |

Layout:

```
.claude/skills/public-apis/   SKILL.md, scripts/search_apis.py, scripts/build_catalog.py, data/apis.json
.claude/skills/agent-reach/   upstream SKILL.md (+ setup notes), references/, LICENSE
dist/*.zip                    the same skills, zipped for claude.ai upload
scripts/package_skills.sh     rebuilds dist/
scripts/fetch_channel.sh      downloads a YouTube channel's captions into research/<channel>/
research/                     transcripts + analysis per channel (see research/README.md)
```

## Making them available everywhere

Skills don't sync automatically across Claude products, so install them once per surface:

1. **Claude Code in this repo** (CLI, desktop, web/cloud): automatic. Claude picks up
   `.claude/skills/` when a session opens this repo.
2. **Claude Code in every project on your machine**: copy them to your personal skills dir:
   `cp -r .claude/skills/* ~/.claude/skills/`
3. **claude.ai / Claude desktop & mobile chats**: enable *Code execution and file creation*
   under Settings → Capabilities, then under Skills click *Upload skill* and upload
   `dist/public-apis.zip` (and `dist/agent-reach.zip` if you want it). After that, skills
   are available in all your conversations with any model that supports skills.
4. **Claude API / Agent SDK**: upload the same zips via the Skills API, or point the SDK at
   `.claude/skills/`.

### Caveats

- **Network access.** Claude can only call an API whose host its sandbox allows. In Claude
  Code cloud sessions, set the environment's network access to *Full*, or add the API hosts
  under *Allowed domains* ([docs](https://code.claude.com/docs/en/cloud-environments#network-access)).
  On claude.ai, check the code-execution network/domain allowlist setting. Searching the catalog itself works offline.
- **agent-reach needs a shell with installs allowed.** It's a Python CLI that drives other CLIs
  (`yt-dlp`, `gh`, `mcporter`, `twitter`, `opencli`…). It works best in Claude Code on your
  own machine; on claude.ai it's limited to what the sandbox can install and reach. Login-backed
  platforms (Twitter, Reddit, XiaoHongShu, Facebook, Instagram) need your cookies or browser session.
  Install it from GitHub, not PyPI (the PyPI `agent-reach` is an unrelated package):
  `uv tool install "agent-reach @ git+https://github.com/Panniantong/agent-reach@94f06c1969dfc1834001269d79d3ad0972d9dee6"`

## Updating

```bash
python3 .claude/skills/public-apis/scripts/build_catalog.py   # refresh API catalog
scripts/package_skills.sh                                     # rebuild zips, then re-upload to claude.ai
```

To bump agent-reach, re-copy `agent_reach/skill/SKILL_en.md` + `references/` from upstream and
update the pinned commit in `.claude/skills/agent-reach/SKILL.md` and this README.
