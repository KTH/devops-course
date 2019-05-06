We're going to talk about how Git works under the hood.

First, imagine that we have a repository with a single
version of a single file. In other words, run these three
commands. Git actually stores version history as Git objects
in the .git/objects directory, which is visualized in this
figure. But what is that we're looking at here? Let's start
from `git add`, which can be decomposed into the
`hash-object` and `update-index` commands. `hash-object`
creates a compressed version of the file's contents, called
a blob, and stores it in the objects directory. However, the
blob contains only the file's contents, and not for example
filepath. That information is first stored in the index
file, which `update-index` command updates. That's `git
add`. `git commit` on the other hand can be decomposed into
`write-tree` and `commit-tree`. `write-tree` reads the index
file and creates tree objects, which are essentially just
directories. Finally, the `commit-tree` command creates a
commit object which points to the root tree of some specific
version of the repository. Recreating a version of the
repository is then pretty simple, just start from a commit
and follow the named edges to trees and blobs, creating the
respective directories and files.

Now, Simon will show you how to use the low-level commands
to actually achieve this single add and commit. There are
three things to look at here. The terminal down here is
where we will run commands. The terminal over here shows the
directory structure of .git/objects, and the image here will
show a visualization of the Git objects.

**Begin live demo (largely follows the screencast) :)**
