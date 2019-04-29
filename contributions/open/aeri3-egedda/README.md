# Fuzzing of JSON parsing libraries /w Open-Source Contributions

## Introduction ***!!!TODO!!!***
This project aims to detect and possibly resolve bugs in a range of JSON parsing libraries using fuzzing.

Any bugs found during fuzzing will be reported as an issue to the corresponding FOSS-project. If the bugs are of a simple nature, we would like to resolve them and issue pull requests on GitHub.

### Goal ***!!!TODO!!!***

Ideally, we would like this project to result in one or more pull requests on GitHub resolving bugs found during fuzzing. If no bugs discovered are of a reasonably simple nature for this project to resolve, we will at least report any bugs we discover to aid the development of our chosen libraries.

### Authors

- Emil Gedda (egedda@kth.se)
- Anders Eriksson (aeri3@kth.se)

## Usage ***!!!TODO!!!***

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

AFLFast was run on [Google Compute Engine](https://cloud.google.com/compute/) due to Emil having leftover credits from a student promotion for [Google Cloud](https://cloud.google.com/). A virtual machine with 8 physical CPU-cores was used to run the fuzzing.

An example JSON-file exhibiting all language features of JSON was created to seed AFLFast:

#### JSON-File Seed
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

#### Fuzzing Dockerfile (Excerpt)
```docker
FROM archlinux/base

LABEL maintainer=emil.gedda@emilgedda.se
WORKDIR /

RUN pacman -Syu --noconfirm gcc git make diffutils wget tmux

RUN git clone -j8 https://github.com/mboehme/aflfast.git \
    && cd aflfast && make install -j8

RUN git clone -j8 --recurse-submodules https://github.com/EmilGedda/simdjson.git \
    && cd simdjson \
    && make CXX=afl-g++ allparserscheckfile -j8 \
    && install allparserscheckfile /json-parsers

RUN mkdir -p fuzz/input \
    && cd fuzz/input    \
    && wget https://gist.githubusercontent.com/EmilGedda/370e487cd658b61139b63d92059e73fd/raw/a3b7358f524b9b62af188707c985e8fc586a9997/seed.json

[...]
```

AFLFast was first run for approximately 3 days after which it crashed, due to running out of disk space. After upgrading to a larger storage space, it was left to run for approximately 4 days. 5,073 unique crashes of the parsing libraries occured during uzzing.

Every unique JSON-string output by AFLFast that caused a crash was saved to a file. At this point, these files were not sorted by the JSON-library that caused the crash.

### Classifying

### Analysis

## Results

## Final Thoughts

# References

- [Bohme, Marcel & Pham, Thuan & Roychoudhury, Abhik. (2017). *Coverage-based Greybox Fuzzing as Markov Chain*. IEEE Transactions on Software Engineering. PP. 1-1. 10.1109/TSE.2017.2785841. ](https://www.researchgate.net/publication/321987454_Coverage-based_Greybox_Fuzzing_as_Markov_Chain)
