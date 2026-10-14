#!/usr/bin/python3
# list PRs (open and closed) labelled feedback, tutorial or project,
# in order of submission
# usage ./list_prs.py
# requires the GitHub CLI (gh), authenticated

import json
import subprocess

REPO = "KTH/devops-course"
LABELS = ["feedback", "tutorial", "project", "contribution_to_opensource"]
YEAR = "2026"

prs = {}
for label in LABELS:
    # gh combines multiple --label flags with AND, so query each label separately
    output = subprocess.check_output([
        "gh", "pr", "list",
        "--repo", REPO,
        "--state", "all",
        "--label", label,
        "--limit", "10000",
        "--json", "number,url,state,createdAt,labels",
    ])
    for pr in json.loads(output):
        # createdAt is ISO 8601, e.g. 2026-09-29T10:00:00Z
        if pr["createdAt"].startswith(YEAR):
            prs[pr["number"]] = pr

print("URL\tstatus\ttask type")
for pr in sorted(prs.values(), key=lambda p: p["createdAt"]):
    # merged PRs count as closed
    status = "open" if pr["state"] == "OPEN" else "closed"
    task_type = ",".join(l["name"] for l in pr["labels"] if l["name"] in LABELS)
    print(f"{pr['url']}\t{status}\t{task_type}")
