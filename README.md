# skill-hub

taisukey の GitHub Starred から **Agent Skills（SKILL.md を含むリポジトリ）だけ** を抽出した
カタログと、それを Muse / Hermes / DeepSeek Harness (DSH) の各エージェントへ
配布するための CLI。スター 135 件 → SKILL.md 保有 60 リポジトリ / 1,258 スキルを分類済み。

## 分類

- `dedicated` — スキル自体が目的のリポジトリ（導入候補）
- `collection` — 大規模コレクション（Composio 等、指名したものだけ入れる）
- `agent-bundled` — エージェント本体同梱のスキルライブラリ
- `product-internal` — その製品の開発・利用専用（通常は入れない）

一覧は [CATALOG.md](CATALOG.md)、機械可読版は `catalog.json`。

## 使い方

```sh
bin/skillhub search <keyword>
bin/skillhub install <skill-name> [--agent Muse|hermes|dsh]
bin/skillhub installed
bin/skillhub remove <skill-name>
```

導入先（マシン上で自動判定）: Muse = `~/workspace/custom-skills`（VM）/ `~/.claude/skills`（Mac）、
Hermes = `~/.hermes/skills/starred/`、DSH = `~/.dsh/skills/`。
導入元のリポジトリは `cache/` に shallow clone され、状態は `installed.json` に記録される（どちらも git 管理外）。

## エージェント向けメタスキル

`meta/skillhub/SKILL.md` を各エージェントのスキルフォルダに入れると、
エージェント自身がカタログ検索と導入を行えるようになる。

## カタログの再生成

`python3 build_catalog.py`（gh CLI が使えるマシンで実行。Starred 取得 → SKILL.md 走査 →
frontmatter 収集 → curated.json の分類上書きを適用）。
