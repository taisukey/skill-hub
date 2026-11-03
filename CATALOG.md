# CATALOG — Starred Agent Skills

GitHub Starred から SKILL.md を含むリポジトリだけを抽出し、分類したカタログ。
生成: build_catalog.py / 元データ: catalog.json

## 専用スキル集（導入候補）（19 repos）

### [obra/superpowers](https://github.com/obra/superpowers) — 15 skills ★311667
> 開発方法論のスキル集
An agentic skills framework & software development methodology that works.
- **brainstorming** (`skills/brainstorming`) — You MUST use this before any creative work - creating features, building components, adding function
- **diagnosing-superpowers** (`skills/diagnosing-superpowers`) — Use when a superpowers session went wrong and your human partner wants to know why — repeated work, 
- **dispatching-parallel-agents** (`skills/dispatching-parallel-agents`) — Use when facing 2+ independent tasks that can be worked on without shared state or sequential depend
- **executing-plans** (`skills/executing-plans`) — Use when executing an implementation plan in the current session as the implementer yourself — your 
- **finishing-a-development-branch** (`skills/finishing-a-development-branch`) — Use when implementation is complete, all tests pass, and you need to decide how to integrate the wor
- **receiving-code-review** (`skills/receiving-code-review`) — Use when receiving code review feedback, before implementing suggestions, especially if feedback see
- **requesting-code-review** (`skills/requesting-code-review`) — Use when completing tasks, implementing major features, or before merging to verify work meets requi
- **subagent-driven-development** (`skills/subagent-driven-development`) — Use when executing implementation plans with independent tasks in the current session
- **systematic-debugging** (`skills/systematic-debugging`) — Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
- **test-driven-development** (`skills/test-driven-development`) — Use when implementing any feature or bugfix, before writing implementation code
- **using-git-worktrees** (`skills/using-git-worktrees`) — Use when starting feature work that needs isolation from current workspace or before executing imple
- **using-superpowers** (`skills/using-superpowers`) — Use when starting any conversation - establishes how to find and use skills, requiring skill invocat
- **verification-before-completion** (`skills/verification-before-completion`) — Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - req
- **writing-plans** (`skills/writing-plans`) — Use when you have a spec or requirements for a multi-step task, before touching code
- **writing-skills** (`skills/writing-skills`) — Use when creating new skills, editing existing skills, or verifying skills work before deployment

### [mattpocock/skills](https://github.com/mattpocock/skills) — 39 skills ★311032
> 実務エンジニアリングのスキル集
Skills for Real Engineers. Straight from my .agents directory.
- **ask-matt** (`skills/engineering/ask-matt`) — Ask which skill or flow fits your situation. A router over the skills in this repo.
- **code-review** (`skills/engineering/code-review`) — Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standard
- **codebase-design** (`skills/engineering/codebase-design`) — Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module'
- **diagnosing-bugs** (`skills/engineering/diagnosing-bugs`) — Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug t
- **domain-modeling** (`skills/engineering/domain-modeling`) — Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or edi
- **grill-with-docs** (`skills/engineering/grill-with-docs`) — A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as 
- **implement-spec** (`skills/engineering/implement-spec`) — Implement the result of /to-spec and /to-tickets in code.
- **implement** (`skills/engineering/implement`) — Implement a piece of work based on a spec or set of tickets.
- **improve-codebase-architecture** (`skills/engineering/improve-codebase-architecture`) — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill throug
- **pr** (`skills/engineering/pr`) — Use when writing a PR body.
- **prototype** (`skills/engineering/prototype`) — Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whe
- **research** (`skills/engineering/research`) — Investigate a question against high-trust primary sources and capture the findings as a Markdown fil
- **retro** (`skills/engineering/retro`) — Conduct a retrospective on a coding session.
- **setup-matt-pocock-skills** (`skills/engineering/setup-matt-pocock-skills`) — Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, a
- **tdd** (`skills/engineering/tdd`) — Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions 
- **to-spec** (`skills/engineering/to-spec`) — Turn the current conversation into a spec and publish it to the project issue tracker: no interview,
- **to-tickets** (`skills/engineering/to-tickets`) — Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring 
- **triage** (`skills/engineering/triage`) — Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if n
- **wayfinder** (`skills/engineering/wayfinder`) — Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets
- **wizard** (`skills/engineering/wizard`) — Generate an interactive bash wizard that walks a human through steps only they can perform. Use when
- **chief-of-staff** (`skills/in-progress/chief-of-staff`) — Pursue a long-running goal in a single session by co-ordinating subagents.
- **claude-handoff** (`skills/in-progress/claude-handoff`) — Hand the current conversation off to a fresh background agent that picks up the work immediately.
- **loop-me** (`skills/in-progress/loop-me`) — Grill me about specs for the workflows I want to build, within this workspace.
- **setup-ts-deep-modules** (`skills/in-progress/setup-ts-deep-modules`) — Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation
- **software-factory** (`skills/in-progress/software-factory`) — Shared language for designing a software factory: the tasks it runs and the services it plugs into.
- **writing-beats** (`skills/in-progress/writing-beats`) — Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat l
- **writing-fragments** (`skills/in-progress/writing-fragments`) — Writing, explore: mine raw fragments, no structure yet.
- **writing-shape** (`skills/in-progress/writing-shape`) — Writing, exploit: shape raw material into an article, paragraph by paragraph.
- **git-guardrails-claude-code** (`skills/misc/git-guardrails-claude-code`) — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.
- **migrate-to-shoehorn** (`skills/misc/migrate-to-shoehorn`) — Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions s
- **scaffold-exercises** (`skills/misc/scaffold-exercises`) — Create exercise directory structures with sections, problems, solutions, and explainers that pass li
- **setup-pre-commit** (`skills/misc/setup-pre-commit`) — Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current r
- **grill-me** (`skills/productivity/grill-me`) — A relentless interview to sharpen a plan or design.
- **grilling** (`skills/productivity/grilling`) — Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test 
- **handoff** (`skills/productivity/handoff`) — Compact the current conversation into a handoff document for another agent to pick up.
- **teach** (`skills/productivity/teach`) — Teach the user a new skill or concept, within this workspace.
- **to-questionnaire** (`skills/productivity/to-questionnaire`) — Turn a decision you can't fully answer into a questionnaire for someone else to fill in.
- **wait-what** (`skills/productivity/wait-what`) — Stop. That last message did not land: re-pitch it.
- **writing-for-agents** (`skills/productivity/writing-for-agents`) — Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.

### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — 13 skills ★183463
> 最小実装を促す行動スキル集
Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **ponytail-audit** (`.openclaw/skills/ponytail-audit`) — Quality audit of the whole repo: bugs, security, real load, missing tests, speed, and what to delete
- **ponytail-debt** (`.openclaw/skills/ponytail-debt`) — Harvest every shortcut: comment into one debt ledger, so deferrals get tracked instead of forgotten.
- **ponytail-gain** (`.openclaw/skills/ponytail-gain`) — Show ponytail measured impact as a scoreboard: less code, less cost, more speed, from the agentic be
- **ponytail-help** (`.openclaw/skills/ponytail-help`) — Quick reference for ponytail's modes, skills, and commands. One-shot display.
- **ponytail-review** (`.openclaw/skills/ponytail-review`) — Quality review of a diff: bugs, security, real load, missing tests, speed, and what to delete. Each 
- **ponytail** (`.openclaw/skills/ponytail`) — Lazy senior dev mode for any coding task: the smallest change that fully solves it, and a reply a bu
- **caveman** (`.`) — >
- **ponytail-audit** (`skills/ponytail-audit`) — >
- **ponytail-debt** (`skills/ponytail-debt`) — >
- **ponytail-gain** (`skills/ponytail-gain`) — >
- **ponytail-help** (`skills/ponytail-help`) — >
- **ponytail-review** (`skills/ponytail-review`) — >
- **ponytail** (`skills/ponytail`) — >

### [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — 1 skills ★66446
> 直近30日の話題リサーチ
AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary
- **last30days** (`skills/last30days`) — Research what people actually say about any topic in the last 30 days. Pulls posts and engagement fr

### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — 1 skills ★64581
> 図解デザイン
Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 45 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop.
- **diagram-design** (`skills/diagram-design`) — Create branded architecture, architecture delta, IT current-state, flowchart, sequence, state machin

### [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) — 2 skills ★59908
> ADHD 配慮の出力スキル
A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **i-have-adhd** (`.cursor/skills/i-have-adhd`) — Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate stat
- **i-have-adhd** (`skills/i-have-adhd`) — Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate stat

### [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — 6 skills ★50685
> Obsidian 用スキル集
Agent skills for Obsidian. Teach your agent to use Obsidian CLI and open formats including Markdown, Bases, JSON Canvas.
- **defuddle** (`skills/defuddle`) — Extract clean Markdown from HTML pages with Defuddle CLI.
- **json-canvas** (`skills/json-canvas`) — Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when wor
- **knap** (`skills/knap`) — Render Markdown from templates and structured data using Knap CLI. Use when the user asks to apply a
- **obsidian-bases** (`skills/obsidian-bases`) — Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when 
- **obsidian-cli** (`skills/obsidian-cli`) — Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, task
- **obsidian-markdown** (`skills/obsidian-markdown`) — Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other O

### [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) — 1 skills ★38608
> LLM のハード適合アドバイザ
Hundreds of models & providers. One command to find what runs on your hardware.
- **llmfit-advisor** (`skills/llmfit-advisor`) — Detect local hardware (RAM, CPU, GPU/VRAM) and recommend the best-fit local LLM models with optimal 

### [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) — 1 skills ★36850
> 書籍 PDF をスキル化
Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work.
- **book-to-skill** (`.`) — Converts books and documents (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF, MOBI/AZW with Calibr

### [abiosoft/colima](https://github.com/abiosoft/colima) — 1 skills ★31508
> colima 利用スキル（M1 で利用中）
Container runtimes on macOS (and Linux) with minimal setup
- **colima** (`skills`) — >-

### [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) — 2 skills ★26095
> 透かし除去・文面クリーニング
A privacy-first app that strips AI watermarks from content you own.
- **clean-user-facing-text** (`skills/clean-user-facing-text`) — Clean and finalize authorized natural-language text intended for readers by auditing suspicious invi
- **remove-ai-marks** (`skills/remove-ai-marks`) — >

### [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) — 12 skills ★25164
> CAD / 3D プリント系スキル集
Design physical products with AI
- **bambu-labs** (`skills/bambu-labs`) — Send prints to Bambu Lab printers through Bambu Connect, Bambu Lab's official app for printing from 
- **cad** (`skills/cad`) — Creates and edits parametric CAD parts and assemblies as Python build123d models that text-to-cad's 
- **dfam-check** (`skills/dfam-check`) — Measure mesh files against Design for Additive Manufacturing (DfAM) rules and report printability fi
- **dfm** (`skills/dfm`) — Design-for-manufacturing review of a part for sheet metal, CNC machining, or injection molding - ben
- **dxf** (`skills/dxf`) — Generates, regenerates and validates 2D DXF drawings from Python build123d models, exported by text-
- **engineering-drawing** (`skills/engineering-drawing`) — Make an engineering drawing of a part as a PDF - orthographic views with hidden lines and centre mar
- **gcode** (`skills/gcode`) — Slice 3D models into printer-ready G-code with OrcaSlicer, the open-source slicer with built-in prof
- **sdf** (`skills/sdf`) — SDFormat/SDF model and world authoring, validation, and simulator handoff. Use for `.sdf` files, SDF
- **sendcutsend** (`skills/sendcutsend`) — Review DXF and STEP/STP uploads for SendCutSend.com orders using its ordering guide, catalog, and sp
- **srdf** (`skills/srdf`) — MoveIt2 SRDF authoring, validation, and planning-semantics workflow. Use when creating, editing, ins
- **step-parts** (`skills/step-parts`) — >-
- **urdf** (`skills/urdf`) — URDF robot description authoring and validation. Use when creating, editing, inspecting, validating,

### [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) — 1 skills ★24347
> 等角分解イラスト（Hermes 導入済み）
An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems. Generates polished SVGs with optional WebGL shaders and 3D effects.
- **anatomy** (`.`) — Build crafted, highly detailed, interactive isometric SVG figures that explain a technical idea as a

### [firecrawl/anydoc](https://github.com/firecrawl/anydoc) — 1 skills ★23330
> 文書→Markdown 変換
Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean Markdown. Built in Rust, with Node.js and Python bindings.
- **convert-documents-to-markdown** (`skills/convert-documents-to-markdown`) — Convert Word (.doc, .docx), PowerPoint (.ppt, .pptx), Excel (.xls, .xlsx), OpenDocument (.odt, .ods,

### [heydamir/unslop](https://github.com/heydamir/unslop) — 1 skills ★7121
> UI の AI っぽさを取るスキル（導入済み）
A Claude skill that turns vibecoded, AI-looking UI into a designed interface
- **unslop** (`skills/unslop`) — Turns vibecoded, AI-looking UI into a designed interface with its own character. Finds a direction f

### [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) — 14 skills ★4435
Local video editor for coding agents: 42 FFmpeg tools with a machine-readable contract and an MCP server, for Claude Code, Cursor and Codex. Cut, captions, reframe, loudness, platform exports. No cloud, no API keys.
- **shipping-build-artifacts** (`.claude/skills/build-artifacts`) — Make the build step a real gate on what you actually distribute — build scripts that warn and exit 0
- **ci-pipeline-synthesizer** (`.claude/skills/ci-pipeline-synthesizer`) — Generate GitHub Actions CI/CD pipeline configurations for automated building and testing of library 
- **reviewing-ffmpeg-skill-changes** (`.claude/skills/code-review`) — Review a change to the ffmpeg-skill repository for the failures its own contract makes possible — a 
- **concurrent-branches** (`.claude/skills/concurrent-branches`) — Resolve conflicts and merges when several branches are open against one repo at the same time — the 
- **shipping-across-surfaces** (`.claude/skills/cross-surface-changes`) — Land a change everywhere the same fact is stated — enumerating the full surface inventory (landing c
- **writing-defect-reports** (`.claude/skills/defect-reports`) — Establish a finding before you publish it, and correct it after — headlines that overstate what actu
- **guarding-destructive-operations** (`.claude/skills/destructive-operations`) — Add and review preconditions on operations that delete, overwrite, rewrite history, or resolve a cal
- **keeping-git-repos-clean** (`.claude/skills/git-hygiene`) — Prevents, detects, and remediates files that should never be committed — secrets (.env, API tokens, 
- **running-github-actions-efficiently** (`.claude/skills/github-actions`) — Cut GitHub Actions minutes and wall-clock time without losing coverage — the OS billing multiplier (
- **building-python-mcp-servers** (`.claude/skills/mcp-server-design`) — Builds robust Python MCP (Model Context Protocol) servers with FastMCP — tool design, error contract
- **managing-python-releases** (`.claude/skills/release-management`) — Manages Python library releases including semantic versioning, changelog maintenance (Keep a Changel
- **reproducing-ci-locally** (`.claude/skills/reproducing-ci-locally`) — Run the CI gate on your machine so it agrees with the runner — deriving the exact command, paths, ma
- **verifying-external-behavior** (`.claude/skills/verifying-external-behavior`) — Confirms what a third-party library, remote API, build backend, or scraped document actually does be
- **ffmpeg-skill** (`.`) — Edit video and audio with local FFmpeg: cut, join, reframe, speed, captions, overlays, silence remov

### [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) — 1 skills ★2828
> 日本語推敲スキル
AI生成の日本語を自然な日本語へ推敲するAgent Skill / Agent Skill for Refining AI-Generated Japanese into Natural Japanese
- **yomiyasu** (`skills/yomiyasu`) — AIが生成した日本語を推敲するスキル。利用者が yomiyasu の名前を出して頼んだとき（「/yomiyasu」、「$yomiyasu:yomiyasu」、「yomiyasu で推敲して」など）と、

### [enesozturk/dimensional-drawing](https://github.com/enesozturk/dimensional-drawing) — 2 skills ★1763
> 寸法図スキル（導入済み）
Create Apple style dimensional drawings of UI components.
- **dimensional-drawing-motion** (`skills/dimensional-drawing-motion`) — Turn a finished dimensional drawing sheet into a ~10 s Apple-style motion film — lines draw themselv
- **dimensional-drawing** (`skills/dimensional-drawing`) — Make an Apple-style monochrome dimensional drawing of a UI component or physical product — title-blo

### [taisukey/chat-map](https://github.com/taisukey/chat-map) — 1 skills ★1
Agent skill: map your chat threads (main + side chats) as a graph x historic timeline — branches, handovers, recurring deliveries
- **chat-map** (`.`) — Draw the user's conversation landscape as one map — every chat thread as a node, branch / handover /

## エージェント同梱（1 repos）

### [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — 194 skills ★260130
> Hermes 本体のスキルライブラリ（optional-skills が追加プール）
The agent that grows with you
- **agent-merge-conflict-arbiter** (`optional-skills/autonomous-ai-agents/agent-merge-conflict-arbiter`) — Neutral arbiter for merge conflicts between two agents.
- **antigravity-cli** (`optional-skills/autonomous-ai-agents/antigravity-cli`) — Operate the Antigravity CLI (agy): plugins, auth, sandbox.
- **blackbox** (`optional-skills/autonomous-ai-agents/blackbox`) — Delegate coding tasks to the Blackbox AI multi-model CLI.
- **dynamic-workflow** (`optional-skills/autonomous-ai-agents/dynamic-workflow`) — Plan-in-code fan-outs, adversarial verification, waves.
- **grok** (`optional-skills/autonomous-ai-agents/grok`) — Delegate coding to xAI Grok Build CLI (features, PRs).
- **honcho** (`optional-skills/autonomous-ai-agents/honcho`) — Configure and troubleshoot Honcho memory for Hermes.
- **opencode** (`optional-skills/autonomous-ai-agents/opencode`) — Delegate coding to OpenCode CLI (features, PR review).
- **openhands** (`optional-skills/autonomous-ai-agents/openhands`) — Delegate coding to OpenHands CLI (model-agnostic, LiteLLM).
- **evm** (`optional-skills/blockchain/evm`) — Read-only EVM client: wallets, tokens, gas across 8 chains.
- **hyperliquid** (`optional-skills/blockchain/hyperliquid`) — Hyperliquid market data, account history, trade review.
- **solana** (`optional-skills/blockchain/solana`) — Query Solana wallets, tokens, txs, and NFTs in USD.
- **one-three-one-rule** (`optional-skills/communication/one-three-one-rule`) — 1-3-1 decision briefs: problem, three options, one pick.
- **ai-presenter-video** (`optional-skills/creative/ai-presenter-video`) — Make a verified AI presenter video from script + image.
- **anatomy** (`optional-skills/creative/anatomy`) — Explain an idea as an interactive isometric machine figure.
- **archify** (`optional-skills/creative/archify`) — Validated interactive HTML diagrams, upstream-maintained.
- **ascii-art** (`optional-skills/creative/ascii-art`) — ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.
- **auteur** (`optional-skills/creative/auteur`) — Design and build cinematic, award-level web pages.
- **baoyu-article-illustrator** (`optional-skills/creative/baoyu-article-illustrator`) — Article illustrations: type × style × palette consistency.
- **baoyu-comic** (`optional-skills/creative/baoyu-comic`) — Knowledge comics (知识漫画): educational, biography, tutorial.
- **brag-slim** (`optional-skills/creative/brag-slim`) — Launch video from a project or URL, upstream-maintained.
- **brag** (`optional-skills/creative/brag`) — Project launch video via Hyperframes, upstream-maintained.
- **comfyui** (`optional-skills/creative/comfyui`) — Generate images, video, and audio via diffusion workflows.
- **concept-diagrams** (`optional-skills/creative/concept-diagrams`) — Generate flat, minimal educational SVG visuals as HTML.
- **creative-ideation** (`optional-skills/creative/creative-ideation`) — Generate ideas via named methods from creative practice.
- **design-md** (`optional-skills/creative/design-md`) — Author/validate/export Google's DESIGN.md token spec files.
- **draw-your-font** (`optional-skills/creative/draw-your-font`) — Turn a handwriting photo into an installable TTF font.
- **dream-loop** (`optional-skills/creative/dream-loop`) — Build stunning 3D scenes via a concept-art fidelity loop.
- **excalidraw** (`optional-skills/creative/excalidraw`) — Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).
- **heartmula** (`optional-skills/creative/heartmula`) — HeartMuLa: Suno-like song generation from lyrics + tags.
- **hyperframes** (`optional-skills/creative/hyperframes`) — Render MP4/WebM videos from HTML compositions.
- **impeccable** (`optional-skills/creative/impeccable`) — Frontend design guidance, upstream-maintained (impeccable).
- **ip-as-logo** (`optional-skills/creative/ip-as-logo`) — Design minimal cute IP mascot marks readable at 32px.
- **kanban-video-orchestrator** (`optional-skills/creative/kanban-video-orchestrator`) — Plan and run multi-agent video production pipelines.
- **meme-generation** (`optional-skills/creative/meme-generation`) — Create meme PNGs from templates with Pillow text overlay.
- **mono-color** (`optional-skills/creative/mono-color`) — Generate one- or two-ink editorial print poster images.
- **pixel-art** (`optional-skills/creative/pixel-art`) — Pixel art w/ era palettes (NES, Game Boy, PICO-8).
- **pretext** (`optional-skills/creative/pretext`) — Build creative browser demos with DOM-free text layout.
- **simple-english** (`optional-skills/creative/simple-english`) — Rewrite text to ASD-STE100 Simplified Technical English.
- **sketch** (`optional-skills/creative/sketch`) — Throwaway HTML mockups: 2-3 design variants to compare.
- **social-media-content-calendar** (`optional-skills/creative/social-media-content-calendar`) — Plan multi-platform social campaigns: briefs to posting.
- **system-atlas** (`optional-skills/creative/system-atlas`) — Build explorable isometric architecture atlases as HTML.
- **tldraw-offline** (`optional-skills/creative/tldraw-offline`) — Drive and script tldraw offline canvases with an agent.
- **unreal-mcp** (`optional-skills/creative/unreal-mcp`) — Automate Unreal Engine editor scenes, actors, and renders.
- **jupyter-notebook** (`optional-skills/data-science/jupyter-notebook`) — Iterative Python via live Jupyter kernel (hamelnb).
- **actual-setup** (`optional-skills/devops/actual-setup`) — Set up Actual Computer (actual.inc) inference in Hermes.
- **docker-management** (`optional-skills/devops/docker-management`) — Manage Docker containers, images, volumes, and Compose.
- **hermes-s6-container-supervision** (`optional-skills/devops/hermes-s6-container-supervision`) — Modify or debug s6 services in the Hermes Docker image.
- **inference-sh-cli** (`optional-skills/devops/inference-sh-cli`) — Run 150+ AI apps (image, video, LLM) via inference.sh CLI.
- **pinggy-tunnel** (`optional-skills/devops/pinggy-tunnel`) — Zero-install localhost tunnels over SSH via Pinggy.
- **setup-wizard-generator** (`optional-skills/devops/setup-wizard-generator`) — Generate a bash wizard guiding a human through manual setup.
- **watchers** (`optional-skills/devops/watchers`) — Poll RSS, JSON APIs, and GitHub with watermark dedup.
- **adversarial-ux-test** (`optional-skills/dogfood/adversarial-ux-test`) — Roleplay a hostile user to find and triage UX pain points.
- **agentmail** (`optional-skills/email/agentmail`) — Use when an agent needs AgentMail CLI email inboxes.
- **3-statement-model** (`optional-skills/finance/3-statement-model`) — Build integrated IS/BS/CF financial workbooks in Excel.
- **comps-analysis** (`optional-skills/finance/comps-analysis`) — Build comparable-company valuation workbooks in Excel.
- **dcf-model** (`optional-skills/finance/dcf-model`) — Build discounted cash flow valuation workbooks in Excel.
- **excel-author** (`optional-skills/finance/excel-author`) — Build auditable financial workbooks headless via openpyxl.
- **lbo-model** (`optional-skills/finance/lbo-model`) — Build leveraged buyout workbooks with IRR/MOIC in Excel.
- **merger-model** (`optional-skills/finance/merger-model`) — Build M&A accretion/dilution workbooks in Excel.
- **polymarket** (`optional-skills/finance/polymarket`) — Query Polymarket: markets, prices, orderbooks, history.
- **pptx-author** (`optional-skills/finance/pptx-author`) — Build PowerPoint decks headless with python-pptx.
- **stocks** (`optional-skills/finance/stocks`) — Stock quotes, history, search, compare, crypto via Yahoo.
- **minecraft-modpack-server** (`optional-skills/gaming/minecraft-modpack-server`) — Host modded Minecraft servers (CurseForge, Modrinth).
- **pokemon-player** (`optional-skills/gaming/pokemon-player`) — Play Pokemon via headless emulator + RAM reads.
- **fitness-nutrition** (`optional-skills/health/fitness-nutrition`) — Workout planning, macros, and body metrics via wger/USDA.
- **neuroskill-bci** (`optional-skills/health/neuroskill-bci`) — Use live BCI cognitive and mood state from NeuroSkill.
- **fastmcp** (`optional-skills/mcp/fastmcp`) — Build, test, and deploy Python MCP servers.
- **mcp-oauth-remote-gateway** (`optional-skills/mcp/mcp-oauth-remote-gateway`) — Manual OAuth for remote MCP servers on headless gateways.
- **mcporter** (`optional-skills/mcp/mcporter`) — List, auth, and call MCP servers/tools from the terminal.
- **gif-search** (`optional-skills/media/gif-search`) — Search/download GIFs from Tenor via curl + jq.
- **songsee** (`optional-skills/media/songsee`) — Audio spectrograms/features (mel, chroma, MFCC) via CLI.
- **accelerate** (`optional-skills/mlops/accelerate`) — Run PyTorch training across GPUs with minimal changes.
- **chroma** (`optional-skills/mlops/chroma`) — Embedding database for RAG and semantic search.
- **evaluating-llms-harness** (`optional-skills/mlops/evaluation/evaluating-llms-harness`) — lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).
- **faiss** (`optional-skills/mlops/faiss`) — Fast vector similarity search at billion scale.
- **flash-attention** (`optional-skills/mlops/flash-attention`) — Speed up long-sequence transformer training and inference.
- **llama-cpp** (`optional-skills/mlops/inference/llama-cpp`) — llama.cpp local GGUF inference + HF Hub model discovery.
- **serving-llms-vllm** (`optional-skills/mlops/inference/serving-llms-vllm`) — vLLM: high-throughput LLM serving, OpenAI API, quantization.
- **lambda-labs** (`optional-skills/mlops/lambda-labs`) — On-demand GPU cloud instances for ML training.
- **modal** (`optional-skills/mlops/modal`) — Serverless GPU cloud for ML jobs and model APIs.
- **segment-anything-model** (`optional-skills/mlops/models/segment-anything-model`) — SAM: zero-shot image segmentation via points, boxes, masks.
- **nemo-curator** (`optional-skills/mlops/nemo-curator`) — Curate LLM training data: dedupe, filter, PII redaction.
- **obliteratus** (`optional-skills/mlops/obliteratus`) — OBLITERATUS: abliterate LLM refusals (diff-in-means).
- **peft** (`optional-skills/mlops/peft`) — Fine-tune large LLMs with LoRA on limited GPU memory.
- **pytorch-fsdp** (`optional-skills/mlops/pytorch-fsdp`) — Fully sharded data-parallel training for large models.
- **pytorch-lightning** (`optional-skills/mlops/pytorch-lightning`) — Clean training loops with built-in distributed support.
- **dspy** (`optional-skills/mlops/research/dspy`) — DSPy: declarative LM programs, auto-optimize prompts, RAG.
- **saelens** (`optional-skills/mlops/saelens`) — Train sparse autoencoders to interpret model features.
- **simpo** (`optional-skills/mlops/simpo`) — Reference-free preference alignment, simpler than DPO.
- **slime** (`optional-skills/mlops/slime`) — RL post-training for LLMs with Megatron and SGLang.
- **tensorrt-llm** (`optional-skills/mlops/tensorrt-llm`) — High-throughput LLM inference on NVIDIA GPUs.
- **torchtitan** (`optional-skills/mlops/torchtitan`) — Pretrain LLMs at scale with PyTorch 4D parallelism.
- **axolotl** (`optional-skills/mlops/training/axolotl`) — Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO).
- **unsloth** (`optional-skills/mlops/training/unsloth`) — Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM.
- **mpp-agent** (`optional-skills/payments/mpp-agent`) — Pay HTTP 402 APIs via Machine Payments Protocol (MPP).
- **stripe-link-cli** (`optional-skills/payments/stripe-link-cli`) — Agent payments via Stripe Link — cards, SPT, approvals.
- **stripe-projects** (`optional-skills/payments/stripe-projects`) — Provision SaaS services + sync creds via Stripe Projects.
- **airtable** (`optional-skills/productivity/airtable`) — Airtable REST API via curl. Records CRUD, filters, upserts.
- **box** (`optional-skills/productivity/box`) — Box manages cloud files, sharing, search, and metadata.
- **canvas** (`optional-skills/productivity/canvas`) — Fetch Canvas LMS courses and assignments via API token.
- **decision-questionnaire** (`optional-skills/productivity/decision-questionnaire`) — Turn an unanswerable decision into a questionnaire doc.
- **here-now** (`optional-skills/productivity/here-now`) — Publish sites to {slug}.here.now and store files in Drives.
- **live-dashboard** (`optional-skills/productivity/live-dashboard`) — Build self-updating dashboards from live sources.
- **memento-flashcards** (`optional-skills/productivity/memento-flashcards`) — Spaced-repetition flashcards: create, review, quiz, export.
- **notion** (`optional-skills/productivity/notion`) — Notion API + ntn CLI: pages, databases, markdown, Workers.
- **property-listings** (`optional-skills/productivity/property-listings`) — Present property and rental listings as desktop cards.
- **shop** (`optional-skills/productivity/shop`) — Shop catalog search, checkout, order tracking, returns.
- **shopify** (`optional-skills/productivity/shopify`) — Query Shopify Admin/Storefront GraphQL APIs via curl.
- **siyuan** (`optional-skills/productivity/siyuan`) — Query and edit a SiYuan knowledge base via its API.
- **telephony** (`optional-skills/productivity/telephony`) — Provision Twilio numbers, SMS/MMS, and AI outbound calls.
- **bioinformatics** (`optional-skills/research/bioinformatics`) — Gateway to 400+ genomics and computational biology skills.
- **blogwatcher** (`optional-skills/research/blogwatcher`) — Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.
- **darwinian-evolver** (`optional-skills/research/darwinian-evolver`) — Evolve prompts/regex/SQL/code with Imbue's evolution loop.
- **domain-intel** (`optional-skills/research/domain-intel`) — Passive recon of subdomains, SSL certs, WHOIS, and DNS.
- **drug-discovery** (`optional-skills/research/drug-discovery`) — Drug discovery: ChEMBL search, drug-likeness, interactions.
- **duckduckgo-search** (`optional-skills/research/duckduckgo-search`) — Free keyless web, news, and image search via ddgs.
- **gitnexus-explorer** (`optional-skills/research/gitnexus-explorer`) — Serve an interactive codebase knowledge graph web UI.
- **llm-wiki** (`optional-skills/research/llm-wiki`) — Karpathy's LLM Wiki: build/query interlinked markdown KB.
- **osint-investigation** (`optional-skills/research/osint-investigation`) — Follow the money via public records and sanctions data.
- **parallel-cli** (`optional-skills/research/parallel-cli`) — Agent-native web search, deep research, and enrichment.
- **qmd** (`optional-skills/research/qmd`) — Hybrid local search over notes, docs, and transcripts.
- **research-paper-writing** (`optional-skills/research/research-paper-writing`) — Write ML papers for NeurIPS/ICML/ICLR: design→submit.
- **rss-feeds** (`optional-skills/research/rss-feeds`) — Read RSS, Atom, JSON feeds; discover feeds behind a page.
- **scrapling** (`optional-skills/research/scrapling`) — Scrape sites with stealth browsing and Cloudflare bypass.
- **searxng-search** (`optional-skills/research/searxng-search`) — Free keyless meta-search aggregating 70+ engines.
- **1password** (`optional-skills/security/1password`) — Set up op CLI, sign in, and read or inject secrets.
- **godmode** (`optional-skills/security/godmode`) — Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.
- **oss-forensics** (`optional-skills/security/oss-forensics`) — GitHub supply-chain forensics: recovery, IOCs, reporting.
- **sherlock** (`optional-skills/security/sherlock`) — Find accounts for a username across 400+ platforms.
- **unbroker** (`optional-skills/security/unbroker`) — Remove your info from data-broker sites, by name or phone.
- **web-pentest** (`optional-skills/security/web-pentest`) — Authorized web pentest: recon, proof-based exploits, report.
- **openhue** (`optional-skills/smart-home/openhue`) — Control Philips Hue lights, scenes, rooms via OpenHue CLI.
- **reddit-reading** (`optional-skills/social-media/reddit-reading`) — Read Reddit: subreddits, search, threads, users. No browser.
- **ast-grep** (`optional-skills/software-development/ast-grep`) — AST-aware structural code search and rewrite via ast-grep.
- **code-wiki** (`optional-skills/software-development/code-wiki`) — Generate wiki docs + Mermaid diagrams for any codebase.
- **grill-me** (`optional-skills/software-development/grill-me`) — Adversarial plan interview before implementation.
- **hermes-agent-skill-authoring** (`optional-skills/software-development/hermes-agent-skill-authoring`) — Author in-repo SKILL.md files: frontmatter and structure.
- **inspecting-hermes-desktop-dom** (`optional-skills/software-development/inspecting-hermes-desktop-dom`) — Read the live Hermes desktop DOM/CSS over CDP.
- **node-inspect-debugger** (`optional-skills/software-development/node-inspect-debugger`) — Debug Node.js via --inspect + Chrome DevTools Protocol CLI.
- **pr-lens** (`optional-skills/software-development/pr-lens`) — Draw code changes as animated architecture/data-flow SVGs.
- **python-debugpy** (`optional-skills/software-development/python-debugpy`) — Debug Python: pdb REPL + debugpy remote (DAP).
- **rest-graphql-debug** (`optional-skills/software-development/rest-graphql-debug`) — Debug REST/GraphQL APIs: status codes, auth, schemas, repro.
- **subagent-driven-development** (`optional-skills/software-development/subagent-driven-development`) — Execute plans via delegate_task subagents (2-stage review).
- **cloudflare-temporary-deploy** (`optional-skills/web-development/cloudflare-temporary-deploy`) — Deploy a Worker live, no account, via wrangler --temporary.
- **har-derived-api-client** (`optional-skills/web-development/har-derived-api-client`) — Record a site's XHR into a HAR, derive an HTTP client.
- **page-agent** (`optional-skills/web-development/page-agent`) — Embed an in-page natural-language GUI copilot in web apps.
- **publish-site** (`optional-skills/web-development/publish-site`) — Versioned site deploys to GitHub/Cloudflare/Netlify Pages.
- **scrollcraft** (`optional-skills/web-development/scrollcraft`) — Premium scroll-driven landing pages; scroll = timeline.
- **yuanbao** (`optional-skills/yuanbao`) — Yuanbao (元宝) groups: @mention users, query info/members.
- **google_meet** (`plugins/google_meet`) — Join a Google Meet call, transcribe live captions, optionally speak in realtime, and do the followup
- **apple-notes** (`skills/apple/apple-notes`) — Manage Apple Notes via memo CLI: create, search, edit.
- **apple-reminders** (`skills/apple/apple-reminders`) — Apple Reminders via remindctl: add, list, complete.
- **findmy** (`skills/apple/findmy`) — Track Apple devices/AirTags via FindMy.app on macOS.
- **imessage** (`skills/apple/imessage`) — Send and receive iMessages/SMS via the imsg CLI on macOS.
- **claude-code** (`skills/autonomous-ai-agents/claude-code`) — Delegate coding to Claude Code CLI (features, PRs).
- **codex** (`skills/autonomous-ai-agents/codex`) — Delegate coding to OpenAI Codex CLI (features, PRs).
- **computer-use** (`skills/autonomous-ai-agents/computer-use`) — Drive the desktop background-first; escalate on signal.
- **hermes-agent** (`skills/autonomous-ai-agents/hermes-agent`) — Use, configure, theme, extend, and orchestrate Hermes Agent.
- **architecture-diagram** (`skills/creative/architecture-diagram`) — Dark-themed SVG architecture/cloud/infra diagrams as HTML.
- **ascii-video** (`skills/creative/ascii-video`) — ASCII video: convert video/audio to colored ASCII MP4/GIF.
- **baoyu-infographic** (`skills/creative/baoyu-infographic`) — Infographics: 21 layouts x 21 styles (信息图, 可视化).
- **claude-design** (`skills/creative/claude-design`) — Design one-off HTML artifacts (landing, deck, prototype).
- **humanizer** (`skills/creative/humanizer`) — Humanize text: strip AI-isms and add real voice.
- **manim-video** (`skills/creative/manim-video`) — Manim CE animations: 3Blue1Brown math/algo videos.
- **p5js** (`skills/creative/p5js`) — p5.js sketches: gen art, shaders, interactive, 3D.
- **popular-web-designs** (`skills/creative/popular-web-designs`) — 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- **songwriting-and-ai-music** (`skills/creative/songwriting-and-ai-music`) — Songwriting craft and Suno AI music prompts.
- **sdlc-review** (`skills/devops/sdlc-review`) — Review Kanban handoffs and route verified outcomes.
- **email-inbox-triage** (`skills/email/email-inbox-triage`) — Triage an inbox: prioritize threads, draft replies safely.
- **himalaya** (`skills/email/himalaya`) — Himalaya CLI: IMAP/SMTP email from terminal.
- **youtube-content** (`skills/media/youtube-content`) — YouTube transcripts to summaries, threads, blogs.
- **obsidian** (`skills/note-taking/obsidian`) — Read, search, create, and edit notes in the Obsidian vault.
- **document-to-action-items** (`skills/productivity/document-to-action-items`) — Extract cited obligations, deadlines, tasks from documents.
- **google-workspace** (`skills/productivity/google-workspace`) — Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.
- **maps** (`skills/productivity/maps`) — Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- **meeting-action-items** (`skills/productivity/meeting-action-items`) — Turn meeting notes into cited decisions, owners, tickets.
- **microsoft-office** (`skills/productivity/microsoft-office`) — Create, read, and edit Word, PowerPoint, and Excel files.
- **pdf** (`skills/productivity/pdf`) — PDF files: create, read, merge, fill, OCR, edit text.
- **product-price-monitor** (`skills/productivity/product-price-monitor`) — Watch product, flight, or listing prices; alert on target.
- **teams-meeting-pipeline** (`skills/productivity/teams-meeting-pipeline`) — Teams meeting summaries, job replay, Graph subscriptions.
- **weekly-review-planning** (`skills/productivity/weekly-review-planning`) — Weekly reset: commitments, stalled work, next-week plan.
- **arxiv** (`skills/research/arxiv`) — Search arXiv papers by keyword, author, category, or ID.
- **competitor-news-monitor** (`skills/research/competitor-news-monitor`) — Watch named companies for material news; cited digests.
- **grounded-citations** (`skills/research/grounded-citations`) — Ground answers and documents in cited, verifiable sources.
- **xurl** (`skills/social-media/xurl`) — X/Twitter via xurl CLI: raw post search, posting, DM, media.
- **codebase-inspection** (`skills/software-development/codebase-inspection`) — Inspect codebases w/ pygount: LOC, languages, ratios.
- **dogfood** (`skills/software-development/dogfood`) — Exploratory QA of web apps: find bugs, evidence, reports.
- **github** (`skills/software-development/github`) — GitHub via gh CLI: PRs, issues, reviews, repos, auth.
- **requesting-code-review** (`skills/software-development/requesting-code-review`) — Pre-commit review: security scan, quality gates, auto-fix.
- **simplify-code** (`skills/software-development/simplify-code`) — Parallel 4-agent cleanup of recent code changes.
- **spike** (`skills/software-development/spike`) — Throwaway experiments to validate an idea before build.
- **systematic-debugging** (`skills/software-development/systematic-debugging`) — 4-phase root cause debugging: understand bugs before fixing.
- **test-driven-development** (`skills/software-development/test-driven-development`) — TDD: enforce RED-GREEN-REFACTOR, tests before code.
- **blocked-page-recovery** (`skills/web/blocked-page-recovery`) — Use when a fetch fails: 403/429, paywall, WAF, bot wall.

## 製品スコープ（通常は入れない）（28 repos）

### [morluto/rea](https://github.com/morluto/rea) — 5 skills ★425832
Reverse engineer anything with agents, from app behavior down to native binaries.

### [react/react](https://github.com/react/react) — 14 skills ★251892
The library for web and native user interfaces.

### [anomalyco/opencode](https://github.com/anomalyco/opencode) — 24 skills ★224276
The open source coding agent.

### [n8n-io/n8n](https://github.com/n8n-io/n8n) — 40 skills ★209447
Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

### [vercel/next.js](https://github.com/vercel/next.js) — 27 skills ★143245
The React Framework

### [nodejs/node](https://github.com/nodejs/node) — 28 skills ★123206
Node.js JavaScript runtime ✨🐢🚀✨

### [earendil-works/pi](https://github.com/earendil-works/pi) — 17 skills ★119797
AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI

### [supabase/supabase](https://github.com/supabase/supabase) — 24 skills ★114475
The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

### [microsoft/TypeScript](https://github.com/microsoft/TypeScript) — 4 skills ★111727
TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

### [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — 25 skills ★108700
An open-source AI agent that brings the power of Gemini directly into your terminal.

### [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) — 1 skills ★95791
JavaScript API for Chrome and Firefox

### [grafana/grafana](https://github.com/grafana/grafana) — 3 skills ★77656
The open and composable observability and data visualization platform. Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, Elasticsearch, InfluxDB, Postgres and many more. 

### [tw93/Mole](https://github.com/tw93/Mole) — 6 skills ★73722
🐹 Keep your Mac and PC clean, light, and running like new. Fast open-source CLI, plus native Mac and Windows apps.

### [ansible/ansible](https://github.com/ansible/ansible) — 4 skills ★71226
Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com.

### [BerriAI/litellm](https://github.com/BerriAI/litellm) — 11 skills ★62632
The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]

### [MemPalace/mempalace](https://github.com/MemPalace/mempalace) — 15 skills ★60318
The best-benchmarked open-source AI memory system. And it's free.

### [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) — 20 skills ★58382
Hindsight: Agent Memory That Learns

### [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — 11 skills ★45371
Browser automation CLI for AI agents

### [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) — 1 skills ★29095
The #1 AI Harness for Building Resumes, PDFs, Cover Letters & more, locally with 100+ LLMs support.

### [google-labs-code/design.md](https://github.com/google-labs-code/design.md) — 4 skills ★28701
A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system.

### [virattt/dexter](https://github.com/virattt/dexter) — 3 skills ★27753
An autonomous agent for deep financial research

### [steipete/CodexBar](https://github.com/steipete/CodexBar) — 3 skills ★22968
Show usage stats for OpenAI Codex and Claude Code, without having to login.

### [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — 29 skills ★21026
OpenShell is the safe, private runtime for autonomous AI agents.

### [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) — 2 skills ★16015
Towards a More Autonomous Agent System

### [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) — 17 skills ★13323
SolidCraft: an open-source parametric 3D CAD application built in pure Rust. Desktop, web, and automation through MCP.

### [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — 8 skills ★11955
Computer use CLI for AI agents

### [microsoft/inshellisense](https://github.com/microsoft/inshellisense) — 1 skills ★10754
IDE style command line auto complete

### [xykong/flux-markdown](https://github.com/xykong/flux-markdown) — 2 skills ★1296
Markdown Preview Enhanced for macOS QuickLook
