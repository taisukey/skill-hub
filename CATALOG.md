# CATALOG — Starred Agent Skills

GitHub Starred から SKILL.md を含むリポジトリだけを抽出し、分類したカタログ。
生成: build_catalog.py / 元データ: catalog.json

## 専用スキル集（導入候補）（19 repos）

### [obra/superpowers](https://github.com/obra/superpowers) — 15 skills ★311665
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

### [mattpocock/skills](https://github.com/mattpocock/skills) — 39 skills ★311031
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

### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — 1 skills ★64579
> 図解デザイン
Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 45 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop.
- **diagram-design** (`skills/diagram-design`) — Create branded architecture, architecture delta, IT current-state, flowchart, sequence, state machin

### [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) — 2 skills ★59907
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

### [heydamir/unslop](https://github.com/heydamir/unslop) — 1 skills ★7119
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

## コレクション（1 repos）

### [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — 864 skills ★78651
> キュレーション一覧＋Composio 自動化スキル 864 件
A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows
- **artifacts-builder** (`artifacts-builder`) — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern fronten
- **brand-guidelines** (`brand-guidelines`) — Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit fr
- **canvas-design** (`canvas-design`) — Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this 
- **changelog-generator** (`changelog-generator`) — Automatically creates user-facing changelogs from git commits by analyzing commit history, categoriz
- **competitive-ads-extractor** (`competitive-ads-extractor`) — Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand wh
- **-21risk-automation** (`composio-skills/-21risk-automation`) — Automate 21risk tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **-2chat-automation** (`composio-skills/-2chat-automation`) — Automate 2chat tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ably-automation** (`composio-skills/ably-automation`) — Automate Ably tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **abstract-automation** (`composio-skills/abstract-automation`) — Automate Abstract tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **abuselpdb-automation** (`composio-skills/abuselpdb-automation`) — Automate Abuselpdb tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **abyssale-automation** (`composio-skills/abyssale-automation`) — Automate Abyssale tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **accelo-automation** (`composio-skills/accelo-automation`) — Automate Accelo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **accredible-certificates-automation** (`composio-skills/accredible-certificates-automation`) — Automate Accredible Certificates tasks via Rube MCP (Composio). Always search tools first for curren
- **acculynx-automation** (`composio-skills/acculynx-automation`) — Automate Acculynx tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **active-campaign-automation** (`composio-skills/active-campaign-automation`) — Automate ActiveCampaign tasks via Rube MCP (Composio). Always search tools first for current schemas
- **addresszen-automation** (`composio-skills/addresszen-automation`) — Automate Addresszen tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **adobe-automation** (`composio-skills/adobe-automation`) — Automate Adobe tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **adrapid-automation** (`composio-skills/adrapid-automation`) — Automate Adrapid tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **adyntel-automation** (`composio-skills/adyntel-automation`) — Automate Adyntel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **aero-workflow-automation** (`composio-skills/aero-workflow-automation`) — Automate Aero Workflow tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **aeroleads-automation** (`composio-skills/aeroleads-automation`) — Automate Aeroleads tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **affinda-automation** (`composio-skills/affinda-automation`) — Automate Affinda tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **affinity-automation** (`composio-skills/affinity-automation`) — Automate Affinity tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **agencyzoom-automation** (`composio-skills/agencyzoom-automation`) — Automate Agencyzoom tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **agent-mail-automation** (`composio-skills/agent-mail-automation`) — Automate Agent Mail tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **agentql-automation** (`composio-skills/agentql-automation`) — Automate Agentql tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **agenty-automation** (`composio-skills/agenty-automation`) — Automate Agenty tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **agiled-automation** (`composio-skills/agiled-automation`) — Automate Agiled tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **agility-cms-automation** (`composio-skills/agility-cms-automation`) — Automate Agility CMS tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Ahrefs Automation** (`composio-skills/ahrefs-automation`) — Automate SEO research with Ahrefs -- analyze backlink profiles, research keywords, track domain metr
- **ai-ml-api-automation** (`composio-skills/ai-ml-api-automation`) — Automate AI ML API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **aivoov-automation** (`composio-skills/aivoov-automation`) — Automate Aivoov tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **alchemy-automation** (`composio-skills/alchemy-automation`) — Automate Alchemy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **algodocs-automation** (`composio-skills/algodocs-automation`) — Automate Algodocs tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **algolia-automation** (`composio-skills/algolia-automation`) — Automate Algolia tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **all-images-ai-automation** (`composio-skills/all-images-ai-automation`) — Automate All Images AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **alpha-vantage-automation** (`composio-skills/alpha-vantage-automation`) — Automate Alpha Vantage tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **altoviz-automation** (`composio-skills/altoviz-automation`) — Automate Altoviz tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **alttext-ai-automation** (`composio-skills/alttext-ai-automation`) — Automate Alttext AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **amara-automation** (`composio-skills/amara-automation`) — Automate Amara tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **amazon-automation** (`composio-skills/amazon-automation`) — Automate Amazon tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ambee-automation** (`composio-skills/ambee-automation`) — Automate Ambee tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ambient-weather-automation** (`composio-skills/ambient-weather-automation`) — Automate Ambient Weather tasks via Rube MCP (Composio). Always search tools first for current schema
- **amcards-automation** (`composio-skills/amcards-automation`) — Automate Amcards tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **anchor-browser-automation** (`composio-skills/anchor-browser-automation`) — Automate Anchor Browser tasks via Rube MCP (Composio). Always search tools first for current schemas
- **anonyflow-automation** (`composio-skills/anonyflow-automation`) — Automate Anonyflow tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **anthropic-administrator-automation** (`composio-skills/anthropic-administrator-automation`) — Automate Anthropic Admin tasks via Rube MCP (Composio). Always search tools first for current schema
- **anthropic_administrator-automation** (`composio-skills/anthropic_administrator-automation`) — Automate Anthropic Admin tasks via Rube MCP (Composio): API keys, usage, workspaces, and organizatio
- **apaleo-automation** (`composio-skills/apaleo-automation`) — Automate Apaleo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **apex27-automation** (`composio-skills/apex27-automation`) — Automate Apex27 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **api-bible-automation** (`composio-skills/api-bible-automation`) — Automate API Bible tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **api-labz-automation** (`composio-skills/api-labz-automation`) — Automate API Labz tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **api-ninjas-automation** (`composio-skills/api-ninjas-automation`) — Automate API Ninjas tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **api-sports-automation** (`composio-skills/api-sports-automation`) — Automate API Sports tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **api2pdf-automation** (`composio-skills/api2pdf-automation`) — Automate Api2pdf tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **apiflash-automation** (`composio-skills/apiflash-automation`) — Automate Apiflash tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Apify Automation** (`composio-skills/apify-automation`) — Automate web scraping and data extraction with Apify -- run Actors, manage datasets, create reusable
- **apilio-automation** (`composio-skills/apilio-automation`) — Automate Apilio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **apipie-ai-automation** (`composio-skills/apipie-ai-automation`) — Automate Apipie AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **apitemplate-io-automation** (`composio-skills/apitemplate-io-automation`) — Automate Apitemplate IO tasks via Rube MCP (Composio). Always search tools first for current schemas
- **apiverve-automation** (`composio-skills/apiverve-automation`) — Automate Apiverve tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Apollo Automation** (`composio-skills/apollo-automation`) — Automate Apollo.io lead generation -- search organizations, discover contacts, enrich prospect data,
- **appcircle-automation** (`composio-skills/appcircle-automation`) — Automate Appcircle tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **appdrag-automation** (`composio-skills/appdrag-automation`) — Automate Appdrag tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **appointo-automation** (`composio-skills/appointo-automation`) — Automate Appointo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **appsflyer-automation** (`composio-skills/appsflyer-automation`) — Automate Appsflyer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **appveyor-automation** (`composio-skills/appveyor-automation`) — Automate Appveyor tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **aryn-automation** (`composio-skills/aryn-automation`) — Automate Aryn tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ascora-automation** (`composio-skills/ascora-automation`) — Automate Ascora tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Ashby Automation** (`composio-skills/ashby-automation`) — Automate recruiting and hiring workflows in Ashby -- manage candidates, jobs, applications, intervie
- **asin-data-api-automation** (`composio-skills/asin-data-api-automation`) — Automate Asin Data API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **astica-ai-automation** (`composio-skills/astica-ai-automation`) — Automate Astica AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **async-interview-automation** (`composio-skills/async-interview-automation`) — Automate Async Interview tasks via Rube MCP (Composio). Always search tools first for current schema
- **atlassian-automation** (`composio-skills/atlassian-automation`) — Automate Atlassian tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Attio Automation** (`composio-skills/attio-automation`) — Automate Attio CRM operations -- search records, query contacts and companies with advanced filters,
- **auth0-automation** (`composio-skills/auth0-automation`) — Automate Auth0 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **autobound-automation** (`composio-skills/autobound-automation`) — Automate Autobound tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **autom-automation** (`composio-skills/autom-automation`) — Automate Autom tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **axonaut-automation** (`composio-skills/axonaut-automation`) — Automate Axonaut tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ayrshare-automation** (`composio-skills/ayrshare-automation`) — Automate Ayrshare tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **backendless-automation** (`composio-skills/backendless-automation`) — Automate Backendless tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bannerbear-automation** (`composio-skills/bannerbear-automation`) — Automate Bannerbear tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bart-automation** (`composio-skills/bart-automation`) — Automate Bart tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **baselinker-automation** (`composio-skills/baselinker-automation`) — Automate Baselinker tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **baserow-automation** (`composio-skills/baserow-automation`) — Automate Baserow tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **basin-automation** (`composio-skills/basin-automation`) — Automate Basin tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **battlenet-automation** (`composio-skills/battlenet-automation`) — Automate Battlenet tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **beaconchain-automation** (`composio-skills/beaconchain-automation`) — Automate Beaconchain tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **beaconstac-automation** (`composio-skills/beaconstac-automation`) — Automate Beaconstac tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **beamer-automation** (`composio-skills/beamer-automation`) — Automate Beamer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **beeminder-automation** (`composio-skills/beeminder-automation`) — Automate Beeminder tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bench-automation** (`composio-skills/bench-automation`) — Automate Bench tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **benchmark-email-automation** (`composio-skills/benchmark-email-automation`) — Automate Benchmark Email tasks via Rube MCP (Composio). Always search tools first for current schema
- **benzinga-automation** (`composio-skills/benzinga-automation`) — Automate Benzinga tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bestbuy-automation** (`composio-skills/bestbuy-automation`) — Automate Bestbuy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **better-proposals-automation** (`composio-skills/better-proposals-automation`) — Automate Better Proposals tasks via Rube MCP (Composio). Always search tools first for current schem
- **better-stack-automation** (`composio-skills/better-stack-automation`) — Automate Better Stack tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bidsketch-automation** (`composio-skills/bidsketch-automation`) — Automate Bidsketch tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **big-data-cloud-automation** (`composio-skills/big-data-cloud-automation`) — Automate Big Data Cloud tasks via Rube MCP (Composio). Always search tools first for current schemas
- **bigmailer-automation** (`composio-skills/bigmailer-automation`) — Automate Bigmailer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bigml-automation** (`composio-skills/bigml-automation`) — Automate Bigml tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bigpicture-io-automation** (`composio-skills/bigpicture-io-automation`) — Automate Bigpicture IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bitquery-automation** (`composio-skills/bitquery-automation`) — Automate Bitquery tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bitwarden-automation** (`composio-skills/bitwarden-automation`) — Automate Bitwarden tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **blackbaud-automation** (`composio-skills/blackbaud-automation`) — Automate Blackbaud tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **blackboard-automation** (`composio-skills/blackboard-automation`) — Automate Blackboard tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **blocknative-automation** (`composio-skills/blocknative-automation`) — Automate Blocknative tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **boldsign-automation** (`composio-skills/boldsign-automation`) — Automate Boldsign tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bolna-automation** (`composio-skills/bolna-automation`) — Automate Bolna tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **boloforms-automation** (`composio-skills/boloforms-automation`) — Automate Boloforms tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bolt-iot-automation** (`composio-skills/bolt-iot-automation`) — Automate Bolt Iot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bonsai-automation** (`composio-skills/bonsai-automation`) — Automate Bonsai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bookingmood-automation** (`composio-skills/bookingmood-automation`) — Automate Bookingmood tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **booqable-automation** (`composio-skills/booqable-automation`) — Automate Booqable tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **borneo-automation** (`composio-skills/borneo-automation`) — Automate Borneo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **botbaba-automation** (`composio-skills/botbaba-automation`) — Automate Botbaba tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **botpress-automation** (`composio-skills/botpress-automation`) — Automate Botpress tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **botsonic-automation** (`composio-skills/botsonic-automation`) — Automate Botsonic tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **botstar-automation** (`composio-skills/botstar-automation`) — Automate Botstar tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bouncer-automation** (`composio-skills/bouncer-automation`) — Automate Bouncer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **boxhero-automation** (`composio-skills/boxhero-automation`) — Automate Boxhero tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Braintree Automation** (`composio-skills/braintree-automation`) — Braintree Automation: manage payment processing via Stripe-compatible tools for customers, subscript
- **brandfetch-automation** (`composio-skills/brandfetch-automation`) — Automate Brandfetch tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **breeze-automation** (`composio-skills/breeze-automation`) — Automate Breeze tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **breezy-hr-automation** (`composio-skills/breezy-hr-automation`) — Automate Breezy HR tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **brex-automation** (`composio-skills/brex-automation`) — Automate Brex tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **brex-staging-automation** (`composio-skills/brex-staging-automation`) — Automate Brex Staging tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **brightdata-automation** (`composio-skills/brightdata-automation`) — Automate Brightdata tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **brightpearl-automation** (`composio-skills/brightpearl-automation`) — Automate Brightpearl tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **brilliant-directories-automation** (`composio-skills/brilliant-directories-automation`) — Automate Brilliant Directories tasks via Rube MCP (Composio). Always search tools first for current 
- **browseai-automation** (`composio-skills/browseai-automation`) — Automate Browseai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **browser-tool-automation** (`composio-skills/browser-tool-automation`) — Automate Browser Tool tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **browserbase-tool-automation** (`composio-skills/browserbase-tool-automation`) — Automate Browserbase Tool tasks via Rube MCP (Composio). Always search tools first for current schem
- **browserhub-automation** (`composio-skills/browserhub-automation`) — Automate Browserhub tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **browserless-automation** (`composio-skills/browserless-automation`) — Automate Browserless tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **btcpay-server-automation** (`composio-skills/btcpay-server-automation`) — Automate Btcpay Server tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bubble-automation** (`composio-skills/bubble-automation`) — Automate Bubble tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bugbug-automation** (`composio-skills/bugbug-automation`) — Automate Bugbug tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bugherd-automation** (`composio-skills/bugherd-automation`) — Automate Bugherd tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bugsnag-automation** (`composio-skills/bugsnag-automation`) — Automate Bugsnag tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **buildkite-automation** (`composio-skills/buildkite-automation`) — Automate Buildkite tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **builtwith-automation** (`composio-skills/builtwith-automation`) — Automate Builtwith tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **bunnycdn-automation** (`composio-skills/bunnycdn-automation`) — Automate Bunnycdn tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **byteforms-automation** (`composio-skills/byteforms-automation`) — Automate Byteforms tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cabinpanda-automation** (`composio-skills/cabinpanda-automation`) — Automate Cabinpanda tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cal-automation** (`composio-skills/cal-automation`) — Automate Cal tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **calendarhero-automation** (`composio-skills/calendarhero-automation`) — Automate Calendarhero tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **callerapi-automation** (`composio-skills/callerapi-automation`) — Automate Callerapi tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **callingly-automation** (`composio-skills/callingly-automation`) — Automate Callingly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **callpage-automation** (`composio-skills/callpage-automation`) — Automate Callpage tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **campaign-cleaner-automation** (`composio-skills/campaign-cleaner-automation`) — Automate Campaign Cleaner tasks via Rube MCP (Composio). Always search tools first for current schem
- **campayn-automation** (`composio-skills/campayn-automation`) — Automate Campayn tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **canny-automation** (`composio-skills/canny-automation`) — Automate Canny tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **canvas-automation** (`composio-skills/canvas-automation`) — Automate Canvas tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Capsule CRM Automation** (`composio-skills/capsule-crm-automation`) — Automate Capsule CRM operations -- manage contacts (parties), run structured filter queries, track t
- **capsule_crm-automation** (`composio-skills/capsule_crm-automation`) — Automate Capsule CRM tasks via Rube MCP (Composio): contacts, opportunities, cases, tasks, and pipel
- **carbone-automation** (`composio-skills/carbone-automation`) — Automate Carbone tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cardly-automation** (`composio-skills/cardly-automation`) — Automate Cardly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **castingwords-automation** (`composio-skills/castingwords-automation`) — Automate Castingwords tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cats-automation** (`composio-skills/cats-automation`) — Automate Cats tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cdr-platform-automation** (`composio-skills/cdr-platform-automation`) — Automate Cdr Platform tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **census-bureau-automation** (`composio-skills/census-bureau-automation`) — Automate Census Bureau tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **centralstationcrm-automation** (`composio-skills/centralstationcrm-automation`) — Automate Centralstationcrm tasks via Rube MCP (Composio). Always search tools first for current sche
- **certifier-automation** (`composio-skills/certifier-automation`) — Automate Certifier tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **chaser-automation** (`composio-skills/chaser-automation`) — Automate Chaser tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **chatbotkit-automation** (`composio-skills/chatbotkit-automation`) — Automate Chatbotkit tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **chatfai-automation** (`composio-skills/chatfai-automation`) — Automate Chatfai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **chatwork-automation** (`composio-skills/chatwork-automation`) — Automate Chatwork tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **chmeetings-automation** (`composio-skills/chmeetings-automation`) — Automate Chmeetings tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cincopa-automation** (`composio-skills/cincopa-automation`) — Automate Cincopa tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **claid-ai-automation** (`composio-skills/claid-ai-automation`) — Automate Claid AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **classmarker-automation** (`composio-skills/classmarker-automation`) — Automate Classmarker tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **clearout-automation** (`composio-skills/clearout-automation`) — Automate Clearout tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **clickmeeting-automation** (`composio-skills/clickmeeting-automation`) — Automate Clickmeeting tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Clockify Automation** (`composio-skills/clockify-automation`) — Automate time tracking workflows in Clockify -- create and manage time entries, workspaces, and user
- **cloudcart-automation** (`composio-skills/cloudcart-automation`) — Automate Cloudcart tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cloudconvert-automation** (`composio-skills/cloudconvert-automation`) — Automate Cloudconvert tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cloudflare-api-key-automation** (`composio-skills/cloudflare-api-key-automation`) — Automate Cloudflare API tasks via Rube MCP (Composio). Always search tools first for current schemas
- **cloudflare-automation** (`composio-skills/cloudflare-automation`) — Automate Cloudflare tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cloudflare-browser-rendering-automation** (`composio-skills/cloudflare-browser-rendering-automation`) — Automate Cloudflare Browser Rendering tasks via Rube MCP (Composio). Always search tools first for c
- **Cloudinary Automation** (`composio-skills/cloudinary-automation`) — Automate Cloudinary media management including folder organization, upload presets, asset lookup, tr
- **cloudlayer-automation** (`composio-skills/cloudlayer-automation`) — Automate Cloudlayer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cloudpress-automation** (`composio-skills/cloudpress-automation`) — Automate Cloudpress tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **coassemble-automation** (`composio-skills/coassemble-automation`) — Automate Coassemble tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **codacy-automation** (`composio-skills/codacy-automation`) — Automate Codacy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **codeinterpreter-automation** (`composio-skills/codeinterpreter-automation`) — Automate Codeinterpreter tasks via Rube MCP (Composio). Always search tools first for current schema
- **codereadr-automation** (`composio-skills/codereadr-automation`) — Automate Codereadr tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Coinbase Automation** (`composio-skills/coinbase-automation`) — Coinbase Automation: list and manage cryptocurrency wallets, accounts, and portfolio data via Coinba
- **coinmarketcal-automation** (`composio-skills/coinmarketcal-automation`) — Automate Coinmarketcal tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **coinmarketcap-automation** (`composio-skills/coinmarketcap-automation`) — Automate Coinmarketcap tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **coinranking-automation** (`composio-skills/coinranking-automation`) — Automate Coinranking tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **college-football-data-automation** (`composio-skills/college-football-data-automation`) — Automate College Football Data tasks via Rube MCP (Composio). Always search tools first for current 
- **composio-automation** (`composio-skills/composio-automation`) — Automate Composio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **composio-search-automation** (`composio-skills/composio-search-automation`) — Automate Composio Search tasks via Rube MCP (Composio). Always search tools first for current schema
- **connecteam-automation** (`composio-skills/connecteam-automation`) — Automate Connecteam tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Contentful Automation** (`composio-skills/contentful-automation`) — Automate headless CMS operations in Contentful -- list spaces, retrieve space metadata, and update s
- **contentful-graphql-automation** (`composio-skills/contentful-graphql-automation`) — Automate Contentful Graphql tasks via Rube MCP (Composio). Always search tools first for current sch
- **control-d-automation** (`composio-skills/control-d-automation`) — Automate Control D tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **conversion-tools-automation** (`composio-skills/conversion-tools-automation`) — Automate Conversion Tools tasks via Rube MCP (Composio). Always search tools first for current schem
- **convertapi-automation** (`composio-skills/convertapi-automation`) — Automate Convertapi tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **conveyor-automation** (`composio-skills/conveyor-automation`) — Automate Conveyor tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **convolo-ai-automation** (`composio-skills/convolo-ai-automation`) — Automate Convolo AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **corrently-automation** (`composio-skills/corrently-automation`) — Automate Corrently tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **countdown-api-automation** (`composio-skills/countdown-api-automation`) — Automate Countdown API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **coupa-automation** (`composio-skills/coupa-automation`) — Automate Coupa tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **craftmypdf-automation** (`composio-skills/craftmypdf-automation`) — Automate Craftmypdf tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **crowdin-automation** (`composio-skills/crowdin-automation`) — Automate Crowdin tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **crustdata-automation** (`composio-skills/crustdata-automation`) — Automate Crustdata tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cults-automation** (`composio-skills/cults-automation`) — Automate Cults tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **curated-automation** (`composio-skills/curated-automation`) — Automate Curated tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **currents-api-automation** (`composio-skills/currents-api-automation`) — Automate Currents API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Customer.io Automation** (`composio-skills/customerio-automation`) — Automate customer engagement workflows including broadcast triggers, message analytics, segment mana
- **customgpt-automation** (`composio-skills/customgpt-automation`) — Automate Customgpt tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **customjs-automation** (`composio-skills/customjs-automation`) — Automate Customjs tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **cutt-ly-automation** (`composio-skills/cutt-ly-automation`) — Automate Cutt Ly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **d2lbrightspace-automation** (`composio-skills/d2lbrightspace-automation`) — Automate D2lbrightspace tasks via Rube MCP (Composio). Always search tools first for current schemas
- **dadata-ru-automation** (`composio-skills/dadata-ru-automation`) — Automate Dadata Ru tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **daffy-automation** (`composio-skills/daffy-automation`) — Automate Daffy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dailybot-automation** (`composio-skills/dailybot-automation`) — Automate Dailybot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **datagma-automation** (`composio-skills/datagma-automation`) — Automate Datagma tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **datarobot-automation** (`composio-skills/datarobot-automation`) — Automate Datarobot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **deadline-funnel-automation** (`composio-skills/deadline-funnel-automation`) — Automate Deadline Funnel tasks via Rube MCP (Composio). Always search tools first for current schema
- **deel-automation** (`composio-skills/deel-automation`) — Automate Deel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **deepgram-automation** (`composio-skills/deepgram-automation`) — Automate Deepgram tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **demio-automation** (`composio-skills/demio-automation`) — Automate Demio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **desktime-automation** (`composio-skills/desktime-automation`) — Automate Desktime tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **detrack-automation** (`composio-skills/detrack-automation`) — Automate Detrack tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dialmycalls-automation** (`composio-skills/dialmycalls-automation`) — Automate Dialmycalls tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dialpad-automation** (`composio-skills/dialpad-automation`) — Automate Dialpad tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dictionary-api-automation** (`composio-skills/dictionary-api-automation`) — Automate Dictionary API tasks via Rube MCP (Composio). Always search tools first for current schemas
- **diffbot-automation** (`composio-skills/diffbot-automation`) — Automate Diffbot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **digicert-automation** (`composio-skills/digicert-automation`) — Automate Digicert tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **digital-ocean-automation** (`composio-skills/digital-ocean-automation`) — Automate DigitalOcean tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **discordbot-automation** (`composio-skills/discordbot-automation`) — Automate Discordbot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dnsfilter-automation** (`composio-skills/dnsfilter-automation`) — Automate Dnsfilter tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dock-certs-automation** (`composio-skills/dock-certs-automation`) — Automate Dock Certs tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Docker Hub Automation** (`composio-skills/docker-hub-automation`) — Automate Docker Hub operations -- manage organizations, repositories, teams, members, and webhooks v
- **docker_hub-automation** (`composio-skills/docker_hub-automation`) — Automate Docker Hub tasks via Rube MCP (Composio): repositories, images, tags, and container registr
- **docmosis-automation** (`composio-skills/docmosis-automation`) — Automate Docmosis tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docnify-automation** (`composio-skills/docnify-automation`) — Automate Docnify tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docsbot-ai-automation** (`composio-skills/docsbot-ai-automation`) — Automate Docsbot AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docsumo-automation** (`composio-skills/docsumo-automation`) — Automate Docsumo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docugenerate-automation** (`composio-skills/docugenerate-automation`) — Automate Docugenerate tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **documenso-automation** (`composio-skills/documenso-automation`) — Automate Documenso tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **documint-automation** (`composio-skills/documint-automation`) — Automate Documint tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docupilot-automation** (`composio-skills/docupilot-automation`) — Automate Docupilot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docupost-automation** (`composio-skills/docupost-automation`) — Automate Docupost tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **docuseal-automation** (`composio-skills/docuseal-automation`) — Automate Docuseal tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **doppler-marketing-automation-automation** (`composio-skills/doppler-marketing-automation-automation`) — Automate Doppler Marketing Automation tasks via Rube MCP (Composio). Always search tools first for c
- **doppler-secretops-automation** (`composio-skills/doppler-secretops-automation`) — Automate Doppler Secretops tasks via Rube MCP (Composio). Always search tools first for current sche
- **dotsimple-automation** (`composio-skills/dotsimple-automation`) — Automate Dotsimple tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dovetail-automation** (`composio-skills/dovetail-automation`) — Automate Dovetail tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dpd2-automation** (`composio-skills/dpd2-automation`) — Automate Dpd2 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **draftable-automation** (`composio-skills/draftable-automation`) — Automate Draftable tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dreamstudio-automation** (`composio-skills/dreamstudio-automation`) — Automate Dreamstudio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **drip-jobs-automation** (`composio-skills/drip-jobs-automation`) — Automate Drip Jobs tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dripcel-automation** (`composio-skills/dripcel-automation`) — Automate Dripcel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dromo-automation** (`composio-skills/dromo-automation`) — Automate Dromo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dropbox-sign-automation** (`composio-skills/dropbox-sign-automation`) — Automate Dropbox Sign tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dropcontact-automation** (`composio-skills/dropcontact-automation`) — Automate Dropcontact tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **dungeon-fighter-online-automation** (`composio-skills/dungeon-fighter-online-automation`) — Automate Dungeon Fighter Online tasks via Rube MCP (Composio). Always search tools first for current
- **Dynamics 365 Automation** (`composio-skills/dynamics365-automation`) — Dynamics 365 Automation: manage CRM contacts, accounts, leads, opportunities, sales orders, invoices
- **echtpost-automation** (`composio-skills/echtpost-automation`) — Automate Echtpost tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ElevenLabs Automation** (`composio-skills/elevenlabs-automation`) — Automate ElevenLabs text-to-speech workflows -- generate speech from text, browse and inspect voices
- **elorus-automation** (`composio-skills/elorus-automation`) — Automate Elorus tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **emailable-automation** (`composio-skills/emailable-automation`) — Automate Emailable tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **emaillistverify-automation** (`composio-skills/emaillistverify-automation`) — Automate Emaillistverify tasks via Rube MCP (Composio). Always search tools first for current schema
- **emailoctopus-automation** (`composio-skills/emailoctopus-automation`) — Automate Emailoctopus tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **emelia-automation** (`composio-skills/emelia-automation`) — Automate Emelia tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **encodian-automation** (`composio-skills/encodian-automation`) — Automate Encodian tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **endorsal-automation** (`composio-skills/endorsal-automation`) — Automate Endorsal tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **enginemailer-automation** (`composio-skills/enginemailer-automation`) — Automate Enginemailer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **enigma-automation** (`composio-skills/enigma-automation`) — Automate Enigma tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **entelligence-automation** (`composio-skills/entelligence-automation`) — Automate Entelligence tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **eodhd-apis-automation** (`composio-skills/eodhd-apis-automation`) — Automate Eodhd Apis tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **epic-games-automation** (`composio-skills/epic-games-automation`) — Automate Epic Games tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **esignatures-io-automation** (`composio-skills/esignatures-io-automation`) — Automate Esignatures IO tasks via Rube MCP (Composio). Always search tools first for current schemas
- **espocrm-automation** (`composio-skills/espocrm-automation`) — Automate Espocrm tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **esputnik-automation** (`composio-skills/esputnik-automation`) — Automate Esputnik tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **etermin-automation** (`composio-skills/etermin-automation`) — Automate Etermin tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **evenium-automation** (`composio-skills/evenium-automation`) — Automate Evenium tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Eventbrite Automation** (`composio-skills/eventbrite-automation`) — Automate Eventbrite event management, attendee tracking, organization discovery, and category browsi
- **eventee-automation** (`composio-skills/eventee-automation`) — Automate Eventee tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **eventzilla-automation** (`composio-skills/eventzilla-automation`) — Automate Eventzilla tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **everhour-automation** (`composio-skills/everhour-automation`) — Automate Everhour tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **eversign-automation** (`composio-skills/eversign-automation`) — Automate Eversign tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **exa-automation** (`composio-skills/exa-automation`) — Automate Exa tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Excel Automation** (`composio-skills/excel-automation`) — Excel Automation: create workbooks, manage worksheets, read/write cell data, and format spreadsheets
- **exist-automation** (`composio-skills/exist-automation`) — Automate Exist tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **expofp-automation** (`composio-skills/expofp-automation`) — Automate Expofp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **extracta-ai-automation** (`composio-skills/extracta-ai-automation`) — Automate Extracta AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Facebook Automation** (`composio-skills/facebook-automation`) — Automate Facebook Page management including post creation, scheduling, video uploads, Messenger conv
- **faceup-automation** (`composio-skills/faceup-automation`) — Automate Faceup tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **factorial-automation** (`composio-skills/factorial-automation`) — Automate Factorial tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **feathery-automation** (`composio-skills/feathery-automation`) — Automate Feathery tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **felt-automation** (`composio-skills/felt-automation`) — Automate Felt tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fibery-automation** (`composio-skills/fibery-automation`) — Automate Fibery tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fidel-api-automation** (`composio-skills/fidel-api-automation`) — Automate Fidel API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **files-com-automation** (`composio-skills/files-com-automation`) — Automate Files Com tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fillout-forms-automation** (`composio-skills/fillout-forms-automation`) — Automate Fillout tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fillout_forms-automation** (`composio-skills/fillout_forms-automation`) — Automate Fillout tasks via Rube MCP (Composio): forms, submissions, workflows, and form builder. Alw
- **finage-automation** (`composio-skills/finage-automation`) — Automate Finage tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **findymail-automation** (`composio-skills/findymail-automation`) — Automate Findymail tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **finerworks-automation** (`composio-skills/finerworks-automation`) — Automate Finerworks tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fingertip-automation** (`composio-skills/fingertip-automation`) — Automate Fingertip tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **finmei-automation** (`composio-skills/finmei-automation`) — Automate Finmei tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fireberry-automation** (`composio-skills/fireberry-automation`) — Automate Fireberry tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Firecrawl Automation** (`composio-skills/firecrawl-automation`) — Automate web crawling and data extraction with Firecrawl -- scrape pages, crawl sites, extract struc
- **fireflies-automation** (`composio-skills/fireflies-automation`) — Automate Fireflies tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **firmao-automation** (`composio-skills/firmao-automation`) — Automate Firmao tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fitbit-automation** (`composio-skills/fitbit-automation`) — Automate Fitbit tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fixer-automation** (`composio-skills/fixer-automation`) — Automate Fixer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fixer-io-automation** (`composio-skills/fixer-io-automation`) — Automate Fixer IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **flexisign-automation** (`composio-skills/flexisign-automation`) — Automate Flexisign tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **flowiseai-automation** (`composio-skills/flowiseai-automation`) — Automate Flowiseai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **flutterwave-automation** (`composio-skills/flutterwave-automation`) — Automate Flutterwave tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fluxguard-automation** (`composio-skills/fluxguard-automation`) — Automate Fluxguard tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **folk-automation** (`composio-skills/folk-automation`) — Automate Folk tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fomo-automation** (`composio-skills/fomo-automation`) — Automate Fomo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **forcemanager-automation** (`composio-skills/forcemanager-automation`) — Automate Forcemanager tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **formbricks-automation** (`composio-skills/formbricks-automation`) — Automate Formbricks tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **formcarry-automation** (`composio-skills/formcarry-automation`) — Automate Formcarry tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **formdesk-automation** (`composio-skills/formdesk-automation`) — Automate Formdesk tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **formsite-automation** (`composio-skills/formsite-automation`) — Automate Formsite tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **foursquare-automation** (`composio-skills/foursquare-automation`) — Automate Foursquare tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fraudlabs-pro-automation** (`composio-skills/fraudlabs-pro-automation`) — Automate Fraudlabs Pro tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **FreshBooks Automation** (`composio-skills/freshbooks-automation`) — FreshBooks Automation: manage businesses, projects, time tracking, and billing in FreshBooks cloud a
- **front-automation** (`composio-skills/front-automation`) — Automate Front tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **fullenrich-automation** (`composio-skills/fullenrich-automation`) — Automate Fullenrich tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gagelist-automation** (`composio-skills/gagelist-automation`) — Automate Gagelist tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gamma-automation** (`composio-skills/gamma-automation`) — Automate Gamma tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gan-ai-automation** (`composio-skills/gan-ai-automation`) — Automate Gan AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gatherup-automation** (`composio-skills/gatherup-automation`) — Automate Gatherup tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gemini-automation** (`composio-skills/gemini-automation`) — Automate Gemini tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gender-api-automation** (`composio-skills/gender-api-automation`) — Automate Gender API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **genderapi-io-automation** (`composio-skills/genderapi-io-automation`) — Automate Genderapi IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **genderize-automation** (`composio-skills/genderize-automation`) — Automate Genderize tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **geoapify-automation** (`composio-skills/geoapify-automation`) — Automate Geoapify tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **geocodio-automation** (`composio-skills/geocodio-automation`) — Automate Geocodio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **geokeo-automation** (`composio-skills/geokeo-automation`) — Automate Geokeo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **getform-automation** (`composio-skills/getform-automation`) — Automate Getform tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gift-up-automation** (`composio-skills/gift-up-automation`) — Automate Gift Up tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gigasheet-automation** (`composio-skills/gigasheet-automation`) — Automate Gigasheet tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **giphy-automation** (`composio-skills/giphy-automation`) — Automate Giphy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gist-automation** (`composio-skills/gist-automation`) — Automate Gist tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **givebutter-automation** (`composio-skills/givebutter-automation`) — Automate Givebutter tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gladia-automation** (`composio-skills/gladia-automation`) — Automate Gladia tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **gleap-automation** (`composio-skills/gleap-automation`) — Automate Gleap tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **globalping-automation** (`composio-skills/globalping-automation`) — Automate Globalping tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **go-to-webinar-automation** (`composio-skills/go-to-webinar-automation`) — Automate GoToWebinar tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **godial-automation** (`composio-skills/godial-automation`) — Automate Godial tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Gong Automation** (`composio-skills/gong-automation`) — Automate Gong conversation intelligence -- retrieve call recordings, transcripts, detailed analytics
- **goodbits-automation** (`composio-skills/goodbits-automation`) — Automate Goodbits tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **goody-automation** (`composio-skills/goody-automation`) — Automate Goody tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **google-address-validation-automation** (`composio-skills/google-address-validation-automation`) — Automate Google Address Validation tasks via Rube MCP (Composio). Always search tools first for curr
- **google-admin-automation** (`composio-skills/google-admin-automation`) — Automate Google Workspace Admin tasks via Rube MCP (Composio): manage users, groups, memberships, su
- **google-classroom-automation** (`composio-skills/google-classroom-automation`) — Automate Google Classroom tasks via Rube MCP (Composio). Always search tools first for current schem
- **google-cloud-vision-automation** (`composio-skills/google-cloud-vision-automation`) — Automate Google Cloud Vision tasks via Rube MCP (Composio). Always search tools first for current sc
- **google-maps-automation** (`composio-skills/google-maps-automation`) — Automate Google Maps tasks via Rube MCP (Composio): geocode addresses, search places, get directions
- **google-search-console-automation** (`composio-skills/google-search-console-automation`) — Automate Google Search Console tasks via Rube MCP (Composio): query search analytics, list sites, in
- **google_admin-automation** (`composio-skills/google_admin-automation`) — Automate Google Admin tasks via Rube MCP (Composio): user management, org units, groups, and domain 
- **google_classroom-automation** (`composio-skills/google_classroom-automation`) — Automate Google Classroom tasks via Rube MCP (Composio): course management, assignments, student ros
- **google_maps-automation** (`composio-skills/google_maps-automation`) — Automate Google Maps tasks via Rube MCP (Composio): geocoding, directions, place search, and distanc
- **google_search_console-automation** (`composio-skills/google_search_console-automation`) — Automate Google Search Console tasks via Rube MCP (Composio): search performance, URL inspection, si
- **googleads-automation** (`composio-skills/googleads-automation`) — Automate Google Ads analytics tasks via Rube MCP (Composio): list Google Ads links, run GA4 reports,
- **googlebigquery-automation** (`composio-skills/googlebigquery-automation`) — Automate Google BigQuery tasks via Rube MCP (Composio): run SQL queries, explore datasets and metada
- **googlecalendar-automation** (`composio-skills/googlecalendar-automation`) — Automate Google Calendar tasks via Rube MCP (Composio). Always search tools first for current schema
- **googledocs-automation** (`composio-skills/googledocs-automation`) — Automate Google Docs tasks via Rube MCP (Composio): create, edit, search, export, copy, and update d
- **googledrive-automation** (`composio-skills/googledrive-automation`) — Automate Google Drive tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **googlemeet-automation** (`composio-skills/googlemeet-automation`) — Automate Google Meet tasks via Rube MCP (Composio): create Meet spaces, schedule video conferences v
- **googlephotos-automation** (`composio-skills/googlephotos-automation`) — Automate Google Photos tasks via Rube MCP (Composio): upload media, manage albums, search photos, ba
- **googleslides-automation** (`composio-skills/googleslides-automation`) — Automate Google Slides tasks via Rube MCP (Composio): create presentations, add slides from Markdown
- **googlesuper-automation** (`composio-skills/googlesuper-automation`) — Automate Google Super tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **googletasks-automation** (`composio-skills/googletasks-automation`) — Automate Google Tasks via Rube MCP (Composio): create, list, update, delete, move, and bulk-insert t
- **Gorgias Automation** (`composio-skills/gorgias-automation`) — Automate e-commerce customer support workflows in Gorgias -- manage tickets, customers, tags, and te
- **gosquared-automation** (`composio-skills/gosquared-automation`) — Automate Gosquared tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **grafbase-automation** (`composio-skills/grafbase-automation`) — Automate Grafbase tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **graphhopper-automation** (`composio-skills/graphhopper-automation`) — Automate Graphhopper tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **griptape-automation** (`composio-skills/griptape-automation`) — Automate Griptape tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **grist-automation** (`composio-skills/grist-automation`) — Automate Grist tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **GroqCloud Automation** (`composio-skills/groqcloud-automation`) — Automate AI inference, chat completions, audio translation, and TTS voice management through GroqClo
- **Gumroad Automation** (`composio-skills/gumroad-automation`) — Automate Gumroad product management, sales tracking, license verification, and webhook subscriptions
- **habitica-automation** (`composio-skills/habitica-automation`) — Automate Habitica tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **hackernews-automation** (`composio-skills/hackernews-automation`) — Automate Hackernews tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **happy-scribe-automation** (`composio-skills/happy-scribe-automation`) — Automate Happy Scribe tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Harvest Automation** (`composio-skills/harvest-automation`) — Automate time tracking, project management, and invoicing workflows in Harvest -- log hours, manage 
- **hashnode-automation** (`composio-skills/hashnode-automation`) — Automate Hashnode tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **helcim-automation** (`composio-skills/helcim-automation`) — Automate Helcim tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **helloleads-automation** (`composio-skills/helloleads-automation`) — Automate Helloleads tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **helpwise-automation** (`composio-skills/helpwise-automation`) — Automate Helpwise tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **here-automation** (`composio-skills/here-automation`) — Automate Here tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **HeyGen Automation** (`composio-skills/heygen-automation`) — Automate AI video generation, avatar browsing, template-based video creation, and video status track
- **heyreach-automation** (`composio-skills/heyreach-automation`) — Automate Heyreach tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **heyzine-automation** (`composio-skills/heyzine-automation`) — Automate Heyzine tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **highergov-automation** (`composio-skills/highergov-automation`) — Automate Highergov tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **highlevel-automation** (`composio-skills/highlevel-automation`) — Automate Highlevel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **honeybadger-automation** (`composio-skills/honeybadger-automation`) — Automate Honeybadger tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **honeyhive-automation** (`composio-skills/honeyhive-automation`) — Automate Honeyhive tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **hookdeck-automation** (`composio-skills/hookdeck-automation`) — Automate Hookdeck tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **hotspotsystem-automation** (`composio-skills/hotspotsystem-automation`) — Automate Hotspotsystem tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **html-to-image-automation** (`composio-skills/html-to-image-automation`) — Automate Html To Image tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **humanitix-automation** (`composio-skills/humanitix-automation`) — Automate Humanitix tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **humanloop-automation** (`composio-skills/humanloop-automation`) — Automate Humanloop tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Hunter Automation** (`composio-skills/hunter-automation`) — Automate Hunter.io email intelligence -- search domains for email addresses, find specific contacts,
- **hypeauditor-automation** (`composio-skills/hypeauditor-automation`) — Automate Hypeauditor tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **hyperbrowser-automation** (`composio-skills/hyperbrowser-automation`) — Automate Hyperbrowser tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **hyperise-automation** (`composio-skills/hyperise-automation`) — Automate Hyperise tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **hystruct-automation** (`composio-skills/hystruct-automation`) — Automate Hystruct tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **icims-talent-cloud-automation** (`composio-skills/icims-talent-cloud-automation`) — Automate Icims Talent Cloud tasks via Rube MCP (Composio). Always search tools first for current sch
- **icypeas-automation** (`composio-skills/icypeas-automation`) — Automate Icypeas tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **idea-scale-automation** (`composio-skills/idea-scale-automation`) — Automate Idea Scale tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **identitycheck-automation** (`composio-skills/identitycheck-automation`) — Automate Identitycheck tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ignisign-automation** (`composio-skills/ignisign-automation`) — Automate Ignisign tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **imagekit-io-automation** (`composio-skills/imagekit-io-automation`) — Automate Imagekit IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **imgbb-automation** (`composio-skills/imgbb-automation`) — Automate Imgbb tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **imgix-automation** (`composio-skills/imgix-automation`) — Automate Imgix tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **influxdb-cloud-automation** (`composio-skills/influxdb-cloud-automation`) — Automate Influxdb Cloud tasks via Rube MCP (Composio). Always search tools first for current schemas
- **insighto-ai-automation** (`composio-skills/insighto-ai-automation`) — Automate Insighto AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **instacart-automation** (`composio-skills/instacart-automation`) — Automate Instacart tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Instantly Automation** (`composio-skills/instantly-automation`) — Automate Instantly cold email outreach -- manage campaigns, sending accounts, lead lists, bulk lead 
- **intelliprint-automation** (`composio-skills/intelliprint-automation`) — Automate Intelliprint tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **interzoid-automation** (`composio-skills/interzoid-automation`) — Automate Interzoid tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ip2location-automation** (`composio-skills/ip2location-automation`) — Automate Ip2location tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ip2location-io-automation** (`composio-skills/ip2location-io-automation`) — Automate Ip2location IO tasks via Rube MCP (Composio). Always search tools first for current schemas
- **ip2proxy-automation** (`composio-skills/ip2proxy-automation`) — Automate Ip2proxy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ip2whois-automation** (`composio-skills/ip2whois-automation`) — Automate Ip2whois tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ipdata-co-automation** (`composio-skills/ipdata-co-automation`) — Automate Ipdata co tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ipinfo-io-automation** (`composio-skills/ipinfo-io-automation`) — Automate Ipinfo IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **iqair-airvisual-automation** (`composio-skills/iqair-airvisual-automation`) — Automate Iqair Airvisual tasks via Rube MCP (Composio). Always search tools first for current schema
- **jigsawstack-automation** (`composio-skills/jigsawstack-automation`) — Automate Jigsawstack tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **jobnimbus-automation** (`composio-skills/jobnimbus-automation`) — Automate Jobnimbus tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Jotform Automation** (`composio-skills/jotform-automation`) — Automate Jotform form listing, user management, activity history, folder organization, and plan insp
- **jumpcloud-automation** (`composio-skills/jumpcloud-automation`) — Automate Jumpcloud tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **junglescout-automation** (`composio-skills/junglescout-automation`) — Automate Junglescout tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **kadoa-automation** (`composio-skills/kadoa-automation`) — Automate Kadoa tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **kaggle-automation** (`composio-skills/kaggle-automation`) — Automate Kaggle tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **kaleido-automation** (`composio-skills/kaleido-automation`) — Automate Kaleido tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **keap-automation** (`composio-skills/keap-automation`) — Automate Keap tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **keen-io-automation** (`composio-skills/keen-io-automation`) — Automate Keen IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **kickbox-automation** (`composio-skills/kickbox-automation`) — Automate Kickbox tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **kit-automation** (`composio-skills/kit-automation`) — Automate Kit tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **klipfolio-automation** (`composio-skills/klipfolio-automation`) — Automate Klipfolio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ko-fi-automation** (`composio-skills/ko-fi-automation`) — Automate Ko Fi tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Kommo Automation** (`composio-skills/kommo-automation`) — Automate Kommo CRM operations -- manage leads, pipelines, pipeline stages, tasks, and custom fields 
- **kontent-ai-automation** (`composio-skills/kontent-ai-automation`) — Automate Kontent AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **kraken-io-automation** (`composio-skills/kraken-io-automation`) — Automate Kraken IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **l2s-automation** (`composio-skills/l2s-automation`) — Automate L2s tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **labs64-netlicensing-automation** (`composio-skills/labs64-netlicensing-automation`) — Automate Labs64 Netlicensing tasks via Rube MCP (Composio). Always search tools first for current sc
- **landbot-automation** (`composio-skills/landbot-automation`) — Automate Landbot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **langbase-automation** (`composio-skills/langbase-automation`) — Automate Langbase tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **lastpass-automation** (`composio-skills/lastpass-automation`) — Automate Lastpass tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **LaunchDarkly Automation** (`composio-skills/launch-darkly-automation`) — Automate LaunchDarkly feature flag management -- list projects and environments, create and delete t
- **launch_darkly-automation** (`composio-skills/launch_darkly-automation`) — Automate LaunchDarkly tasks via Rube MCP (Composio): feature flags, environments, segments, and roll
- **leadfeeder-automation** (`composio-skills/leadfeeder-automation`) — Automate Leadfeeder tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **leadoku-automation** (`composio-skills/leadoku-automation`) — Automate Leadoku tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **leiga-automation** (`composio-skills/leiga-automation`) — Automate Leiga tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Lemlist Automation** (`composio-skills/lemlist-automation`) — Automate Lemlist multichannel outreach -- manage campaigns, enroll leads, add personalization variab
- **Lemon Squeezy Automation** (`composio-skills/lemon-squeezy-automation`) — Automate Lemon Squeezy store management -- products, orders, subscriptions, customers, discounts, an
- **lemon_squeezy-automation** (`composio-skills/lemon_squeezy-automation`) — Automate Lemon Squeezy tasks via Rube MCP (Composio): products, orders, subscriptions, checkouts, an
- **lessonspace-automation** (`composio-skills/lessonspace-automation`) — Automate Lessonspace tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Lever Automation** (`composio-skills/lever-automation`) — Automate recruiting workflows in Lever ATS -- manage opportunities, job postings, requisitions, pipe
- **lever-sandbox-automation** (`composio-skills/lever-sandbox-automation`) — Automate Lever Sandbox tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **leverly-automation** (`composio-skills/leverly-automation`) — Automate Leverly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **lexoffice-automation** (`composio-skills/lexoffice-automation`) — Automate Lexoffice tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **linguapop-automation** (`composio-skills/linguapop-automation`) — Automate Linguapop tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **linkhut-automation** (`composio-skills/linkhut-automation`) — Automate Linkhut tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **linkup-automation** (`composio-skills/linkup-automation`) — Automate Linkup tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **listclean-automation** (`composio-skills/listclean-automation`) — Automate Listclean tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **listennotes-automation** (`composio-skills/listennotes-automation`) — Automate Listennotes tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **livesession-automation** (`composio-skills/livesession-automation`) — Automate Livesession tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **lmnt-automation** (`composio-skills/lmnt-automation`) — Automate Lmnt tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **lodgify-automation** (`composio-skills/lodgify-automation`) — Automate Lodgify tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **logo-dev-automation** (`composio-skills/logo-dev-automation`) — Automate Logo Dev tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **loomio-automation** (`composio-skills/loomio-automation`) — Automate Loomio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **loyverse-automation** (`composio-skills/loyverse-automation`) — Automate Loyverse tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **magnetic-automation** (`composio-skills/magnetic-automation`) — Automate Magnetic tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mailbluster-automation** (`composio-skills/mailbluster-automation`) — Automate Mailbluster tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mailboxlayer-automation** (`composio-skills/mailboxlayer-automation`) — Automate Mailboxlayer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mailcheck-automation** (`composio-skills/mailcheck-automation`) — Automate Mailcheck tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mailcoach-automation** (`composio-skills/mailcoach-automation`) — Automate Mailcoach tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **MailerLite Automation** (`composio-skills/mailerlite-automation`) — Automate email marketing workflows including subscriber management, campaign analytics, group segmen
- **mailersend-automation** (`composio-skills/mailersend-automation`) — Automate Mailersend tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mails-so-automation** (`composio-skills/mails-so-automation`) — Automate Mails So tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mailsoftly-automation** (`composio-skills/mailsoftly-automation`) — Automate Mailsoftly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **maintainx-automation** (`composio-skills/maintainx-automation`) — Automate Maintainx tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **many-chat-automation** (`composio-skills/many-chat-automation`) — Automate ManyChat tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **many_chat-automation** (`composio-skills/many_chat-automation`) — Automate ManyChat tasks via Rube MCP (Composio): chatbot flows, subscribers, broadcasts, and messeng
- **mapbox-automation** (`composio-skills/mapbox-automation`) — Automate Mapbox tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mapulus-automation** (`composio-skills/mapulus-automation`) — Automate Mapulus tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mboum-automation** (`composio-skills/mboum-automation`) — Automate Mboum tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **melo-automation** (`composio-skills/melo-automation`) — Automate Melo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mem-automation** (`composio-skills/mem-automation`) — Automate Mem tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mem0-automation** (`composio-skills/mem0-automation`) — Automate Mem0 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **memberspot-automation** (`composio-skills/memberspot-automation`) — Automate Memberspot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **memberstack-automation** (`composio-skills/memberstack-automation`) — Automate Memberstack tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **membervault-automation** (`composio-skills/membervault-automation`) — Automate Membervault tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **metaads-automation** (`composio-skills/metaads-automation`) — Automate Metaads tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **metaphor-automation** (`composio-skills/metaphor-automation`) — Automate Metaphor tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mezmo-automation** (`composio-skills/mezmo-automation`) — Automate Mezmo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Microsoft Clarity Automation** (`composio-skills/microsoft-clarity-automation`) — Automate user behavior analytics with Microsoft Clarity -- export heatmap data, session metrics, and
- **microsoft-tenant-automation** (`composio-skills/microsoft-tenant-automation`) — Automate Microsoft Tenant tasks via Rube MCP (Composio). Always search tools first for current schem
- **microsoft_clarity-automation** (`composio-skills/microsoft_clarity-automation`) — Automate Microsoft Clarity tasks via Rube MCP (Composio): session recordings, heatmaps, and user beh
- **minerstat-automation** (`composio-skills/minerstat-automation`) — Automate Minerstat tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **missive-automation** (`composio-skills/missive-automation`) — Automate Missive tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Mistral AI Automation** (`composio-skills/mistral-ai-automation`) — Automate Mistral AI operations -- manage files and libraries, upload documents for fine-tuning, batc
- **mistral_ai-automation** (`composio-skills/mistral_ai-automation`) — Automate Mistral AI tasks via Rube MCP (Composio): completions, embeddings, fine-tuning, and model m
- **mocean-automation** (`composio-skills/mocean-automation`) — Automate Mocean tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **moco-automation** (`composio-skills/moco-automation`) — Automate Moco tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **modelry-automation** (`composio-skills/modelry-automation`) — Automate Modelry tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **moneybird-automation** (`composio-skills/moneybird-automation`) — Automate Moneybird tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **moonclerk-automation** (`composio-skills/moonclerk-automation`) — Automate Moonclerk tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **moosend-automation** (`composio-skills/moosend-automation`) — Automate Moosend tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mopinion-automation** (`composio-skills/mopinion-automation`) — Automate Mopinion tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **more-trees-automation** (`composio-skills/more-trees-automation`) — Automate More Trees tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **moxie-automation** (`composio-skills/moxie-automation`) — Automate Moxie tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **moz-automation** (`composio-skills/moz-automation`) — Automate Moz tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **msg91-automation** (`composio-skills/msg91-automation`) — Automate Msg91 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mural-automation** (`composio-skills/mural-automation`) — Automate Mural tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **mx-technologies-automation** (`composio-skills/mx-technologies-automation`) — Automate MX Technologies tasks via Rube MCP (Composio). Always search tools first for current schema
- **mx-toolbox-automation** (`composio-skills/mx-toolbox-automation`) — Automate Mx Toolbox tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **nango-automation** (`composio-skills/nango-automation`) — Automate Nango tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **nano-nets-automation** (`composio-skills/nano-nets-automation`) — Automate Nano Nets tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **nasa-automation** (`composio-skills/nasa-automation`) — Automate Nasa tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **nasdaq-automation** (`composio-skills/nasdaq-automation`) — Automate Nasdaq tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ncscale-automation** (`composio-skills/ncscale-automation`) — Automate Ncscale tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **needle-automation** (`composio-skills/needle-automation`) — Automate Needle tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Neon Automation** (`composio-skills/neon-automation`) — Automate Neon serverless Postgres operations -- manage projects, branches, databases, roles, and con
- **NetSuite Automation** (`composio-skills/netsuite-automation`) — NetSuite Automation: manage customers, sales orders, invoices, inventory, and records via Oracle Net
- **neuronwriter-automation** (`composio-skills/neuronwriter-automation`) — Automate Neuronwriter tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **neutrino-automation** (`composio-skills/neutrino-automation`) — Automate Neutrino tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **neverbounce-automation** (`composio-skills/neverbounce-automation`) — Automate Neverbounce tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **New Relic Automation** (`composio-skills/new-relic-automation`) — Automate New Relic observability workflows -- manage alert policies, notification channels, alert co
- **new_relic-automation** (`composio-skills/new_relic-automation`) — Automate New Relic tasks via Rube MCP (Composio): APM, alerts, dashboards, NRQL queries, and infrast
- **news-api-automation** (`composio-skills/news-api-automation`) — Automate News API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **nextdns-automation** (`composio-skills/nextdns-automation`) — Automate Nextdns tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ngrok-automation** (`composio-skills/ngrok-automation`) — Automate Ngrok tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ninox-automation** (`composio-skills/ninox-automation`) — Automate Ninox tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **nocrm-io-automation** (`composio-skills/nocrm-io-automation`) — Automate Nocrm IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **npm-automation** (`composio-skills/npm-automation`) — Automate NPM tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ocr-web-service-automation** (`composio-skills/ocr-web-service-automation`) — Automate OCR Web Service tasks via Rube MCP (Composio). Always search tools first for current schema
- **ocrspace-automation** (`composio-skills/ocrspace-automation`) — Automate Ocrspace tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Omnisend Automation** (`composio-skills/omnisend-automation`) — Automate ecommerce marketing workflows including contact management, bulk operations, and subscriber
- **oncehub-automation** (`composio-skills/oncehub-automation`) — Automate Oncehub tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **onedesk-automation** (`composio-skills/onedesk-automation`) — Automate Onedesk tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **onepage-automation** (`composio-skills/onepage-automation`) — Automate Onepage tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **onesignal-rest-api-automation** (`composio-skills/onesignal-rest-api-automation`) — Automate OneSignal tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **onesignal-user-auth-automation** (`composio-skills/onesignal-user-auth-automation`) — Automate Onesignal User Auth tasks via Rube MCP (Composio). Always search tools first for current sc
- **onesignal_rest_api-automation** (`composio-skills/onesignal_rest_api-automation`) — Automate OneSignal tasks via Rube MCP (Composio): push notifications, segments, templates, and messa
- **open-sea-automation** (`composio-skills/open-sea-automation`) — Automate Open Sea tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **OpenAI Automation** (`composio-skills/openai-automation`) — Automate OpenAI API operations -- generate responses with multimodal and structured output support, 
- **opencage-automation** (`composio-skills/opencage-automation`) — Automate Opencage tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **opengraph-io-automation** (`composio-skills/opengraph-io-automation`) — Automate Opengraph IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **openperplex-automation** (`composio-skills/openperplex-automation`) — Automate Openperplex tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **openrouter-automation** (`composio-skills/openrouter-automation`) — Automate Openrouter tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **openweather-api-automation** (`composio-skills/openweather-api-automation`) — Automate Openweather API tasks via Rube MCP (Composio). Always search tools first for current schema
- **optimoroute-automation** (`composio-skills/optimoroute-automation`) — Automate Optimoroute tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **owl-protocol-automation** (`composio-skills/owl-protocol-automation`) — Automate Owl Protocol tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **page-x-automation** (`composio-skills/page-x-automation`) — Automate Page X tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **PandaDoc Automation** (`composio-skills/pandadoc-automation`) — Automate document workflows with PandaDoc -- create documents from files, manage contacts, organize 
- **paradym-automation** (`composio-skills/paradym-automation`) — Automate Paradym tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **parallel-automation** (`composio-skills/parallel-automation`) — Automate Parallel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **parma-automation** (`composio-skills/parma-automation`) — Automate Parma tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **parsehub-automation** (`composio-skills/parsehub-automation`) — Automate Parsehub tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **parsera-automation** (`composio-skills/parsera-automation`) — Automate Parsera tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **parseur-automation** (`composio-skills/parseur-automation`) — Automate Parseur tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **passcreator-automation** (`composio-skills/passcreator-automation`) — Automate Passcreator tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **passslot-automation** (`composio-skills/passslot-automation`) — Automate Passslot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **payhip-automation** (`composio-skills/payhip-automation`) — Automate Payhip tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pdf-api-io-automation** (`composio-skills/pdf-api-io-automation`) — Automate PDF API IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pdf-co-automation** (`composio-skills/pdf-co-automation`) — Automate PDF co tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pdf4me-automation** (`composio-skills/pdf4me-automation`) — Automate Pdf4me tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pdfless-automation** (`composio-skills/pdfless-automation`) — Automate Pdfless tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pdfmonkey-automation** (`composio-skills/pdfmonkey-automation`) — Automate Pdfmonkey tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **peopledatalabs-automation** (`composio-skills/peopledatalabs-automation`) — Automate Peopledatalabs tasks via Rube MCP (Composio). Always search tools first for current schemas
- **perigon-automation** (`composio-skills/perigon-automation`) — Automate Perigon tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **perplexityai-automation** (`composio-skills/perplexityai-automation`) — Automate Perplexityai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **persistiq-automation** (`composio-skills/persistiq-automation`) — Automate Persistiq tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pexels-automation** (`composio-skills/pexels-automation`) — Automate Pexels tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **PhantomBuster Automation** (`composio-skills/phantombuster-automation`) — Automate lead generation, web scraping, and social media data extraction workflows through PhantomBu
- **piggy-automation** (`composio-skills/piggy-automation`) — Automate Piggy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **piloterr-automation** (`composio-skills/piloterr-automation`) — Automate Piloterr tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pilvio-automation** (`composio-skills/pilvio-automation`) — Automate Pilvio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pingdom-automation** (`composio-skills/pingdom-automation`) — Automate Pingdom tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pipeline-crm-automation** (`composio-skills/pipeline-crm-automation`) — Automate Pipeline CRM tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **placekey-automation** (`composio-skills/placekey-automation`) — Automate Placekey tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **placid-automation** (`composio-skills/placid-automation`) — Automate Placid tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **plain-automation** (`composio-skills/plain-automation`) — Automate Plain tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **plasmic-automation** (`composio-skills/plasmic-automation`) — Automate Plasmic tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **platerecognizer-automation** (`composio-skills/platerecognizer-automation`) — Automate Platerecognizer tasks via Rube MCP (Composio). Always search tools first for current schema
- **plisio-automation** (`composio-skills/plisio-automation`) — Automate Plisio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **polygon-automation** (`composio-skills/polygon-automation`) — Automate Polygon tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **polygon-io-automation** (`composio-skills/polygon-io-automation`) — Automate Polygon IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **poptin-automation** (`composio-skills/poptin-automation`) — Automate Poptin tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **postgrid-automation** (`composio-skills/postgrid-automation`) — Automate Postgrid tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **postgrid-verify-automation** (`composio-skills/postgrid-verify-automation`) — Automate Postgrid Verify tasks via Rube MCP (Composio). Always search tools first for current schema
- **precoro-automation** (`composio-skills/precoro-automation`) — Automate Precoro tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **prerender-automation** (`composio-skills/prerender-automation`) — Automate Prerender tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **printautopilot-automation** (`composio-skills/printautopilot-automation`) — Automate Printautopilot tasks via Rube MCP (Composio). Always search tools first for current schemas
- **prisma-automation** (`composio-skills/prisma-automation`) — Automate Prisma tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Prismic Automation** (`composio-skills/prismic-automation`) — Automate headless CMS operations in Prismic -- query documents, search content, retrieve custom type
- **process-street-automation** (`composio-skills/process-street-automation`) — Automate Process Street tasks via Rube MCP (Composio). Always search tools first for current schemas
- **procfu-automation** (`composio-skills/procfu-automation`) — Automate Procfu tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Productboard Automation** (`composio-skills/productboard-automation`) — Automate product management workflows in Productboard -- manage features, notes, objectives, compone
- **productlane-automation** (`composio-skills/productlane-automation`) — Automate Productlane tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **project-bubble-automation** (`composio-skills/project-bubble-automation`) — Automate Project Bubble tasks via Rube MCP (Composio). Always search tools first for current schemas
- **proofly-automation** (`composio-skills/proofly-automation`) — Automate Proofly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **proxiedmail-automation** (`composio-skills/proxiedmail-automation`) — Automate Proxiedmail tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pushbullet-automation** (`composio-skills/pushbullet-automation`) — Automate Pushbullet tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **pushover-automation** (`composio-skills/pushover-automation`) — Automate Pushover tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **quaderno-automation** (`composio-skills/quaderno-automation`) — Automate Quaderno tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **qualaroo-automation** (`composio-skills/qualaroo-automation`) — Automate Qualaroo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **QuickBooks Automation** (`composio-skills/quickbooks-automation`) — QuickBooks Automation: manage invoices, customers, accounts, and payments in QuickBooks Online for s
- **radar-automation** (`composio-skills/radar-automation`) — Automate Radar tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **rafflys-automation** (`composio-skills/rafflys-automation`) — Automate Rafflys tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ragic-automation** (`composio-skills/ragic-automation`) — Automate Ragic tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **raisely-automation** (`composio-skills/raisely-automation`) — Automate Raisely tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Ramp Automation** (`composio-skills/ramp-automation`) — Ramp Automation: manage corporate card transactions, reimbursements, users, and expense tracking via
- **ravenseotools-automation** (`composio-skills/ravenseotools-automation`) — Automate Ravenseotools tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **re-amaze-automation** (`composio-skills/re-amaze-automation`) — Automate Re Amaze tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **realphonevalidation-automation** (`composio-skills/realphonevalidation-automation`) — Automate Realphonevalidation tasks via Rube MCP (Composio). Always search tools first for current sc
- **recallai-automation** (`composio-skills/recallai-automation`) — Automate Recallai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **recruitee-automation** (`composio-skills/recruitee-automation`) — Automate Recruitee tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **refiner-automation** (`composio-skills/refiner-automation`) — Automate Refiner tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **remarkety-automation** (`composio-skills/remarkety-automation`) — Automate Remarkety tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **remote-retrieval-automation** (`composio-skills/remote-retrieval-automation`) — Automate Remote Retrieval tasks via Rube MCP (Composio). Always search tools first for current schem
- **remove-bg-automation** (`composio-skills/remove-bg-automation`) — Automate Remove Bg tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **renderform-automation** (`composio-skills/renderform-automation`) — Automate Renderform tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **repairshopr-automation** (`composio-skills/repairshopr-automation`) — Automate Repairshopr tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Replicate Automation** (`composio-skills/replicate-automation`) — Automate Replicate AI model operations -- run predictions, upload files, inspect model schemas, list
- **reply-automation** (`composio-skills/reply-automation`) — Automate Reply tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **reply-io-automation** (`composio-skills/reply-io-automation`) — Automate Reply IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **resend-automation** (`composio-skills/resend-automation`) — Automate Resend tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **respond-io-automation** (`composio-skills/respond-io-automation`) — Automate Respond IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **retailed-automation** (`composio-skills/retailed-automation`) — Automate Retailed tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **retellai-automation** (`composio-skills/retellai-automation`) — Automate Retellai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **retently-automation** (`composio-skills/retently-automation`) — Automate Retently tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **rev-ai-automation** (`composio-skills/rev-ai-automation`) — Automate Rev AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **revolt-automation** (`composio-skills/revolt-automation`) — Automate Revolt tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **RingCentral Automation** (`composio-skills/ring-central-automation`) — RingCentral automation via Rube MCP -- toolkit not currently available in Composio; no RING_CENTRAL_
- **ring_central-automation** (`composio-skills/ring_central-automation`) — Automate RingCentral tasks via Rube MCP (Composio): calls, messages, meetings, and unified communica
- **rippling-automation** (`composio-skills/rippling-automation`) — Automate Rippling tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ritekit-automation** (`composio-skills/ritekit-automation`) — Automate Ritekit tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **rkvst-automation** (`composio-skills/rkvst-automation`) — Automate Rkvst tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **rocketlane-automation** (`composio-skills/rocketlane-automation`) — Automate Rocketlane tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **rootly-automation** (`composio-skills/rootly-automation`) — Automate Rootly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **rosette-text-analytics-automation** (`composio-skills/rosette-text-analytics-automation`) — Automate Rosette Text Analytics tasks via Rube MCP (Composio). Always search tools first for current
- **route4me-automation** (`composio-skills/route4me-automation`) — Automate Route4me tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **safetyculture-automation** (`composio-skills/safetyculture-automation`) — Automate Safetyculture tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sage-automation** (`composio-skills/sage-automation`) — Automate Sage tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **salesforce-marketing-cloud-automation** (`composio-skills/salesforce-marketing-cloud-automation`) — Automate Salesforce Marketing Cloud tasks via Rube MCP (Composio). Always search tools first for cur
- **salesforce-service-cloud-automation** (`composio-skills/salesforce-service-cloud-automation`) — Automate Salesforce Service Cloud tasks via Rube MCP (Composio). Always search tools first for curre
- **salesmate-automation** (`composio-skills/salesmate-automation`) — Automate Salesmate tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sap-successfactors-automation** (`composio-skills/sap-successfactors-automation`) — Automate SAP SuccessFactors tasks via Rube MCP (Composio). Always search tools first for current sch
- **satismeter-automation** (`composio-skills/satismeter-automation`) — Automate Satismeter tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **scrape-do-automation** (`composio-skills/scrape-do-automation`) — Automate Scrape Do tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **scrapegraph-ai-automation** (`composio-skills/scrapegraph-ai-automation`) — Automate Scrapegraph AI tasks via Rube MCP (Composio). Always search tools first for current schemas
- **scrapfly-automation** (`composio-skills/scrapfly-automation`) — Automate Scrapfly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **scrapingant-automation** (`composio-skills/scrapingant-automation`) — Automate Scrapingant tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **scrapingbee-automation** (`composio-skills/scrapingbee-automation`) — Automate Scrapingbee tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **screenshot-fyi-automation** (`composio-skills/screenshot-fyi-automation`) — Automate Screenshot Fyi tasks via Rube MCP (Composio). Always search tools first for current schemas
- **screenshotone-automation** (`composio-skills/screenshotone-automation`) — Automate Screenshotone tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **seat-geek-automation** (`composio-skills/seat-geek-automation`) — Automate Seat Geek tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **securitytrails-automation** (`composio-skills/securitytrails-automation`) — Automate Securitytrails tasks via Rube MCP (Composio). Always search tools first for current schemas
- **segmetrics-automation** (`composio-skills/segmetrics-automation`) — Automate Segmetrics tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **seismic-automation** (`composio-skills/seismic-automation`) — Automate Seismic tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **semanticscholar-automation** (`composio-skills/semanticscholar-automation`) — Automate Semanticscholar tasks via Rube MCP (Composio). Always search tools first for current schema
- **SEMrush Automation** (`composio-skills/semrush-automation`) — Automate SEO analysis with SEMrush -- research keywords, analyze domain organic rankings, audit back
- **sendbird-ai-chabot-automation** (`composio-skills/sendbird-ai-chabot-automation`) — Automate Sendbird AI Chabot tasks via Rube MCP (Composio). Always search tools first for current sch
- **sendbird-automation** (`composio-skills/sendbird-automation`) — Automate Sendbird tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sendfox-automation** (`composio-skills/sendfox-automation`) — Automate Sendfox tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sendlane-automation** (`composio-skills/sendlane-automation`) — Automate Sendlane tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sendloop-automation** (`composio-skills/sendloop-automation`) — Automate Sendloop tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sendspark-automation** (`composio-skills/sendspark-automation`) — Automate Sendspark tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sensibo-automation** (`composio-skills/sensibo-automation`) — Automate Sensibo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **seqera-automation** (`composio-skills/seqera-automation`) — Automate Seqera tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **serpapi-automation** (`composio-skills/serpapi-automation`) — Automate Serpapi tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **serpdog-automation** (`composio-skills/serpdog-automation`) — Automate Serpdog tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **serply-automation** (`composio-skills/serply-automation`) — Automate Serply tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **servicem8-automation** (`composio-skills/servicem8-automation`) — Automate Servicem8 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sevdesk-automation** (`composio-skills/sevdesk-automation`) — Automate Sevdesk tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **SharePoint Automation** (`composio-skills/share-point-automation`) — SharePoint Automation: manage sites, lists, documents, folders, pages, and search content across Sha
- **share_point-automation** (`composio-skills/share_point-automation`) — Automate SharePoint tasks via Rube MCP (Composio): document libraries, sites, lists, and content man
- **shipengine-automation** (`composio-skills/shipengine-automation`) — Automate Shipengine tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **short-io-automation** (`composio-skills/short-io-automation`) — Automate Short IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **short-menu-automation** (`composio-skills/short-menu-automation`) — Automate Short Menu tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Shortcut Automation** (`composio-skills/shortcut-automation`) — Automate project management workflows in Shortcut -- create stories, manage tasks, track epics, and 
- **shorten-rest-automation** (`composio-skills/shorten-rest-automation`) — Automate Shorten Rest tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **shortpixel-automation** (`composio-skills/shortpixel-automation`) — Automate Shortpixel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **shotstack-automation** (`composio-skills/shotstack-automation`) — Automate Shotstack tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sidetracker-automation** (`composio-skills/sidetracker-automation`) — Automate Sidetracker tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **signaturely-automation** (`composio-skills/signaturely-automation`) — Automate Signaturely tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **signpath-automation** (`composio-skills/signpath-automation`) — Automate Signpath tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **signwell-automation** (`composio-skills/signwell-automation`) — Automate Signwell tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **similarweb-digitalrank-api-automation** (`composio-skills/similarweb-digitalrank-api-automation`) — Automate SimilarWeb tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **similarweb_digitalrank_api-automation** (`composio-skills/similarweb_digitalrank_api-automation`) — Automate SimilarWeb tasks via Rube MCP (Composio): website traffic, rankings, and digital market int
- **simla-com-automation** (`composio-skills/simla-com-automation`) — Automate Simla Com tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **simple-analytics-automation** (`composio-skills/simple-analytics-automation`) — Automate Simple Analytics tasks via Rube MCP (Composio). Always search tools first for current schem
- **simplesat-automation** (`composio-skills/simplesat-automation`) — Automate Simplesat tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sitespeakai-automation** (`composio-skills/sitespeakai-automation`) — Automate Sitespeakai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **skyfire-automation** (`composio-skills/skyfire-automation`) — Automate Skyfire tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **slackbot-automation** (`composio-skills/slackbot-automation`) — Automate Slackbot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **smartproxy-automation** (`composio-skills/smartproxy-automation`) — Automate Smartproxy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **smartrecruiters-automation** (`composio-skills/smartrecruiters-automation`) — Automate Smartrecruiters tasks via Rube MCP (Composio). Always search tools first for current schema
- **sms-alert-automation** (`composio-skills/sms-alert-automation`) — Automate SMS Alert tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **smtp2go-automation** (`composio-skills/smtp2go-automation`) — Automate Smtp2go tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **smugmug-automation** (`composio-skills/smugmug-automation`) — Automate Smugmug tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Snowflake Automation** (`composio-skills/snowflake-automation`) — Automate Snowflake data warehouse operations -- list databases, schemas, and tables, execute SQL sta
- **sourcegraph-automation** (`composio-skills/sourcegraph-automation`) — Automate Sourcegraph tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **splitwise-automation** (`composio-skills/splitwise-automation`) — Automate Splitwise tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **spoki-automation** (`composio-skills/spoki-automation`) — Automate Spoki tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **spondyr-automation** (`composio-skills/spondyr-automation`) — Automate Spondyr tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Spotify Automation** (`composio-skills/spotify-automation`) — Automate Spotify workflows including playlist management, music search, playback control, and user p
- **spotlightr-automation** (`composio-skills/spotlightr-automation`) — Automate Spotlightr tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sslmate-cert-spotter-api-automation** (`composio-skills/sslmate-cert-spotter-api-automation`) — Automate Sslmate Cert Spotter API tasks via Rube MCP (Composio). Always search tools first for curre
- **stack-exchange-automation** (`composio-skills/stack-exchange-automation`) — Automate Stack Exchange tasks via Rube MCP (Composio). Always search tools first for current schemas
- **stannp-automation** (`composio-skills/stannp-automation`) — Automate Stannp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **starton-automation** (`composio-skills/starton-automation`) — Automate Starton tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **statuscake-automation** (`composio-skills/statuscake-automation`) — Automate Statuscake tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **storeganise-automation** (`composio-skills/storeganise-automation`) — Automate Storeganise tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **storerocket-automation** (`composio-skills/storerocket-automation`) — Automate Storerocket tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **stormglass-io-automation** (`composio-skills/stormglass-io-automation`) — Automate Stormglass IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **strava-automation** (`composio-skills/strava-automation`) — Automate Strava tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **streamtime-automation** (`composio-skills/streamtime-automation`) — Automate Streamtime tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **supadata-automation** (`composio-skills/supadata-automation`) — Automate Supadata tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **superchat-automation** (`composio-skills/superchat-automation`) — Automate Superchat tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **supportbee-automation** (`composio-skills/supportbee-automation`) — Automate Supportbee tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **supportivekoala-automation** (`composio-skills/supportivekoala-automation`) — Automate Supportivekoala tasks via Rube MCP (Composio). Always search tools first for current schema
- **SurveyMonkey Automation** (`composio-skills/survey-monkey-automation`) — Automate SurveyMonkey survey creation, response collection, collector management, and survey discove
- **survey_monkey-automation** (`composio-skills/survey_monkey-automation`) — Automate SurveyMonkey tasks via Rube MCP (Composio): surveys, responses, collectors, and survey anal
- **svix-automation** (`composio-skills/svix-automation`) — Automate Svix tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **sympla-automation** (`composio-skills/sympla-automation`) — Automate Sympla tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **synthflow-ai-automation** (`composio-skills/synthflow-ai-automation`) — Automate Synthflow AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **taggun-automation** (`composio-skills/taggun-automation`) — Automate Taggun tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **talenthr-automation** (`composio-skills/talenthr-automation`) — Automate Talenthr tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tally-automation** (`composio-skills/tally-automation`) — Automate Tally tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tapfiliate-automation** (`composio-skills/tapfiliate-automation`) — Automate Tapfiliate tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tapform-automation** (`composio-skills/tapform-automation`) — Automate Tapform tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tavily-automation** (`composio-skills/tavily-automation`) — Automate Tavily tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **taxjar-automation** (`composio-skills/taxjar-automation`) — Automate Taxjar tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **teamcamp-automation** (`composio-skills/teamcamp-automation`) — Automate Teamcamp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **telnyx-automation** (`composio-skills/telnyx-automation`) — Automate Telnyx tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **teltel-automation** (`composio-skills/teltel-automation`) — Automate Teltel tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **templated-automation** (`composio-skills/templated-automation`) — Automate Templated tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **test-app-automation** (`composio-skills/test-app-automation`) — Automate Test App tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **text-to-pdf-automation** (`composio-skills/text-to-pdf-automation`) — Automate Text To PDF tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **textcortex-automation** (`composio-skills/textcortex-automation`) — Automate Textcortex tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **textit-automation** (`composio-skills/textit-automation`) — Automate Textit tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **textrazor-automation** (`composio-skills/textrazor-automation`) — Automate Textrazor tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **thanks-io-automation** (`composio-skills/thanks-io-automation`) — Automate Thanks IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **the-odds-api-automation** (`composio-skills/the-odds-api-automation`) — Automate The Odds API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ticketmaster-automation** (`composio-skills/ticketmaster-automation`) — Automate Ticketmaster tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ticktick-automation** (`composio-skills/ticktick-automation`) — Automate Ticktick tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **timecamp-automation** (`composio-skills/timecamp-automation`) — Automate Timecamp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **timekit-automation** (`composio-skills/timekit-automation`) — Automate Timekit tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **timelinesai-automation** (`composio-skills/timelinesai-automation`) — Automate Timelinesai tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **timelink-automation** (`composio-skills/timelink-automation`) — Automate Timelink tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **timely-automation** (`composio-skills/timely-automation`) — Automate Timely tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tinyurl-automation** (`composio-skills/tinyurl-automation`) — Automate Tinyurl tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tisane-automation** (`composio-skills/tisane-automation`) — Automate Tisane tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Toggl Automation** (`composio-skills/toggl-automation`) — Automate time tracking workflows in Toggl Track -- create time entries, manage projects, clients, ta
- **token-metrics-automation** (`composio-skills/token-metrics-automation`) — Automate Token Metrics tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tomba-automation** (`composio-skills/tomba-automation`) — Automate Tomba tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tomtom-automation** (`composio-skills/tomtom-automation`) — Automate Tomtom tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **toneden-automation** (`composio-skills/toneden-automation`) — Automate Toneden tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tpscheck-automation** (`composio-skills/tpscheck-automation`) — Automate Tpscheck tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **triggercmd-automation** (`composio-skills/triggercmd-automation`) — Automate Triggercmd tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **tripadvisor-content-api-automation** (`composio-skills/tripadvisor-content-api-automation`) — Automate TripAdvisor tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **turbot-pipes-automation** (`composio-skills/turbot-pipes-automation`) — Automate Turbot Pipes tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **turso-automation** (`composio-skills/turso-automation`) — Automate Turso tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **twelve-data-automation** (`composio-skills/twelve-data-automation`) — Automate Twelve Data tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **twitch-automation** (`composio-skills/twitch-automation`) — Automate Twitch tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **twocaptcha-automation** (`composio-skills/twocaptcha-automation`) — Automate Twocaptcha tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **typefully-automation** (`composio-skills/typefully-automation`) — Automate Typefully tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **typless-automation** (`composio-skills/typless-automation`) — Automate Typless tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **u301-automation** (`composio-skills/u301-automation`) — Automate U301 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **unione-automation** (`composio-skills/unione-automation`) — Automate Unione tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **updown-io-automation** (`composio-skills/updown-io-automation`) — Automate Updown IO tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Uploadcare Automation** (`composio-skills/uploadcare-automation`) — Automate Uploadcare file management including listing, storing, inspecting, downloading, and organiz
- **uptimerobot-automation** (`composio-skills/uptimerobot-automation`) — Automate Uptimerobot tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **userlist-automation** (`composio-skills/userlist-automation`) — Automate Userlist tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **v0-automation** (`composio-skills/v0-automation`) — Automate V0 tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **venly-automation** (`composio-skills/venly-automation`) — Automate Venly tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **veo-automation** (`composio-skills/veo-automation`) — Automate Veo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **verifiedemail-automation** (`composio-skills/verifiedemail-automation`) — Automate Verifiedemail tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **veriphone-automation** (`composio-skills/veriphone-automation`) — Automate Veriphone tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **vero-automation** (`composio-skills/vero-automation`) — Automate Vero tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **vestaboard-automation** (`composio-skills/vestaboard-automation`) — Automate Vestaboard tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **virustotal-automation** (`composio-skills/virustotal-automation`) — Automate Virustotal tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **visme-automation** (`composio-skills/visme-automation`) — Automate Visme tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **waboxapp-automation** (`composio-skills/waboxapp-automation`) — Automate Waboxapp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **wachete-automation** (`composio-skills/wachete-automation`) — Automate Wachete tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **waiverfile-automation** (`composio-skills/waiverfile-automation`) — Automate Waiverfile tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **wakatime-automation** (`composio-skills/wakatime-automation`) — Automate Wakatime tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **wati-automation** (`composio-skills/wati-automation`) — Automate Wati tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Wave Accounting Automation** (`composio-skills/wave-accounting-automation`) — Wave Accounting toolkit is not currently available as a native integration. No Wave-specific tools w
- **wave_accounting-automation** (`composio-skills/wave_accounting-automation`) — Automate Wave Accounting tasks via Rube MCP (Composio): invoices, customers, payments, and small bus
- **weathermap-automation** (`composio-skills/weathermap-automation`) — Automate Weathermap tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Webex Automation** (`composio-skills/webex-automation`) — Automate Cisco Webex messaging, rooms, teams, webhooks, and people management through natural langua
- **webscraping-ai-automation** (`composio-skills/webscraping-ai-automation`) — Automate Webscraping AI tasks via Rube MCP (Composio). Always search tools first for current schemas
- **webvizio-automation** (`composio-skills/webvizio-automation`) — Automate Webvizio tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **whautomate-automation** (`composio-skills/whautomate-automation`) — Automate Whautomate tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **winston-ai-automation** (`composio-skills/winston-ai-automation`) — Automate Winston AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **wit-ai-automation** (`composio-skills/wit-ai-automation`) — Automate Wit AI tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **wiz-automation** (`composio-skills/wiz-automation`) — Automate Wiz tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **wolfram-alpha-api-automation** (`composio-skills/wolfram-alpha-api-automation`) — Automate Wolfram Alpha API tasks via Rube MCP (Composio). Always search tools first for current sche
- **woodpecker-co-automation** (`composio-skills/woodpecker-co-automation`) — Automate Woodpecker co tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **workable-automation** (`composio-skills/workable-automation`) — Automate Workable tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Workday Automation** (`composio-skills/workday-automation`) — Automate HR operations in Workday -- manage workers, time off requests, absence balances, and employ
- **workiom-automation** (`composio-skills/workiom-automation`) — Automate Workiom tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **worksnaps-automation** (`composio-skills/worksnaps-automation`) — Automate Worksnaps tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **writer-automation** (`composio-skills/writer-automation`) — Automate Writer tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Xero Automation** (`composio-skills/xero-automation`) — Xero Automation: manage invoices, contacts, payments, bank transactions, and accounts in Xero for cl
- **y-gy-automation** (`composio-skills/y-gy-automation`) — Automate Y Gy tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **yandex-automation** (`composio-skills/yandex-automation`) — Automate Yandex tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **yelp-automation** (`composio-skills/yelp-automation`) — Automate Yelp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **ynab-automation** (`composio-skills/ynab-automation`) — Automate Ynab tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **yousearch-automation** (`composio-skills/yousearch-automation`) — Automate Yousearch tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zenrows-automation** (`composio-skills/zenrows-automation`) — Automate Zenrows tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zenserp-automation** (`composio-skills/zenserp-automation`) — Automate Zenserp tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zeplin-automation** (`composio-skills/zeplin-automation`) — Automate Zeplin tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zerobounce-automation** (`composio-skills/zerobounce-automation`) — Automate Zerobounce tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zoho-automation** (`composio-skills/zoho-automation`) — Automate Zoho tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zoho-bigin-automation** (`composio-skills/zoho-bigin-automation`) — Automate Zoho Bigin tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **Zoho Books Automation** (`composio-skills/zoho-books-automation`) — Automate Zoho Books accounting workflows including invoice creation, bill management, contact lookup
- **Zoho Desk Automation** (`composio-skills/zoho-desk-automation`) — Zoho Desk automation via Rube MCP -- toolkit not currently available in Composio; no ZOHO_DESK_ tool
- **zoho-inventory-automation** (`composio-skills/zoho-inventory-automation`) — Automate Zoho Inventory tasks via Rube MCP (Composio). Always search tools first for current schemas
- **zoho-invoice-automation** (`composio-skills/zoho-invoice-automation`) — Automate Zoho Invoice tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zoho-mail-automation** (`composio-skills/zoho-mail-automation`) — Automate Zoho Mail tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zoho_bigin-automation** (`composio-skills/zoho_bigin-automation`) — Automate Zoho Bigin tasks via Rube MCP (Composio): pipelines, contacts, companies, products, and sma
- **zoho_books-automation** (`composio-skills/zoho_books-automation`) — Automate Zoho Books tasks via Rube MCP (Composio): invoices, expenses, contacts, payments, and accou
- **zoho_desk-automation** (`composio-skills/zoho_desk-automation`) — Automate Zoho Desk tasks via Rube MCP (Composio): tickets, contacts, agents, departments, and help d
- **zoho_inventory-automation** (`composio-skills/zoho_inventory-automation`) — Automate Zoho Inventory tasks via Rube MCP (Composio): items, orders, warehouses, shipments, and sto
- **zoho_invoice-automation** (`composio-skills/zoho_invoice-automation`) — Automate Zoho Invoice tasks via Rube MCP (Composio): invoices, estimates, expenses, clients, and pay
- **zoho_mail-automation** (`composio-skills/zoho_mail-automation`) — Automate Zoho Mail tasks via Rube MCP (Composio): email sending, folders, labels, and mailbox manage
- **zoominfo-automation** (`composio-skills/zoominfo-automation`) — Automate Zoominfo tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zylvie-automation** (`composio-skills/zylvie-automation`) — Automate Zylvie tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **zyte-api-automation** (`composio-skills/zyte-api-automation`) — Automate Zyte API tasks via Rube MCP (Composio). Always search tools first for current schemas.
- **connect-apps** (`connect-apps`) — Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to sen
- **connect** (`connect`) — Connect Claude to any app. Send emails, create issues, post messages, update databases - take real a
- **content-research-writer** (`content-research-writer`) — Assists in writing high-quality content by conducting research, adding citations, improving hooks, i
- **developer-growth-analysis** (`developer-growth-analysis`) — Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and are
- **docx** (`document-skills/docx`) — Comprehensive document creation, editing, and analysis with support for tracked changes, comments, f
- **pdf** (`document-skills/pdf`) — Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/sp
- **pptx** (`document-skills/pptx`) — Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx fi
- **xlsx** (`document-skills/xlsx`) — Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, dat
- **domain-name-brainstormer** (`domain-name-brainstormer`) — Generates creative domain name ideas for your project and checks availability across multiple TLDs (
- **file-organizer** (`file-organizer`) — Intelligently organizes your files and folders across your computer by understanding context, findin
- **image-enhancer** (`image-enhancer`) — Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clar
- **internal-comms** (`internal-comms`) — A set of resources to help me write all kinds of internal communications, using the formats that my 
- **invoice-organizer** (`invoice-organizer`) — Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting
- **langsmith-fetch** (`langsmith-fetch`) — Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when de
- **lead-research-assistant** (`lead-research-assistant`) — Identifies high-quality leads for your product or service by analyzing your business, searching for 
- **mcp-builder** (`mcp-builder`) — Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact wi
- **meeting-insights-analyzer** (`meeting-insights-analyzer`) — Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, 
- **raffle-winner-picker** (`raffle-winner-picker`) — Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests
- **skill-creator** (`skill-creator`) — Guide for creating effective skills. This skill should be used when users want to create a new skill
- **skill-share** (`skill-share`) — A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamles
- **slack-gif-creator** (`slack-gif-creator`) — Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and com
- **tailored-resume-generator** (`tailored-resume-generator`) — Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills,
- **template-skill** (`template-skill`) — Replace with description of the skill and when Claude should use it.
- **theme-factory** (`theme-factory`) — Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML la
- **twitter-algorithm-optimizer** (`twitter-algorithm-optimizer`) — Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrit
- **youtube-downloader** (`video-downloader`) — Download YouTube videos with customizable quality and format options. Use this skill when the user a
- **webapp-testing** (`webapp-testing`) — Toolkit for interacting with and testing local web applications using Playwright. Supports verifying

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

### [morluto/rea](https://github.com/morluto/rea) — 5 skills ★425824
Reverse engineer anything with agents, from app behavior down to native binaries.

### [react/react](https://github.com/react/react) — 14 skills ★251892
The library for web and native user interfaces.

### [anomalyco/opencode](https://github.com/anomalyco/opencode) — 24 skills ★224275
The open source coding agent.

### [n8n-io/n8n](https://github.com/n8n-io/n8n) — 40 skills ★209446
Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

### [vercel/next.js](https://github.com/vercel/next.js) — 27 skills ★143245
The React Framework

### [nodejs/node](https://github.com/nodejs/node) — 28 skills ★123206
Node.js JavaScript runtime ✨🐢🚀✨

### [earendil-works/pi](https://github.com/earendil-works/pi) — 17 skills ★119795
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

### [tw93/Mole](https://github.com/tw93/Mole) — 6 skills ★73721
🐹 Keep your Mac and PC clean, light, and running like new. Fast open-source CLI, plus native Mac and Windows apps.

### [ansible/ansible](https://github.com/ansible/ansible) — 4 skills ★71226
Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com.

### [BerriAI/litellm](https://github.com/BerriAI/litellm) — 11 skills ★62632
The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]

### [MemPalace/mempalace](https://github.com/MemPalace/mempalace) — 15 skills ★60318
The best-benchmarked open-source AI memory system. And it's free.

### [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) — 20 skills ★58382
Hindsight: Agent Memory That Learns

### [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — 11 skills ★45370
Browser automation CLI for AI agents

### [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) — 1 skills ★29095
The #1 AI Harness for Building Resumes, PDFs, Cover Letters & more, locally with 100+ LLMs support.

### [google-labs-code/design.md](https://github.com/google-labs-code/design.md) — 4 skills ★28701
A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system.

### [virattt/dexter](https://github.com/virattt/dexter) — 3 skills ★27752
An autonomous agent for deep financial research

### [steipete/CodexBar](https://github.com/steipete/CodexBar) — 3 skills ★22968
Show usage stats for OpenAI Codex and Claude Code, without having to login.

### [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — 29 skills ★21026
OpenShell is the safe, private runtime for autonomous AI agents.

### [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) — 2 skills ★16011
Towards a More Autonomous Agent System

### [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) — 17 skills ★13323
SolidCraft: an open-source parametric 3D CAD application built in pure Rust. Desktop, web, and automation through MCP.

### [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — 8 skills ★11949
Computer use CLI for AI agents

### [microsoft/inshellisense](https://github.com/microsoft/inshellisense) — 1 skills ★10754
IDE style command line auto complete

### [xykong/flux-markdown](https://github.com/xykong/flux-markdown) — 2 skills ★1296
Markdown Preview Enhanced for macOS QuickLook
