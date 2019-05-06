# Fuzzing of JSON Parsing Libraries w/ Open-Source Contributions

## Summary
This project was part of the graduate course, [*DD2482 Automated Software Testing and DevOps*](https://www.kth.se/student/kurser/kurs/DD2482?l=en) at [KTH Royal Institute of Technology](https://kth.se), with the aim of detecting and possibly resolving bugs in a range of JSON parsing libraries using fuzzing.

A selection of widely available, popular, and open-source JSON-parsing libraries were fuzzed as part of this project. Crashes were discovered in two of them, [simdjson](https://github.com/lemire/simdjson) and [ultrajson](https://github.com/esnme/ultrajson).

Crashes found in `ultrajson` were found to be not recreatable. As such, no contribution was made to the `ultrajson` project. The `simdjson` crashes however were recreatable and as such, an issue was submitted to the `simdjson` GitHub page detailing a heap corruption bug.

### Authors

- Emil Gedda (egedda@kth.se)
- Anders Eriksson (aeri3@kth.se)

## JSON Parsing Libraries
The libraries fuzzed as part of this project are listed below:

- [simdjson](https://github.com/lemire/simdjson/blob/master/README.md)
- [RapidJSON](https://github.com/Tencent/rapidjson)
- [sajson](https://github.com/chadaustin/sajson)
- [dropbox](https://github.com/dropbox/json11)
- [fastjson](https://github.com/alibaba/fastjson)
- [gason](https://github.com/vivkin/gason)
- [ultrajson](https://github.com/esnme/ultrajson)
- [jsmn](https://github.com/zserge/jsmn)
- [cJSON](https://github.com/DaveGamble/cJSON)

All of these libraries are hosted on GitHub under an open-source license and are open for contributions. All of these libraries are widely used based on their GitHub activity.

These libraries where chosen due to their inclusion in the benchmarks provided by [simdjson](https://github.com/lemire/simdjson) in their GitHub Readme.

## Tools
The tools used as part of this project are are:

- [Docker](https://www.docker.com/) - Containerization
- [AFLFast](https://github.com/mboehme/aflfast) - Gray Box Fuzzing
- [gcc](https://www.gnu.org/software/gcc/) - Compiler
- [gcc AddressSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) - Memory Error Detector
- [Python 3.7](https://www.python.org/) - For scripting

## Methodology

### Fuzzing

For the actual fuzzing part of this project, [AFLFast](https://github.com/mboehme/aflfast) was used. AFLFast is a fork of [american fuzzy lop (AFL)](http://lcamtuf.coredump.cx/afl/), a security-oriented fuzzer. We decided to use AFLFast due to the much higher performance compared to AFL.

AFLFast was run on [Google Compute Engine](https://cloud.google.com/compute/) due to Emil having leftover credits from a student promotion for [Google Cloud](https://cloud.google.com/). A virtual machine with 8 physical CPU-cores Intel Core i7 Skylake and 16 GB of RAM was used to run the fuzzing.

An example JSON-file exhibiting all language features of JSON was created to seed AFLFast:

##### JSON-File Seed
```json
{
    "a": "b",
    "b": true,
    "obj": { "a": "c" },
    "undef": null,
    "c": false,
    "int": -1,
    "list": [1, 2, 0,    3,
        4, -6 ],
    "obj2": {
        "a": { "d": "c", "g": 
            [
                "123 456-7890", null, ""
            ] },
        "b": [],
	"c": { "d": { "e": { "f": -0}}} }
}
```

A docker image was set up with AFLFast and all the JSON parsing libraries compiled and deployed to Google Compute Engine. To reduce the overhead of process instantiation and forking, we bundled all JSON parsing libraries into one single executable based on [the benchmark used in the simdjson source repo](https://github.com/lemire/simdjson/blob/master/tests/allparserscheckfile.cpp).

##### Fuzzing Dockerfile (Excerpt)
```dockerfile
FROM archlinux/base

LABEL maintainer=emil.gedda@emilgedda.se
WORKDIR /

RUN pacman -Syu --noconfirm gcc git make diffutils wget tmux

RUN git clone -j8 https://github.com/mboehme/aflfast.git \
    && cd aflfast && make install -j8

RUN git clone --recurse-submodules -j8 https://github.com/EmilGedda/simdjson.git \
    && cd simdjson \
    && git checkout 7c8404eaf95b2cde087cc131bea42a429fdab8cb \
    && make CXX=afl-g++ allparserscheckfile -j8 \
    && install allparserscheckfile /json-parsers

RUN mkdir -p fuzz/input \
    && cd fuzz/input    \
    && wget https://gist.githubusercontent.com/EmilGedda/370e487cd658b61139b63d92059e73fd/raw/a3b7358f524b9b62af188707c985e8fc586a9997/seed.json

[...]
```

The resulting binary is based on test code in the [simdjson](https://github.com/lemire/simdjson) repository. The test code did not compile in its original state, and four pull requests were submitted to make it compile as well as simplifying the related buildsystem configuration.
AFLFast was first run for approximately 3 days after which it crashed, due to running out of disk space. After upgrading to a larger storage space, it was left to run for approximately 4 days. 9,359 unique crashes of the parsing libraries occured during the fuzzing.

Every unique JSON-string output by AFLFast that caused a crash was saved to a file. At this point, these files were not sorted by the JSON-library that caused the crash.

### Classifying

The classification of what input crashed which library was done automatically by [a script written in Python](classify.py). The script was a wrapper around standalone executables we wrote for each of the JSON-libraries.
The Python script also served as a purpose to verify that the JSON-libraries crashed independently of each other, and that AFLFast did not influence the crash.
The classifier created a folder for every crashing input it discovered, recording the crashing library's stdout and stderr, aswell as a AddressSanitizer log.

##### Structure of the output from the classifier
```
$ tree bugs/simdjson | head -20
bugs/simdjson
├── 1
│   ├── asan.log.606
│   ├── input.json
│   ├── stderr.txt
│   └── stdout.txt
├── 10
│   ├── asan.log.653
│   ├── input.json
│   ├── stderr.txt
│   └── stdout.txt
[...]
```

A Dockerfile was also written for the classification, to provide consistency in the build environment. An image of this Dockerfile is available from the Dockerhub as `gedda/json-classify`.

##### Classifying Dockerfile
```dockerfile
FROM archlinux/base

LABEL maintainer=emil.gedda@emilgedda.se

RUN pacman -Syu --noconfirm gcc git make diffutils python python-pip \
    && mkdir /parsers && pip install python-Levenshtein

RUN git clone -j8 --recurse-submodules https://github.com/EmilGedda/simdjson.git 

RUN cd simdjson                                 \
    && make    SANITIZE=1 checkfile -j8         \
    && install dropbox       /parsers/dropbox   \
    && install fastjson      /parsers/fastjson  \
    && install gason         /parsers/gason     \
    && install jsmn          /parsers/jsmn      \
    && install rapidjson-enc /parsers/rapid-enc \
    && install rapidjson     /parsers/rapid     \
    && install sajson        /parsers/sajson    \
    && install simdjson      /parsers/simdjson  \
    && install ultrajson     /parsers/ultrajson

RUN rm -rf simdjson

WORKDIR /proj
ENTRYPOINT python classify.py crashes bugs /parsers/*
```
## Usage

There are two main Docker images which were written and used in this project.
For finding crashes in all libraries with AFLFast, [the docker image](Dockerfile.fuzzing) `gedda/json-fuzzing` was set up easily spin up containers fully prepared with AFLFast instrumentation compiled into the JSON-libraries.
```
$ docker pull gedda/json-fuzzing
$ docker run -it gedda/json-fuzzing
```
AFLFast will now run endlessly until cancelled by the user.
**Note:** AFLFast is currently set up to be used in an 8 physical core cpu with AVX2 support.
To disable AFLFast's core affinity requirement, add the argument `--env AFL_NO_AFFINITY=1` to the `docker run` command. AFLFast is executed within a `tmux` session to provide an easy overview of all the AFLFast instances quickly.

This docker container will populate the `/fuzz/output` directory inside the container with the documented crashes found by AFLFast.


To classify the crashes which resulted from the above step, the classifier must be used.
As the previous step, [a Docker image](Dockerfile.classify) have been prepared `gedda/json-classify` have been prepared to provide a reproducible execution environment.
```
$ git clone https://github.com/EmilGedda/kth-devops
$ cd kth-devops/open
$ docker pull gedda/json-classify
$ docker run -v $PWD:/proj --cap-add SYS_PTRACE -t gedda/json-classify
```
Where `$PWD` is the absolute path to the open directory in the classifier repository. The classifier repository includes the +9000 test cases we found from the previous step.
Since the classifier script runs binaries which include AddressSanitizer, we need to elevate our container with system ptracing capabilities.

## Crashes

##### Output of classifying script:
```
$ docker run -v $PWD:/proj --cap-add SYS_PTRACE -t gedda/json-classify
[0000s] Found 9359 test cases
[0114s|  dropbox] Classifying crashes:    0 [9359/9359 100.00%]
[0226s| fastjson] Classifying crashes:    0 [9359/9359 100.00%]
[0333s|    gason] Classifying crashes:    0 [9359/9359 100.00%]
[0443s|     jsmn] Classifying crashes:    0 [9359/9359 100.00%]
[0555s|    rapid] Classifying crashes:    0 [9359/9359 100.00%]
[0668s|rapid-enc] Classifying crashes:    0 [9359/9359 100.00%]
[0777s|   sajson] Classifying crashes:    0 [9359/9359 100.00%]
[1031s| simdjson] Classifying crashes: 1457 [9359/9359 100.00%]
[1146s|ultrajson] Classifying crashes: 1891 [9359/9359 100.00%]

Crashes found in 3348 out of 9359 given inputs
       lib  crash dupes uniqs     %
  simdjson:  1457     0  1457 15.57
 ultrajson:  1891     0  1891 20.21

[1146s] All output written to: /proj/bugs
```

All in all, `simdjson` and `ultrajson` were the only libraries that crashed during fuzzing.
Out of the 9359 crashing json files reported by AFLFast only 3348 of those were crashing when tested against each library separately.

### Libraries

#### ultrajson

By studying the `stderr.txt` files of the classifier output, they all seemed to follow the same pattern:

##### ultrajson stderr.txt (Exerpt)
```
dependencies/ujson4c/src/ujdecode.c:273:11: runtime error: member access within misaligned address 0x6290000004bc for type 'struct ArrayItem', which requires 8 byte alignment
0x6290000004bc: note: pointer points here
  00 00 00 00 be be be be  be be be be be be be be  be be be be be be be be  be be be be be be be be
              ^ 
```

`ultrajson` is written in C but comes with bindings for Python. It is clear from the `stderr` outputs that the error lies in the more user friendly layer of `ultrajson`, `ujson4c`. [A Python script](ultrajson_verify_crashes.py) using the bindings was written aiming to recreate the crashes discovered during fuzzing:

##### ultrajson Bug Recreation Script
```python
import os
import ujson

path = "../bugs/ultrajson/"

for f in os.listdir(path):
    try:
        with open(path + f + "/input.json", "rb") as f:
            try:
                ujson.loads(f.read())
            except ValueError:
                pass
    except FileNotFoundError:
pass
```

This loads all of the `input.json` files representing input that caused `ultrajson` to crash during fuzzing, and parses them using the `ujson.loads(s)` function. `ValueError` exceptions, that is when `ultrajson` itself recognizes the JSON as invalid without a crash, are caught and ignored. Some crashes also did not have an `input.json` file and as such `FileNotFoundError` exceptions where also ignored.

After running this script, no errors where discovered. As such, we concluded that we could not recreate the bugs found during fuzzing. No issues or pull requests were submitted to `ultrajson` or `ujson4c`.

#### simdjson

After studying the classifier output for the `simdjson` crashes, it was very clear that they all dealt with heap corruption. All of the AddressSanitizer logs point to the same direction:

##### AddressSanitizer log excerpt
```
=================================================================
==721==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60a000000079 at pc 0x55a201ddbaca bp 0x7ffc512b1ab0 sp 0x7ffc512b1aa0
```

To recreate these bugs, we used a demo program included in the `simdjson` repository:

##### amalgamation_demo.cpp

```cpp
/* auto-generated on Wed 13 Mar 2019 21:02:37 EDT. Do not edit! */

#include <iostream>
#include "simdjson.h"
#include "simdjson.cpp"
int main(int argc, char *argv[]) {
  const char * filename = argv[1];
  std::string_view p = get_corpus(filename);
  ParsedJson pj = build_parsed_json(p); // do the parsing
  if( ! pj.isValid() ) {
    std::cout << "not valid" << std::endl;
  } else {
    std::cout << "valid" << std::endl;
  }
  return EXIT_SUCCESS;
}
```

This program takes a filepath from as a parameter from `argv` and reads the file at that location. The program then outputs `not valid` if the file does not contain a valid JSON-string. Otherwise, it outputs `valid`. The program was compiled and run in Windows 10 using Visual Studio 2019.

Feeding this program with various `input.json` files from the `simdjson` crashes always resulted in one of four scenarios:

- Crash due to heap corruption error (Windows error popup)
- Silent crash (no output)
- Invalid output (e.g. `valid` for invalid JSON)
- Valid output with no noticable errors

As such, we considered the bug recreatable. [An issue](https://github.com/lemire/simdjson/issues/150) was created on the `simdjson` GitHub repository. A zip-file containing all the classifier output for `simdjson` was included in the issue.

## Results

Here, any results of this project are presented. This includes any issues and pull requests made as a result of this project, whether found due to the fuzzing or otherwise.

### Pull Requests Made During Set-up of *simdjson*

- [Fix parsing success check for simdjson's json_parse in allparserscheckfile.cpp and minor cleanup #141 **[MERGED]**](https://github.com/lemire/simdjson/pull/141)
- [Allows additional C(XX)FLAGS to be passed through command line #142 **[MERGED]**](https://github.com/lemire/simdjson/pull/142)
- [Fix syntax error introduced by 772919 #138 **[MERGED]**](https://github.com/lemire/simdjson/pull/138)

### Issue Created as Direct Result of Fuzzing

- [Heap Corruption error on several inputs](https://github.com/lemire/simdjson/issues/150)

## Final Thoughts

Although a lot of time and effort was spent setting up tools, we are still a bit surprised at how "easy" it was to find a bug in a big project such as `simdjson`. The bug itself is not insignificant since a heap corruption error could be a possible security issue.

As a result of this project, we've gained experience not only in fuzzing but also in the usage of Docker containers and general scripting. All in all, we are satisfied with the project as it did result in several contributions to a quite high-profile open-source library, which was our intended goal. 
On AFL vs AFLFast, one of the 8 AFLFast processes used the original AFL fuzzing heuristic, and found on average half the number of crashes of any of the AFLFast heuristics.

# Bibliography

- [Böhme, Marcel & Pham, Thuan & Roychoudhury, Abhik. (2017). *Coverage-based Greybox Fuzzing as Markov Chain*. IEEE Transactions on Software Engineering. PP. 1-1. 10.1109/TSE.2017.2785841. ](https://www.researchgate.net/publication/321987454_Coverage-based_Greybox_Fuzzing_as_Markov_Chain)
- [Langdale, Geoff & Lemire, Daniel. (2019). *Parsing Gigabytes of JSON per Second*. Computing Research Repository. arXiv:1902.08318](https://arxiv.org/abs/1902.08318)
