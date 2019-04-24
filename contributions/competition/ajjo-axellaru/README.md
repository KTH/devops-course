# Grand Fuzzing Challenge 

## Group members
 
  - Arnthor Jonsson ajjo@kth.se
  - Axel Larusson axellaru@kth.se

## Introduction

This is our submission for the “Grand Fuzzing Challenge” for the course Automated Software Testing and DevOps (DD2482). The goal was to fuzz 20 binaries from the GNU coreutils 8.25 and compete with our colleagues in the course to see which group had provided the best coverage for the following binaries.

    /bin/cat
    /bin/cp
    /bin/date
    /bin/dd
    /bin/df
    /bin/dir
    /bin/echo
    /bin/false
    /bin/ln
    /bin/ls
    /bin/mkdir
    /bin/mktemp
    /bin/mv
    /bin/pwd
    /bin/sleep
    /bin/printf
    /bin/touch
    /bin/true
    /bin/uname
    /bin/vdir

## Tools

In order to get a reproducible environment, we used the [kthassert/fuzzing-competition-reference-build](https://hub.docker.com/r/kthassert/fuzzing-competition-reference-build) docker image. The image contains [coreutils-v8.25](https://git.savannah.gnu.org/gitweb/?p=coreutils.git;a=tag;h=4d1b3017f53da17bee470ff33b9e658f4e06972c) with detailed instructions in the [HACKING](https://git.savannah.gnu.org/gitweb/?p=coreutils.git;a=blob_plain;f=HACKING;hb=7d8adb20f6bb37ab8e922cca9ea367bea078b28c) file on how one can get up and running by setting the `--coverage` flag when compiling in order to view the coverage with [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html). 

### Getting Started

In order to get coverage from the src/ folder, we did the following steps

    $ sudo systemctl start docker                                                 # to start docker
    $ docker run -it kthassert/fuzzing-competition-reference-build:latest bash    # go into container
    $ cd coreutils                                                                # start fuzzing
    $ env RUN_EXPENSIVE_TESTS=yes env RUN_VERY_EXPENSIVE_TESTS=yes                # to run expensive tests
    $ env FORCE_UNSAFE_CONFIGURE=1                                                # so you can run as sudo
    $ ./bootstrap
    $ ./configure
    $ ./configure CFLAGS="-fprofile-arcs -ftest-coverage"
    $ make
    $ make check                                                                  # This runs the entire test suite
    $ cd src/
    $ rm *.gcda                                                                   # Delete gcov files
    $ {run inputs}                                                                # Example: $ ls -l
    $ gcov {binary}                                                               # Example: $ gcov ls

## Approach

While we tried some of the better-known fuzzing tools like [afl-fuzz](http://lcamtuf.coredump.cx/afl/) and [libFuzzer](https://llvm.org/docs/LibFuzzer.html) we either weren't able to make them work or we didn't get high enough coverage. We, therefore, concluded that while these tools are created for caching bugs by generating unusual inputs they weren't what we need so we decided to create our own script to pump out [man pages](https://linux.die.net/man/) information which we then manually edited. 

Most tests worked without to much trouble but some needed some tweaks. Our general approach was to try arguments and see if they contributed to an increase in coverage. This we did iteratively and noted the arguments which resulted in greater coverage. While we tested the commands we found on the help pages and the man-pages we also tested blank commands and commands that would purposely fail. 

This gave us decent coverage but in order to increase the coverage we decided to take a look a test in a newer version of [coreutils-v8.31](https://git.savannah.gnu.org/gitweb/?p=coreutils.git;a=tag;h=4d1b3017f53da17bee470ff33b9e658f4e06972c). While one could create a script to extract the inputs of the test suite we decided that since there were only 20 binaries that we would do that manually. This approach increased our coverage to a satisfactory level.

After we gathered all the inputs which contributed to an increase in coverage we ran 

    $ rm *.gcda

Then we ran our complete list of inputs again to see the final coverage score.    

Every file and directory that we added, changed or used during this process was carefully documented. For every binary that needs some file or folder we created a specific directory under files.

_For example:_

`cp` has its own directory under files called up so we can run 
    
    cp -dR files/cp/file files/cp/file1


## Take-home message

If you want a high coverage this a good approach, however, if you want to increase coverage from the original test suite while finding bugs this is not the correct approach. In that is the case, one should choose the path of a robust tool like [afl-fuzz](http://lcamtuf.coredump.cx/afl/) or [libFuzzer](https://llvm.org/docs/LibFuzzer.html).

