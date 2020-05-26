# GNU Coreutils Fuzzer

![Fuzzy, comfy, pups.](./files/fuzzy_comfy_pups.jpg)

## Introduction

This repository contains a fuzzing tool for the [GNU Coreutils](https://www.gnu.org/software/coreutils/) software suite and was developed to participate in a fuzzing competition as part of the graduate course *DD2482 Automated Software Testing and DevOps*.

This project was made in April 2019 by Anders Eriksson & Emil Gedda at *KTH Royal Institute of Technology*. The source repository can be found at https://github.com/EmilGedda/kth-devops/tree/master/fuzzing/argv_fuzzer.

## Tools Used

Here are some brief explanations of tools we used to analyze our progress.

### Docker

We used Docker to set up `gcov`, `lcov`, as well as to compile the Coreutils. This was done so that we could easily test our fuzzing coverage on any machine, regardless of `glibc` or built-in `coreutils` versions.

### gcov & lcov

To gauge our progress, we used `gcov` to analyze coverage and `lcov` to visualize the data from `gcov`. `lcov` aggregates gcov coverage reports and together with `genhtml` these reports can be made into static html file where the annotated source code will be highlighted depending on coverage.

### GCC

The GNU Coreutils are compiled as specified in the `Dockerfile` using GCC:

```
RUN cd coreutils                                                            \
    && ./bootstrap                                                          \
    && ./configure CFLAGS='-Og --coverage -Wno-error=maybe-uninitialized'   \
				   LDFLAGS='-lgcov'                                         \
	&& make clean                                                           \
    && make -j4 src/cat   src/cp     src/date  src/dd     src/df    src/dir \
			    src/false src/ls     src/mkdir src/mktemp src/mv    src/pwd \
				src/sleep src/printf src/touch src/true   src/uname src/ln  \
				src/echo src/vdir
	
```

This compiles coreutils with coverage reporting i.e. linking with `gcov`.
## Python Script

After the tools were set up properly to analyze fuzzing coverage, a Python 3 script was developed. The script parses a YAML-file of formatted data regarding the utils and what options they accept. Using this data and a set of mock data found in `files`, it picks random options and arguments for each util.

For utils with very specific behaviour, such as `true`, or `sleep`, commands are hardcoded in `data/custom_lines`.

The fuzzing script thereafter randomizes a thousand different combinations of all possible flags (with some restrictions). 

### Usage

This script has only been tested on Python 3.7.3.

This script is dependent on [PyYAML](https://pyyaml.org/) used to parse the YAML-file. This can be installed using `pip`:
```bash
$ pip install --user pyyaml
```

The script is run by running `fuzz.py`:
```bash
$ python fuzz.py
```

Files are written to a new folder in the current working directory `out`.

### Options format YAML-file

We decided early on to write down all available options for each tool in some kind of easily parseable and editable markup language.

The GNU Coreutils manual was was studied and all tool with their corresponding options and accepted arguments were stored in YAML-format.

Every tool contains the following key-value pairs:

|Key|Value|
|---|-----|
|`noOfArgs`|List of accepted number of arguments.|
|`paramFormat`|Option format for options that accept a parameter|
|`optionFormat`|Option format for options that do not accept a parameter|
|`options`|List of options. If an entry is a list, each entry features synonymous options. If an entry is a key-value pair, the option accepts parameters and each value is an accepted parameter. 

#### Example YAML for `mktemp` util
```yaml
mktemp:
  noOfArgs: [0, 1]
  paramFormat: "-{}={}"
  optionFormat: "-{}"
  options:
    - [d, -directory]
    - [q, -quiet]
    - [u, -dry-run]
    - -tmpdir:
      - ~
      - dir
    - -suffix:
      - ~
    - [t]
```

### Common Options

There exists three common options for all GNU Coretutils:

|Option|Description|
|------|-----------|
|`--help`|Print a usage message listing all available options, then exit successfully.|
|`--version`|Print the version number, then exit successfully.|
|`--`|Delimit the option list. Later arguments, if any, are treated as operands even if they begin with `‘-’`. For example, `‘sort -- -r’` reads from the file named `-r`.|

Out of these, `--help` and `--version` where added to each utils option in the `Util` class in the following lines of code:

```python
def addCommonOptions(self):
  help = Option(["--help"], "{}")
  version = Option(["--version"], "{}")
  self.options.add(help)
  self.options.add(version)
```

## Discussion

### Results

The results of our final run:

|Util|Coverage|
|----|--------|
|cp|53.7%|
|date|71.52%|
|df|72.15%|
|dir|0.0%|
|echo|65.74%|
|false|100.0%|
|ln|35.339999999999996%|
|ls|79.52%|
|mkdir|56.99999999999999%|
|mktemp|86.05000000000001%|
|mv|57.98%|
|pwd|36.08%|
|sleep|67.27%|
|printf|26.56%|
|touch|54.0%|
|true|100.0%|
|uname|90.72%|
|vdir|0.0%|
|**TOTAL**|66.34%|

### american fuzzy lop (AFL)

At an early point in the project, we researched using AFL for the competition. We quickly realized the way AFL works would be incredibly inefficient for maximing coverage of the GNU Coreutils. This however inspired another assignment of ours; fuzzing commonly used JSON-parsers.

### Ideas for Further Development

There are a few options we would've liked to develop more intrinsic fuzzing for. These include but are not limited to:

- Anything using the `printf` format
- More proper fuzzing of `dd`
- Fuzzing of `chmod` octal syntax

# References

[Docker, Inc. (2019), *Docker Website*](https://www.docker.com/)

[GNU Project (2019), *gcov—a Test Coverage Program*](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html)

[GNU Project (2019), *Using the GNU Compiler Collection (GCC)*](https://gcc.gnu.org/onlinedocs/gcc-8.3.0/gcc/)

[GNU Project (2019), *GNU Coreutils Manual*](https://www.gnu.org/software/coreutils/manual/coreutils.html)

[Michał Zalewski (2019), *american fuzzy lop*](http://lcamtuf.coredump.cx/afl/)
