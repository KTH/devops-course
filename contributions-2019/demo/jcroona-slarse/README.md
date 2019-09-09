# Git plumbing - What is a commit?

* **Group members:** Joakim Croona (jcroona@kth.se), Simon Larsén
  (slarse@kth.se)
* **Screencast:** [Under the hood of Git: Objects and branches in 3 minutes](https://www.youtube.com/watch?v=_rLuz9gzDVQ)

### Background
Version control is a fundamental part of DevOps. Without VCS, we think DevOps
probably wouldn't be a viable way of doing things. While we concede that version
control is fundamental to many other forms of development as well, we think that
it is _especially_ important in DevOps to facilitate for example fast iteration
and developer accountability in production. Imagine rapibly pushing releases to
production environments without having a tried and true way of figuring out what
changed from one release to another, or who made those changes and is likely
able to fix any related problems. As such, we find that a basic understanding of
what is actually going on in the VCS system is both beneficial to developers
practicing DevOps, but also plain interesting to anyone using version control.

### Demo proposal
We would like to demonstrate the very basics of the functionality that underpins
Git's version control mechanics, mostly focusing on Git blob, tree and commit
objects. The idea is to demonstrate the use some of the low-level plumbing
commands to simulate `git add` and `git commit`, with accompanying graphics
visualising the `.git/objects` directory to facilitate understanding. The goal
is that people who come in with a basic of understanding of how to use Git,
leave with a basic understanding of what a commit actually is in terms of files
and their relations to each other.

### Using `gitviz.py`
The [gitviz.py](gitviz.py) is the script that was used to generate the
graphical representation of the Git objects and branches in the screencast. It
has only been tested to run on Arch Linux, but should run on most any Linux
distribution, and probably macOS as well.

* **Requirements:** Python 3.6+, Evince and the `dot` command line program (from
  `inkscape`).
  - You can replace Evince and `dot` with any comparable programs and edit the
    script. The document viewer (replacing Evince) must be able to automatically
    refresh when a document is updated, and the replacement for `dot` must be
    able to compile graphviz to a PDF.
* **Usage:** Just run the script in the root directory of a _fresh_ Git
  repository.
  - That is to say, run `python3 gitviz.py`!
  - The script cannot handle
    [Packfiles](https://git-scm.com/book/en/v2/Git-Internals-Packfiles), so if
    the repo has ever been pushed or pulled, the script will probably crash.
  - Large repositories take a very long time to render with `dot`. Don't use
    this on large repositories.
