#!/usr/bin/env python3
"""check_licenses.py — skill-hub カタログのライセンス監視リストを出す。

catalog.json の各リポジトリの `license` フィールド（build_catalog.py が
GitHub API から自動記録する SPDX 名）を見て、注意が要るものを分類して表示する。
判定は「記録と見張り」までで、導入の可否は人間が決める。

使い方: python3 check_licenses.py [catalog.json へのパス]
"""
import json
import sys

PERMISSIVE = {"MIT", "MIT-0", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause",
              "ISC", "CC0-1.0", "Unlicense", "0BSD"}
COPYLEFT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0",
            "MPL-2.0", "EPL-2.0", "CC-BY-SA-4.0"}


def classify(entry):
    if "license" not in entry:
        return "未記録"
    lic = entry["license"]
    if lic is None or lic == "" or lic in ("NONE", "ライセンスなし"):
        return "ライセンスなし"
    if lic in PERMISSIVE:
        return "OK"
    if lic in COPYLEFT or "GPL" in lic:
        return "コピーレフト系"
    if lic == "NOASSERTION":
        return "独自・複合（要確認）"
    return "独自・その他（要確認）"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "catalog.json"
    with open(path, encoding="utf-8") as f:
        catalog = json.load(f)
    repos = catalog.get("repos", {})
    watch = {}
    counts = {}
    for full in sorted(repos, key=str.lower):
        kind = classify(repos[full])
        counts[kind] = counts.get(kind, 0) + 1
        if kind != "OK":
            e = repos[full]
            shown = e.get("license") or ("ライセンスなし" if "license" in e else "記録なし")
            watch.setdefault(kind, []).append(f"{full}（{shown}）")
    print(f"対象 {len(repos)} リポジトリ: " +
          " / ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    if not watch:
        print("監視リスト: なし")
        return
    print("監視リスト:")
    for kind in sorted(watch):
        print(f"- {kind}: " + ", ".join(watch[kind]))


if __name__ == "__main__":
    main()
