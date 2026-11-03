#!/usr/bin/env python3
"""skill-hub のカタログ再生成。

前提: gh CLI で GitHub にログイン済みのマシンで実行する。
手順: 自分の Starred を全件取得 → 各リポジトリのツリーで SKILL.md を走査 →
分類（curated.json の上書き優先）→ 導入候補の SKILL.md frontmatter を収集 →
catalog.json と CATALOG.md を書き出す。
"""
import json
import os
import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
AGENT_REPOS = {"NousResearch/hermes-agent"}
INTERNAL_PREFIXES = (".claude/", ".agents/", ".opencode/", ".gemini/", ".github/",
                     ".cursor/", ".openclaw/", "deps/", "tests/", "test/", "src/")


def gh_api(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(f"gh api {path}: {r.stderr.strip()[:200]}")
    return json.loads(r.stdout)


def get_starred():
    r = subprocess.run(["gh", "api", "user/starred", "--paginate"],
                       capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        raise RuntimeError(f"starred 取得失敗: {r.stderr.strip()[:200]}")
    repos = []
    # --paginate は JSON 配列を連結して返すためデコーダで順に読む
    dec = json.JSONDecoder()
    buf = r.stdout.strip()
    while buf:
        arr, idx = dec.raw_decode(buf)
        repos.extend(arr)
        buf = buf[idx:].strip()
    return repos


def skill_paths(repo, branch):
    try:
        tree = gh_api(f"repos/{repo}/git/trees/{branch}?recursive=1")
    except Exception:
        return []
    return [t["path"] for t in tree.get("tree", [])
            if t["path"].endswith("SKILL.md")]


def classify(repo, desc, paths, curated):
    if repo in curated:
        return curated[repo][0], curated[repo][1]
    text = (repo + " " + (desc or "")).lower()
    internal = sum(1 for p in paths
                   if p.startswith(INTERNAL_PREFIXES) or "/test" in p or "fixture" in p)
    if repo in AGENT_REPOS:
        return "agent-bundled", ""
    if "awesome" in repo.lower() and "skill" in text:
        return "collection", ""
    if "skill" in text and internal < len(paths):
        return "dedicated", ""
    return "product-internal", ""


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    if end < 0:
        return None, None
    fm = text[3:end]
    name = desc = None
    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    if m:
        name = m.group(1).strip().strip("\"'")
    m = re.search(r"^description:\s*(.+)$", fm, re.M)
    if m:
        desc = m.group(1).strip().strip("\"'")
    return name, desc


def main():
    curated = {}
    cpath = os.path.join(HERE, "curated.json")
    if os.path.exists(cpath):
        curated = json.load(open(cpath, encoding="utf-8"))
    starred = get_starred()
    print(f"starred: {len(starred)} 件", file=sys.stderr)
    catalog = {"repos": {}, "skills": {}}
    targets = []
    skills = []
    for repo_obj in starred:
        repo = repo_obj["full_name"]
        paths = skill_paths(repo, repo_obj.get("default_branch") or "main")
        if not paths:
            continue
        cls, note = classify(repo, repo_obj.get("description"), paths, curated)
        catalog["repos"][repo] = {
            "class": cls, "note": note,
            "description": repo_obj.get("description") or "",
            "stars": repo_obj.get("stargazers_count"),
            "url": f"https://github.com/{repo}",
            "skill_count": len(paths),
            "branch": repo_obj.get("default_branch") or "main",
        }
        if cls in ("dedicated", "collection", "agent-bundled"):
            for p in paths:
                targets.append((repo, p))
    print(f"SKILL.md 保有: {len(catalog['repos'])} repos / 収集対象 {len(targets)}", file=sys.stderr)

    def fetch(t):
        repo, path = t
        branch = catalog["repos"][repo]["branch"]
        url = f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"
        name = desc = None
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "skillhub-catalog"})
            text = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
            name, desc = parse_frontmatter(text)
        except Exception:
            pass
        return {"repo": repo, "path": path.rsplit("/SKILL.md", 1)[0] or ".",
                "name": name, "description": desc}

    with ThreadPoolExecutor(max_workers=12) as ex:
        skills = list(ex.map(fetch, targets))
    catalog["skills"] = skills
    with open(os.path.join(HERE, "catalog.json"), "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=1)

    lines = ["# CATALOG — Starred Agent Skills", "",
             "GitHub Starred から SKILL.md を含むリポジトリだけを抽出し、分類したカタログ。",
             "生成: build_catalog.py / 元データ: catalog.json", ""]
    order = [("dedicated", "専用スキル集（導入候補）"), ("collection", "コレクション"),
             ("agent-bundled", "エージェント同梱"), ("product-internal", "製品スコープ（通常は入れない）")]
    by_repo = {}
    for s in skills:
        by_repo.setdefault(s["repo"], []).append(s)
    for cls, title in order:
        repos = [(r, i) for r, i in catalog["repos"].items() if i["class"] == cls]
        if not repos:
            continue
        lines += [f"## {title}（{len(repos)} repos）", ""]
        for repo, info in sorted(repos, key=lambda x: -(x[1]["stars"] or 0)):
            lines.append(f"### [{repo}]({info['url']}) — {info['skill_count']} skills ★{info['stars']}")
            if info["note"]:
                lines.append(f"> {info['note']}")
            if info["description"]:
                lines.append(info["description"])
            for s in by_repo.get(repo, []):
                d = (s["description"] or "").replace("\n", " ")[:100]
                lines.append(f"- **{s['name']}** (`{s['path']}`) — {d}")
            lines.append("")
    with open(os.path.join(HERE, "CATALOG.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"完了: {len(skills)} skills を catalog.json / CATALOG.md に出力", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
