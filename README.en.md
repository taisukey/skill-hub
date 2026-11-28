# skill-hub

<p align="center">
  <a href="https://github.com/taisukey/skill-hub/blob/main/LICENSE"><img src="https://img.shields.io/github/license/taisukey/skill-hub" alt="License: MIT"></a>
</p>
<p align="center">
  <a href="README.md">日本語</a> · <b>English</b>
</p>

A catalog of **Agent Skills** — repositories that contain a `SKILL.md` — filtered from my GitHub Starred, plus a CLI that installs them into Muse, Hermes and DeepSeek Harness (DSH). From 135 starred repositories, 60 hold skills — 1,258 skills in total — and are classified here.

## Categories

- `dedicated` — repositories whose purpose is the skill itself (install candidates)
- `collection` — large collections (e.g. Composio); install only the ones you name
- `agent-bundled` — skill libraries shipped with an agent itself
- `product-internal` — skills for developing or using one product (normally not installed)

The full list is [CATALOG.md](CATALOG.md); the machine-readable version is `catalog.json`.

## Usage

```sh
bin/skillhub search <keyword>
bin/skillhub install <skill-name> [--agent Muse|hermes|dsh]
bin/skillhub installed
bin/skillhub remove <skill-name>
```

Install targets are detected per machine (Muse, Hermes and DSH each have their own skills folder). Source repositories are shallow-cloned into `cache/` and the state is recorded in `installed.json` (both outside git).

A meta-skill at `meta/skillhub/SKILL.md` lets an agent search the catalog and install skills itself when placed in that agent's skills folder.

## Regenerating the catalog

`python3 build_catalog.py` — run on a machine with the `gh` CLI: fetches Starred, scans for `SKILL.md`, collects frontmatter, and applies the curated classification overrides.

## License and sources

This repository's own work (the CLI, the catalog generation, the curation) is under the MIT License. Each catalogued skill remains under its upstream repository's license — see [NOTICE.md](NOTICE.md) and [SOURCES.md](SOURCES.md). Upstream licenses are recorded automatically on every regeneration and watched by `check_licenses.py`.

The full README is in [Japanese](README.md).
