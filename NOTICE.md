# NOTICE

このリポジトリ（skill-hub）について、収録物の権利と扱いを明記します。

## このリポジトリの性質

skill-hub は、GitHub 上で公開されている Agent Skills（SKILL.md を含むリポジトリ）の
**カタログ（索引）と導入ツール**です。第三者のスキルの複製は保持していません。

- カタログ（`catalog.json` / `CATALOG.md`）に載るのは、リポジトリ名・URL・スター数と、
  各 SKILL.md の frontmatter 説明文の短い抜粋（識別のために必要な範囲）です。
  これらの権利は各作者に帰属します。
- スキルの導入（`bin/skillhub install`）は、上流リポジトリをその場で取得して行います。
  導入されたスキルの利用条件は、上流のライセンスに従います。

## ライセンスの線引き

- **このリポジトリ自体の作成物**（`bin/skillhub`、`build_catalog.py`、`meta/` のメタスキル、
  分類・注記などのキュレーション）は、**MIT License** です（`LICENSE` ファイル参照）。
- **カタログが参照する各リポジトリ／スキル**は、それぞれの上流ライセンスに従います。
  一覧は `SOURCES.md` にあります。このリポジトリの MIT は、上流の著作物には及びません。

## 棚卸しと自動チェック

- カタログ再生成（`build_catalog.py`）のたびに、上流リポジトリのライセンスを
  GitHub API から自動で記録し、`check_licenses.py` が
  「ライセンスなし／独自ライセンス／コピーレフト系」を監視リストとして出力します。
- 記録は `catalog.json` の各リポジトリの `license` フィールドが正本です。

## 作者の方へ

ご自身のリポジトリについて、記載の修正・削除をご希望の場合は GitHub Issues へ
ご連絡ください。確認のうえ速やかに対応します。

---

## English summary

skill-hub is a catalog and installer for publicly available Agent Skills.
It does not bundle third-party skills: the catalog holds only names, URLs, star
counts and short frontmatter excerpts for identification, and installation
fetches each skill from its upstream repository. Catalogued works remain under
their own licenses (see `SOURCES.md`). The tooling and curation in this
repository itself are MIT-licensed (see `LICENSE`). If you are an author and
want an entry corrected or removed, please open a GitHub Issue.
