#! /usr/bin/python3
"""Visualisation script for Git repositories.

Requires the `evince` and `dot` command line tools.
"""
import time
import subprocess
import tempfile
from pathlib import Path
import sys
from itertools import groupby
from collections import namedtuple

ENCODING = sys.getdefaultencoding()


class Ref(namedtuple("Ref", "name value".split())):
    def to_graphviz(self):
        return "\n".join(
            [f'"{self.name}" [shape=rect];', f'"{self.name}" -> "{self.value}";']
        )

    @property
    def graphviz_tag(self):
        return self.name


class Child(namedtuple("Child", "name obj".split())):
    def __getattr__(self, key):
        return self.__dict__.get(key, getattr(self.obj, key))


class GitObject:
    ORDER = {"blob": 0, "tree": 1, "commit": 2}
    COLOR = {"blob": "azure", "tree": "darkolivegreen1", "commit": "darkslategray1"}
    SHAPES = {"blob": "egg", "tree": "folder", "commit": "rect"}

    def __init__(self, sha, type_, children=None, parents=None):
        self.sha = sha
        self.type_ = type_
        self._children = children or []
        self._parents = parents or []

    @property
    def short_sha(self):
        return short_sha(self.sha)

    @property
    def children(self):
        return self._children

    @property
    def parents(self):
        return self._parents

    def add_child(self, name, obj):
        self._children.append(Child(name, obj))

    def add_parent(self, obj):
        self._parents.append(obj)

    def to_graphviz(self):
        return self._to_graphviz_node() + "\n" + self._to_graphviz_edges()

    @property
    def graphviz_tag(self):
        return self.short_sha

    def _to_graphviz_node(self):
        return (
            f'"{self.short_sha}" [label="{self.type_}\n{self.short_sha}"'
            f",fillcolor={self.COLOR[self.type_]},shape={self.SHAPES[self.type_]}];"
        )

    def _to_graphviz_edges(self):
        output = ""
        if self.children:
            for child in self.children:
                output += f'"{self.graphviz_tag}" -> "{child.graphviz_tag}" [label="{child.name}"];\n'
        if self._parents:
            for parent in self._parents:
                output += (
                    f'"{parent.graphviz_tag}" -> "{self.graphviz_tag}" [dir=back];\n'
                )
        return output.strip()

    def __repr__(self):
        children_str = f", children={self.children}" if self.children else ""
        parent_str = f", parents={self.parents}" if self._parents else ""
        return f"{self.type_}(sha={self.short_sha}{parent_str}{children_str})"

    def __str__(self):
        return fr"{self.type_}\n{self.short_sha}"

    def __lt__(self, o):
        if not isinstance(o, __class__):
            raise TypeError(
                f"'<' not supported between instances of '{self.__class__.__name__}' and '{o.__class__.__name__}'"
            )
        return self.ORDER[self.type_] < self.ORDER[o.type_]

    def __hash__(self):
        return int(self.sha, base=16)


def short_sha(sha):
    return sha[:7]


def git_cat_file(sha, *options):
    options = " ".join(options)
    rc, stdout, stderr = captured_run(*f"git cat-file {options} {sha}".split())
    if rc != 0:
        raise RuntimeError(f"git cat-file exited with non-zero exit status for {sha}")
    return stdout.strip()


def git_state(git_root):
    """Return a hash of the current state of the .git directory. Only considers
    fsck verbose output and refs.
    """
    rc, stdout, stderr = captured_run(*"git fsck --full -v".split())
    refs = "".join([ref.name + ref.value for ref in get_refs(git_root)])
    return hash(stdout + stderr + refs)


def captured_run(*args, **kwargs):
    """Run a subprocess and capture the output."""
    proc = subprocess.run(
        args, **kwargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    return (proc.returncode, proc.stdout.decode(ENCODING), proc.stderr.decode(ENCODING))


def add_children(tree, git_objects):
    """Add children to a tree git object."""
    for line in git_cat_file(tree.sha, "-p").split("\n"):
        mode, type_, sha, name = line.strip().split()
        child = git_objects[sha]
        tree.add_child(name, child)


def add_parents_and_tree(commit, git_objects):
    """Add parent reference (i.e. to the parent commit) and tree reference (to
    the top-level tree) to a commit object.
    """
    content = git_cat_file(commit.sha, "-p")
    ptr_str = content.split("\n")[0].strip()
    ptr_obj = git_objects[ptr_str.strip().split()[1]]
    commit.add_child("", ptr_obj)

    # parents may not exist
    for line in content.split("\n")[1:]:
        if line.startswith("author"):
            break
        elif line.startswith("parent"):
            _, parent_sha = line.strip().split()
            commit.add_parent(git_objects[parent_sha])


def to_cluster(git_objects, label):
    """Return a string with a graphviz cluster of the provided git objects."""
    content = "\n".join([obj.to_graphviz() for obj in git_objects])
    return f"""subgraph cluster_{label} {{
label="{label}";
style="rounded";
bgcolor=beige;
{content}
}}
"""


def get_refs(git_root):
    """Return concrete refs and the HEAD symbolic ref. Return
    nothing if there are no concrete refs.
    """
    symb_file = git_root / "HEAD"
    ref_heads = git_root / "refs" / "heads"
    refs = []
    if ref_heads.exists():
        refs += [
            Ref(f.name, short_sha(f.read_text(encoding=ENCODING).strip()))
            for f in ref_heads.iterdir()
        ]

    if symb_file.exists() and refs:  # only add HEAD if there are concrete refs
        symb_contents = symb_file.read_text(encoding=ENCODING).split()
        symb_value = (
            symb_contents[-1].split("/")[-1]
            if len(symb_contents) > 1
            else short_sha(symb_contents[-1])
        )
        refs.append(Ref("HEAD", symb_value))

    return refs


def to_graphviz(git_objects, refs):
    """Return a string with graphviz representing the provided Git objects and
    refs.
    """
    groups = {
        key: list(group)
        for key, group in groupby(sorted(git_objects), key=lambda obj: obj.type_)
    }

    output = ""
    if "tree" in groups or "blob" in groups:
        content_objs = groups.get("tree", []) + groups.get("blob", [])
        output += to_cluster(content_objs, "Content")
    if "commit" in groups:
        output += to_cluster(groups["commit"], "Commits")
    if refs:
        output += "\n".join([ref.to_graphviz() for ref in refs])

    return f"""digraph G {{
nodesep=.3;
ranksep=.5;
node [style=filled];
rankdir=LR;
{output}
}}"""


def create_graphviz_repr(git_root):
    """Return a string with a graphviz representation of Git objects and
    refs.
    """
    if not git_root.exists():
        return r"digraph G {}"

    objects_root = git_root / "objects"
    object_dirs = (d for d in objects_root.iterdir() if len(d.name) == 2 and d.is_dir())
    object_shas = (d.name + file.name for d in object_dirs for file in d.iterdir())
    git_objects = {
        sha: GitObject(sha=sha, type_=git_cat_file(sha, "-t"), children=set())
        for sha in object_shas
    }
    for obj in git_objects.values():
        if obj.type_ == "tree":
            add_children(obj, git_objects)
        elif obj.type_ == "commit":
            add_parents_and_tree(obj, git_objects)

    return to_graphviz(git_objects.values(), get_refs(git_root))


def compile_pdf(dot_file, pdf_file, graphviz):
    dot_file.write_text(graphviz)
    captured_run(*f"dot -Tpdf {str(dot_file)} -o {str(pdf_file)}".split())


def create_graph_pdf(dot_file, pdf_file, git_root):
    graphviz = create_graphviz_repr(git_root)
    compile_pdf(dot_file, pdf_file, graphviz)


def evince(pdf_file):
    """Run Evince on the PDF file in a new thread."""
    subprocess.Popen(f"evince {str(pdf_file)}".split())


def main():
    pdf_name = "graph.pdf"
    dot_name = "graph.dot"
    git_root = Path(".git")
    with tempfile.TemporaryDirectory() as tmpdir:
        state_cache = git_state(git_root)
        dot_file = Path(str(tmpdir)) / dot_name
        pdf_file = Path(str(tmpdir)) / pdf_name
        create_graph_pdf(dot_file, pdf_file, git_root)
        evince(pdf_file)

        while True:
            time.sleep(1)
            state_out = git_state(git_root)
            if state_cache != state_out:
                state_cache = state_out
                create_graph_pdf(dot_file, pdf_file, git_root)


if __name__ == "__main__":
    main()
