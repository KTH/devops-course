import os
import re
import sys

from github import Auth, Github


# Hidden marker used to find (and update) our own comment on the PR
COMMENT_MARKER = "<!-- cross-task-check -->"
BOT_LOGIN = "github-actions[bot]"

OPPOSITE_TASK = {
    "demo": "scientific-paper",
    "scientific-paper": "demo",
}

CONTRIBUTION_PATH = re.compile(
    r"contributions/"
    r"(demo|scientific-paper)/"
    r"(week[^/\r\n]*)/"
    r"([^/\r\n]+)/"
    r"README\.md"
)


class CheckError(Exception):
    """Infrastructure error (not a conflict between contributions)."""


def parse_contribution(path, source):
    """
    Convert a path such as:
        contributions/demo/week3/group-a-b/README.md

    into:
        {
            "task": "demo",
            "week": "week3",
            "group": "group-a-b",
            "members": {"a", "b"},
            "path": "contributions/demo/week3/group-a-b/README.md",
            "source": "PR #12",
        }

    Return None if the path is not a contribution.
    """
    match = CONTRIBUTION_PATH.fullmatch(path)

    if match is None:
        return None

    task, week, group = match.groups()

    return {
        "task": task,
        "week": week,
        "group": group,
        "members": set(group.split("-")),
        "path": path,
        "source": source,
    }


def get_pr_changes(pr, source):
    """
    Read the files of a PR (paths only, no content is ever read).

    Return:
      - contributions: the contributions that exist after the PR
        (removed files do not count)
      - touched_paths: every path the PR adds, modifies, removes or
        renames (both the old and the new path for a rename)
    """
    contributions = []
    touched_paths = set()

    for changed_file in pr.get_files():
        touched_paths.add(changed_file.filename)

        # Rename: the old path disappears from the branch.
        # Copy: the original still exists, so we do not touch it.
        if changed_file.status == "renamed" and changed_file.previous_filename:
            touched_paths.add(changed_file.previous_filename)

        if changed_file.status == "removed":
            continue

        contribution = parse_contribution(changed_file.filename, source)

        if contribution is not None:
            contributions.append(contribution)

    return contributions, touched_paths


def get_open_contributions(repo, base_ref, current_pr_number, targets):
    """
    Contributions from open PRs (excluding the current one) whose
    (week, task) is one of the targets.

    Return a {path: contribution} dict.
    """
    result = {}

    for pr in repo.get_pulls(
        state="open",
        base=base_ref,
        sort="created",
        direction="asc",
    ):
        if pr.number == current_pr_number:
            continue

        contributions, _ = get_pr_changes(pr, "PR #{}".format(pr.number))

        for contribution in contributions:
            if (contribution["week"], contribution["task"]) in targets:
                result[contribution["path"]] = contribution

    return result


def get_merged_contributions(repo, base_ref, targets, excluded_paths):
    """
    Contributions that exist in the current state of the branch whose
    (week, task) is one of the targets.

    `excluded_paths` holds the paths touched by the current PR (modified,
    removed, renamed). They are dropped from the result to avoid
    self-conflicts and contributions that will no longer exist.

    Return a {path: contribution} dict.
    """
    # Resolve the branch to a commit SHA: it gives a fixed snapshot and
    # avoids any ambiguity with a purely numeric branch name such as "2026"
    commit_sha = repo.get_branch(base_ref).commit.sha
    tree = repo.get_git_tree(commit_sha, recursive=True)

    # The API truncates very large trees: fail loudly rather than
    # silently miss a conflict
    if tree.raw_data.get("truncated"):
        raise CheckError(
            "Git tree of branch {} is truncated, cannot reliably check "
            "cross-task conflicts.".format(base_ref)
        )

    result = {}

    for element in tree.tree:
        if element.type != "blob":
            continue

        if element.path in excluded_paths:
            continue

        contribution = parse_contribution(element.path, "already merged")

        if contribution is None:
            continue

        if (contribution["week"], contribution["task"]) in targets:
            result[contribution["path"]] = contribution

    return result


def compare_contributions(left, right):
    """
    Return a conflict if the two contributions have different tasks, the
    same week, and at least one member in common. Otherwise return None.
    """
    if left["task"] == right["task"]:
        return None

    if left["week"] != right["week"]:
        return None

    common_members = left["members"] & right["members"]

    if not common_members:
        return None

    return {
        "week": left["week"],
        "members": sorted(common_members),
        "left": left,
        "right": right,
    }


def code_span(text):
    """
    Render a student-controlled value as inline code, so it cannot inject
    markdown or trigger an @mention.
    """
    return "`{}`".format(text.replace("`", "'"))


def format_message(conflicts):
    lines = [
        "**Cross-task conflict detected**",
        "",
        "A student cannot participate in both a demo and a "
        "scientific-paper during the same week.",
        "",
    ]

    for conflict in conflicts:
        left = conflict["left"]
        right = conflict["right"]

        lines.append(
            "- Week {week}: {members} appear in {left_path} ({left_source}) "
            "and {right_path} ({right_source}).".format(
                week=code_span(conflict["week"]),
                members=", ".join(code_span(m) for m in conflict["members"]),
                left_path=code_span(
                    "{}/{}".format(left["task"], left["group"])
                ),
                left_source=left["source"],
                right_path=code_span(
                    "{}/{}".format(right["task"], right["group"])
                ),
                right_source=right["source"],
            )
        )

    return "\n".join(lines)


def find_cross_task_conflicts(repo, base_ref, current_pr_number):
    """
    Return None if there is no conflict, otherwise the message to display.
    Raise CheckError on an infrastructure error.
    """
    
    current_pr = repo.get_pull(current_pr_number)
    current_contributions, current_touched_paths = get_pr_changes(
        current_pr, "this PR"
    )

    if not current_contributions:
        return None

    targets = {
        (c["week"], OPPOSITE_TASK[c["task"]])
        for c in current_contributions
    }

    # Open PRs BEFORE the tree: if a PR gets merged between the two API
    # calls, its contribution shows up in one source or the other
    # (or both), and is never lost.
    open_contributions = get_open_contributions(
        repo, base_ref, current_pr_number, targets
    )

    # Current state of the branch, without the paths touched by the
    # current PR (avoids self-conflicts, handles modified/removed files)
    merged_contributions = get_merged_contributions(
        repo, base_ref, targets, excluded_paths=current_touched_paths
    )

    # Deduplicate by path: the "open PR" version wins (it carries the PR number)
    other_contributions = list(
        {**merged_contributions, **open_contributions}.values()
    )

    # Compare
    conflicts = []

    for current in current_contributions:
        for other in other_contributions:
            conflict = compare_contributions(current, other)

            if conflict is not None:
                conflicts.append(conflict)

    # Contributions of the current PR against each other
    for index, left in enumerate(current_contributions):
        for right in current_contributions[index + 1:]:
            conflict = compare_contributions(left, right)

            if conflict is not None:
                conflicts.append(conflict)

    if not conflicts:
        return None

    return format_message(conflicts)


def upsert_comment(repo, pr_number, message):
    """
    Create or update the check's comment on the PR.
    If message is None, delete the existing comment (conflict resolved).
    Only comments written by the bot are considered, so a student cannot
    make the script edit or delete their own comment by copying the marker.
    """
    issue = repo.get_issue(pr_number)

    existing = next(
        (
            comment
            for comment in issue.get_comments()
            if COMMENT_MARKER in comment.body
            and comment.user is not None
            and comment.user.login == BOT_LOGIN
        ),
        None,
    )

    if message is None:
        if existing is not None:
            existing.delete()
        return

    body = "{}\n{}".format(COMMENT_MARKER, message)

    if existing is None:
        issue.create_comment(body)
    elif existing.body != body:
        existing.edit(body)


def escape_command(text):
    """Escape a text for a workflow command (::error::)."""
    return text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def write_step_summary(text):
    path = os.environ.get("GITHUB_STEP_SUMMARY")

    if not path:
        return

    with open(path, "a", encoding="utf-8") as summary:
        summary.write(text + "\n")


def main():
    token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]  # set by GitHub: owner/repo
    pr_number = int(os.environ["PR_NUMBER"])
    base_ref = os.environ["BASE_REF"]

    repo = Github(auth=Auth.Token(token)).get_repo(repo_name)

    try:
        message = find_cross_task_conflicts(repo, base_ref, pr_number)
    except CheckError as error:
        # Infrastructure error: fail the job, but leave any existing
        # conflict comment untouched
        print(
            "::error title=Cross-task check failed::"
            + escape_command(str(error))
        )
        sys.exit(1)

    # Comment first, then fail: the student sees the reason in the PR
    upsert_comment(repo, pr_number, message)

    if message is None:
        write_step_summary("No cross-task conflict detected.")
        return

    write_step_summary(message)
    print("::error title=Cross-task conflict::" + escape_command(message))
    sys.exit(1)


if __name__ == "__main__":
    main()