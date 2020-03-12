# Grand Fuzzing Challenge 2020!

## How to participate

To participate in the fuzzing competition, you submit a solution for fuzzing testing on binary `ffmpeg`, together with a 2-page README explaining what you did.

Binaries to be fuzzed: static build of FFmpeg 4.2

Note that you have a **one hour** execution time budget **in total**, i.e. the grader spends at most one hour to execute all your inputs in a top-down order. If two submissions have the same coverage, the one with less execution time gets the higher score.

The offcially provided static builds of FFmpeg (https://johnvansickle.com/ffmpeg/) do not contain debugging information. If you need to analyze the coverage with the help of debugging symbols, you may need to build FFmpeg by yourself. We provide the following resource for your convenience:

- [Source code of ffmpeg-4.2 for direct download](http://ffmpeg.org/releases/ffmpeg-4.2.tar.bz2) ([FFmpeg Compilation Guide](https://trac.ffmpeg.org/wiki/CompilationGuide))
- Use our [fuzzing-competition-reference-build-ffmpeg42](https://hub.docker.com/repository/docker/kthassert/fuzzing-competition-reference-build-ffmpeg42) docker image, you will find the source code in `/root/ffmpeg_sources`. The binary file `ffmpeg` is in `/root/bin`. `ffmpeg_g` is the one that contains debugging symbols.
- Download `ffmpeg-v4.2-static-build.tar` [from KTH box](https://kth.box.com/) (sha1sum value `todo`). It contains all statically linked binaries, but note that we could only guarantee these binaries work correctly in Ubuntu 16.04.

## Grading Criteria

**Team Name:**  
**Team Members:**

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The solution is correctly formatted | Yes | No | Remarkable |
|The README well explains the used tools  | Yes | No | Remarkable |
|The README well explains the employed search and meta-optimization  | Yes | No | Remarkable |
|The README well explains the undertaken customization / modification | Yes | No | Remarkable |
|The README contains a good and concise take-home message | Yes | No | Remarkable |

To pass, you need to achieve all the criteria above. To get a distinction, the code coverage achieved by the entry is within the top-25%.

## How to Submit

We evaluate submissions in a fully automatic manner. Please strictly follow the instructions below to submit your work.

You submit by email an archive which follows this structure:

```
A folder with your group name (like email-email)
├─ README.md (2-page document explaining what you did)
├─ files (you might use files as parameters)
├──┼─file1
├──┼─file2
├──┴─ ...
└─ input.txt (plain text file, each line contains a sequence of command arguments)
```

An example for `input.txt`:

```
-h
-h long
-h full
-i files/file1.mp4 -b:v 640k output.ts
```

The competition submissions must be sent before **Tue, April 21st, midnight, Stockholm time**, to dd2482@eecs.kth.se If the submission is larger than 10MB, you may upload it to [KTH Box](https://kth.app.box.com/) or other similar platforms and provide us a downloading link.
