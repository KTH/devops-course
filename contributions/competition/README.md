This folder contains students work on Grand Fuzzing Challenge.

## Main Requirement

The students participate to the fuzzing competition and submit a solution for all provided binaries, together with a 2 page document explaining what they did.

## Grading Criteria

**Team Name:**  
**Team Members:**

|                                             | Yes | No | Outstanding |
|-------------------------------------------- | ----|----|-------------|
|All binaries are fuzzed  | Yes | No | Outstanding |
|All binaries are covered more than 0.75 * Average over all entries | Yes | No | Outstanding |
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

Students will create one file per fuzzed programs, for example `ls.txt` for `ls` (GNU coreutils). In the file, each line contains a set of command arguments.

An example for `ls.txt`:

```
-l
-l -a
-lrt
```

Make an archive which follows this structure:

```
A folder with your group name (like T1G1)
├─ READEME.md / READEME.pdf (2 page document explaining what you did)
├─ ls.txt
├─ mkdir.txt
└─ ...
```

The competition submissions must be sent before April 23, noon, Stockholm time, to dd2482@eecs.kth.se