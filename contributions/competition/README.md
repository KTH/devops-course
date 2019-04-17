This folder contains students work on Grand Fuzzing Challenge.

## Main Requirement

To participate to the fuzzing competition, you submit a solution for all provided binaries, together with a 2 page document explaining what you did.

Binaries to be fuzzed: the following 20 commands from GNU coreutils 8.25

- /bin/cat
- /bin/cp
- /bin/date
- /bin/dd
- /bin/df
- /bin/dir
- /bin/echo
- /bin/false
- /bin/ln
- /bin/ls
- /bin/mkdir
- /bin/mktemp
- /bin/mv
- /bin/pwd
- /bin/sleep
- /bin/printf
- /bin/touch
- /bin/true
- /bin/uname
- /bin/vdir

Note that you have a **one hour** execution time budget **in total**, i.e. the grader spends at most one hour to execute all your inputs to these 20 commands. If two submissions have the same coverage, the one with less execution time gets the higher score.

Regarding coreutils 8.25, it is integrated in Ubuntu 16.04 LTS. However, the binaries in Ubuntu don't contain debugging information, you might need to build coreutils by yourself to analyze the fuzzing coverage. We provide the following resource for your convenience:

- [The official Git repo of GNV coreutils](http://git.savannah.gnu.org/gitweb/?p=coreutils.git) (clone the repo and checkout tag `v8.25`)
- Use our [fuzzing-competition-reference-build](https://hub.docker.com/r/kthassert/fuzzing-competition-reference-build) docker image, you will find the source code in `/root/coreutils`, all coreutils binaries in `/bin` have been rebuilt with debugging info.
- Download `coreutils-v8.25-static-build.tar` [from KTH box](https://kth.box.com/s/qrjxfv8qps1gwwlmif395pvemda9yj2j) (sha1sum value `01ed7186b937fbb316eedcb622f391a12b771a55`). It contains all statically linked binaries, but note that we could only guarantee these binaries work correctly in Ubuntu 16.04.

## Grading Criteria

**Team Name:**  
**Team Members:**

|                                             | Yes | No | Outstanding |
|-------------------------------------------- | ----|----|-------------|
|All binaries are fuzzed | Yes | No | Outstanding |
|The coverage on average of all binaries is higher than 50% | Yes | No | Outstanding |
|The solution is correctly formatted | Yes | No | Outstanding |
|The document well explains the used tools  | Yes | No | Outstanding |
|The document well explains the employed search and meta-optimization  | Yes | No | Outstanding |
|The document well explains the undertaken customization / modification | Yes | No | Outstanding |
|The document contains a good and concise take-home message | Yes | No | Outstanding |
|The entry is within the top-25%  | Yes | No | n-a |

| Comments: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------------|
| <br/><br/><br/>|

## How to Submit

We evaluate submissions in a fully automatic manner. Please strictly follow the instructions below to submit your work. You create one file per fuzzed programs, for example `ls.txt` for `ls`. In the file, each line contains a sequence of command arguments.

An example for `ls.txt`:

```
-l
-l -a
-lrt
files/file1
```

You submit by email an archive which follows this structure:

```
A folder with your group name (like email1-email2)
├─ README.md / README.pdf (2 page document explaining what you did)
├─ files (you might use files as parameters)
├──┼─file1
├──┼─file2
├──┴─ ...
├─ ls.txt
├─ mkdir.txt
└─ ...
```

The competition submissions must be sent before **April 23, 23:59, Stockholm time**, to dd2482@eecs.kth.se
