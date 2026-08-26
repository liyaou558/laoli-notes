#!/usr/bin/env python3
"""通过 GitHub Git Data API (api.github.com) 直传 commit，绕开 github.com:443 被墙问题。
使用 `gh api`（已登录）做认证，避免手写 token。

用法:
    python3 push_via_git_data_api.py

需先在下方 CONFIG 修改 REPO/BRANCH/MSG/FILES。
"""
import base64
import json
import subprocess
import sys

CONFIG = {
    "repo": "liyaou558/laoli-notes",
    "branch": "main",
    "msg": "毛选精读: 09 怎样分析农村阶级",
    "files": [
        "public/maoxuan/09_怎样分析农村阶级.html",
        "src/pages/maoxuan/index.astro",
    ],
}


def gh(*args, input_data=None):
    cmd = ["gh", "api", "--hostname", "github.com"]
    cmd.extend(args)
    if input_data is not None:
        cmd.extend(["--input", "-"])
    p = subprocess.run(cmd, input=input_data, capture_output=True, text=True)
    if p.returncode != 0:
        print("[FATAL] gh api 失败:", " ".join(args))
        print("stderr:", p.stderr[:2000])
        sys.exit(1)
    return json.loads(p.stdout) if p.stdout.strip() else {}


def main():
    repo = CONFIG["repo"]
    branch = CONFIG["branch"]

    # 1. 取当前 ref（分支头 commit）
    ref = gh(f"repos/{repo}/git/ref/heads/{branch}")
    base_commit_sha = ref["object"]["sha"]
    print("base commit:", base_commit_sha)

    # 2. 取 base commit → base tree
    commit = gh(f"repos/{repo}/git/commits/{base_commit_sha}")
    base_tree_sha = commit["tree"]["sha"]
    print("base tree:", base_tree_sha)

    # 3. 逐个文件 POST blob
    entries = []
    for path in CONFIG["files"]:
        with open(path, "rb") as f:
            content = f.read()
        b64 = base64.b64encode(content).decode()
        blob = gh(
            f"repos/{repo}/git/blobs",
            input_data=json.dumps({"content": b64, "encoding": "base64"}),
        )
        blob_sha = blob["sha"]
        entries.append({
            "path": path,
            "mode": "100644",
            "type": "blob",
            "sha": blob_sha,
        })
        print("blob ok:", path, blob_sha[:12])

    # 4. POST tree（以 base_tree 为底，覆盖上述文件）
    tree = gh(
        f"repos/{repo}/git/trees",
        input_data=json.dumps({
            "base_tree": base_tree_sha,
            "tree": entries,
        }),
    )
    new_tree_sha = tree["sha"]
    print("new tree:", new_tree_sha)

    # 5. POST commit
    new_commit = gh(
        f"repos/{repo}/git/commits",
        input_data=json.dumps({
            "message": CONFIG["msg"],
            "tree": new_tree_sha,
            "parents": [base_commit_sha],
        }),
    )
    new_commit_sha = new_commit["sha"]
    print("new commit:", new_commit_sha)

    # 6. PATCH ref 指向新 commit
    updated = gh(
        f"repos/{repo}/git/refs/heads/{branch}",
        input_data=json.dumps({"sha": new_commit_sha, "force": False}),
    )
    print("ref updated:", updated.get("object", {}).get("sha", "?"))

    print("\n[DONE] 已通过 Git Data API 直传 commit 到 origin/main")
    print("后续: git fetch origin main && git reset --hard origin/main 同步本地")


if __name__ == "__main__":
    main()
