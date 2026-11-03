---
name: skillhub
description: taisukey の GitHub Starred から抽出した Agent Skills カタログ（skill-hub）を検索し、必要なスキルをこのエージェントに導入するためのスキル。「スキルを探して」「〜できるスキルある？」「skillhub で検索」「スターしたスキルを入れて」と言われたら使う。カタログには専用スキル集・公式スキル・大規模コレクション等が分類済みで収録されている。
---

# skillhub — Starred スキルカタログの検索と導入

taisukey が GitHub で Star したリポジトリのうち、Agent Skills（SKILL.md）を含むものを
抽出・分類したカタログが skill-hub リポジトリにある。このスキルはその入口。

## ハブの場所（マシンごとに異なる）

次のいずれかにある: `~/workspace/skill-hub`（Muse VM）/ `~/skill-hub`（M1）/
`~/muse-work/skill-hub`（mx）。CLI は `<hub>/bin/skillhub`。
無い場合は `git clone https://github.com/taisukey/skill-hub` で取得する。

## 使い方

```sh
HUB=<hubのパス>
$HUB/bin/skillhub status                  # カタログ規模と、このマシンの配置先
$HUB/bin/skillhub search <キーワード>      # 名前・説明・リポジトリ名で検索
$HUB/bin/skillhub list --class dedicated   # 分類: dedicated / collection / agent-bundled / product-internal
$HUB/bin/skillhub install <name>           # このマシンの全エージェントへ導入
$HUB/bin/skillhub install <name> --agent hermes   # エージェントを指定
$HUB/bin/skillhub installed                # 導入済み一覧
$HUB/bin/skillhub remove <name>            # 取り除く
```

配置先はマシンとエージェントで自動判定される:
Muse = `~/workspace/custom-skills`（VM）または `~/.claude/skills`、
Hermes = `~/.hermes/skills/starred/`、DSH = `~/.dsh/skills/`。

## 進め方

1. 頼まれた作業に使えるスキルが手元に無いとき、まず `search` でカタログを当たる。
2. 候補が見つかったら、名前・出所リポジトリ・説明を taisukey に提示し、
   導入してよいか確認してから `install` する（知らないスキルを勝手に入れない）。
3. 同名スキルが複数リポジトリにある場合は `--repo owner/repo` で絞るよう案内される。
4. product-internal 分類は、その製品自体の開発用スキルなので通常は入れない。
   collection（Composio 等）は件数が多いので、ピンポイントで指名されたものだけ入れる。
5. 導入後は `installed` と各エージェントの一覧（例: `hermes skills list`）で
   認識されたことを確認して報告する。
