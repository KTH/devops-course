# Git plumbing - What is a commit?

* **Group members:** Joakim Croona (jcroona@kth.se), Simon Larsén
  (slarse@kth.se)

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
