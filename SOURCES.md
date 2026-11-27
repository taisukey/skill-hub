# SOURCES — 収録リポジトリの出所とライセンス

skill-hub のカタログ（`catalog.json` / `CATALOG.md`）が参照する上流リポジトリの一覧。
各スキルは各リポジトリのライセンスに従う。skill-hub 自体はスキルの複製を保持せず、
導入時は上流リポジトリから直接取得する（`bin/skillhub` の install 動作）。

最終確認: 2026-11-27（GitHub API の SPDX 判定＋ LICENSE 文面の実測）

| リポジトリ | スキル数 | 分類 | 上流ライセンス | 備考 |
|---|---:|---|---|---|
| [abiosoft/colima](https://github.com/abiosoft/colima) | 1 | dedicated | MIT |  |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 25 | product-internal | MIT |  |
| [ansible/ansible](https://github.com/ansible/ansible) | 4 | product-internal | GPL-3.0 | COPYING 実測で確定 |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 2 | dedicated | MIT |  |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 10 | product-internal | MIT（一部除く） | enterprise/ 配下は別ライセンス（LICENSE 実測） |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 1 | dedicated | MIT |  |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 1 | dedicated | MIT |  |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 13 | dedicated | MIT |  |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 8 | dedicated | MIT |  |
| [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | 39 | product-internal | MIT |  |
| [enesozturk/dimensional-drawing](https://github.com/enesozturk/dimensional-drawing) | 2 | dedicated | MIT |  |
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | 1 | dedicated | MIT |  |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 5 | product-internal | AGPL-3.0 |  |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 1 | product-internal | MIT |  |
| [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | 4 | product-internal | Apache-2.0 |  |
| [grafana/grafana](https://github.com/grafana/grafana) | 3 | product-internal | AGPL-3.0 | LICENSE 文面で確認 |
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | 2 | dedicated | MIT |  |
| [heydamir/unslop](https://github.com/heydamir/unslop) | 1 | dedicated | CC-BY-4.0 |  |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 39 | dedicated | MIT |  |
| [meta/astryx](https://github.com/meta/astryx) | 1 | product-internal | MIT |  |
| [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | 11 | product-internal | MIT |  |
| [microsoft/inshellisense](https://github.com/microsoft/inshellisense) | 1 | product-internal | MIT |  |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 4 | product-internal | Apache-2.0 |  |
| [morluto/rea](https://github.com/morluto/rea) | 6 | product-internal | MIT |  |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 1 | dedicated | MIT |  |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 46 | product-internal | Sustainable Use License（独自） | .ee. ファイル等は対象外（LICENSE.md 実測） |
| [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) | 1 | dedicated | MIT |  |
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | 1 | dedicated | MIT |  |
| [nodejs/node](https://github.com/nodejs/node) | 33 | product-internal | Node.js License（独自・MIT系） | LICENSE 実測 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 186 | agent-bundled | MIT |  |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 34 | dedicated | Apache-2.0 |  |
| [obra/superpowers](https://github.com/obra/superpowers) | 15 | dedicated | MIT |  |
| [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills) | 7 | dedicated | MIT |  |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | 1 | product-internal | BSD-3-Clause | LICENSE 文面で確認 |
| [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 1 | product-internal | Apache-2.0 |  |
| [react/react](https://github.com/react/react) | 14 | product-internal | MIT |  |
| [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | 1 | product-internal | Apache-2.0 |  |
| [steipete/CodexBar](https://github.com/steipete/CodexBar) | 3 | product-internal | MIT |  |
| [supabase/supabase](https://github.com/supabase/supabase) | 25 | product-internal | Apache-2.0 |  |
| [taisukey/chat-map](https://github.com/taisukey/chat-map) | 1 | dedicated | MIT |  |
| [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | 27 | product-internal | Apache-2.0 |  |
| [tw93/Mole](https://github.com/tw93/Mole) | 6 | product-internal | GPL-3.0 |  |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 12 | product-internal | Apache-2.0 |  |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 8 | product-internal | Apache-2.0 |  |
| [vercel-labs/ui](https://github.com/vercel-labs/ui) | 5 | product-internal | Apache-2.0 |  |
| [vercel/next.js](https://github.com/vercel/next.js) | 30 | product-internal | MIT |  |
| [virattt/dexter](https://github.com/virattt/dexter) | 3 | product-internal | ライセンスなし | GitHub API で検出なし |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 1 | dedicated | MIT |  |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 1 | dedicated | MIT |  |
| [xykong/flux-markdown](https://github.com/xykong/flux-markdown) | 2 | product-internal | GPL-3.0 | LICENSE 文面で Version 3 を確認 |

## 要注意（自動チェックの監視対象）

- ライセンスなし: virattt/dexter — 再配布条件が存在しない。カタログのメタデータ参照のみとし、扱いは慎重に。
- コピーレフト系: ansible/ansible・firecrawl/firecrawl・grafana/grafana・tw93/Mole・xykong/flux-markdown（GPL/AGPL）— 導入先で使う場合は各条件を確認。
- 独自・複合: BerriAI/litellm（一部 enterprise 別ライセンス）、n8n-io/n8n（Sustainable Use License）、nodejs/node（Node.js License）— 標準 SPDX と異なるため個別確認。
