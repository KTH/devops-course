# Fuzzing of JSON parsing libraries /w Open-Source Contributions

## Introduction
This project aims to detect and possibly resolve bugs in a range of JSON parsing libraries using fuzzing.

Any bugs found during fuzzing will be reported as an issue to the corresponding FOSS-project. If the bugs are of a simple nature, we would like to resolve them and issue pull requests on GitHub.

By: Anders Eriksson & Emil Gedda

## JSON Parsing Libraries
The libraries we intend to fuzz are:

- [simdjson](https://github.com/lemire/simdjson/blob/master/README.md)
- [RapidJSON](https://github.com/Tencent/rapidjson)
- [sajson](https://github.com/chadaustin/sajson)
- [dropbox](https://github.com/dropbox/json11)
- [fastjson](https://github.com/alibaba/fastjson)
- [gason](https://github.com/vivkin/gason)
- [ultrajson](https://github.com/esnme/ultrajson)
- [jsmn](https://github.com/zserge/jsmn)
- [cJSON](https://github.com/DaveGamble/cJSON)

All of these libraries are hosted on GitHub under an open-source license and are open for contributions.

## Tools
The tools we intend to use are:

- [Docker](https://www.docker.com/)
- [AFLFast](https://github.com/mboehme/aflfast)
- [gcc](https://www.gnu.org/software/gcc/)
- [gcc AddressSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer)

This list is preliminary and subject to change.

## Goal

Ideally, we would like this project to result in one or more pull requests on GitHub resolving bugs found during fuzzing. If no bugs discovered are of a reasonably simple nature for this project to resolve, we will at least report any bugs we discover to aid the development of our chosen libraries.

### Deliverables

- Short report detailing our methodology, results, and any relevant discussion
- Docker image used for the actual fuzzing
- Links to any issues or pull requests created on GitHub as part of this project

## References

- [Bohme, Marcel & Pham, Thuan & Roychoudhury, Abhik. (2017). Coverage-based Greybox Fuzzing as Markov Chain. IEEE Transactions on Software Engineering. PP. 1-1. 10.1109/TSE.2017.2785841. ](https://www.researchgate.net/publication/321987454_Coverage-based_Greybox_Fuzzing_as_Markov_Chain)
