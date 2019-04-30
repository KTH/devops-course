1. Initialize the repo
    - `git init`, make note of the `.git` directory and `.git/objects`
2. Create a file, hash it
    - `git hash-object -w file.txt`, make note of `-w` flag
3. Add the file to the index (staging area)
    - What's to be included in the next commit
    - Binary, so hard to inspect
    - `git update-index --add --cacheinfo 100644 HASH file.txt`
    - Make note of the fact that the blob doesn't contain the file name
4. Write the tree
    - `git write-tree`
    - Stores current snapshot of repo in .git derictory
5. Create a commit
    - `echo "First commit" | git commit-tree COMMIT_HASH`
    - Make note of a commit essentially being a reference to the tree that is
      the project root in that snapshot
6. Edit the file, add high-level, then commit with parent
    - `nano file.txt`
    - `git add file.txt`, make note that this is `git hash-object` + `git update-index`
    - `git write-tree`
    - `git commit-tree COMMIT_HASH -p PARENT_COMMIT_HASH`, make note how
      commits know their parents but not their children
7. Branches are missing, create a branch
    - `echo COMMIT_HASH > .git/refs/heads/master`
    - Make note that a branch is nothing more than a human-readable alias of a commit.
    - HEAD is a symbolic branch that acts as a bookmark, where am I right now?
