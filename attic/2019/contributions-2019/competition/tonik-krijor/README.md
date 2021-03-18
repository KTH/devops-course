# Grand Fuzzing Challenge Submission

## Group members

- Toni Karppi (tonik@kth.se)
- Kristian Alvarez Jörgensen (krijor@kth.se)

## Introduction         
In this document we will explain our submission for the fuzzing competition task for the course DD2482. The task was to try to maximize the coverage of the 20 binaries in the GNU core utilities library by providing them with test cases. The test cases for each binary are included as lines in their respective text file. For example, the ls binary has a file ls.txt. Each line consist of command line arguments for the binary to be tested.

Repository with code can be found [here](https://github.com/tonik-krijor/fuzzer)

## Environment
We used Docker based on Alpine to create a reproducible environment. The docker image contains coreutils-v8.25 and uses gcc to compile it. We used the ‘--coverage’ flag when compiling the binaries, which allowed us to use the gcov tool to view the coverage for the binary. It also builds and installs radamsa (a simple fuzzing tool) and all the unix tools needed to run the various bash scripts that were created for the fuzzing purpose (gawk, bc, grep, bash, perl). 
## Evaluation
In order to evaluate the effectiveness of our fuzzing, we are using gcov to measure coverage. A basic `mark.sh` script was written that acts as a wrapper for measuring the coverage of an application based on arguments from a provided text file. `evaluate.sh` was also written to utilize `mark.sh` and invoke it from the docker container in order to evaluate every single binary and their respective text files, and outputs a final result. The result is calculated using grep and awk and outputs the total coverage for all the files associated with that binary. 

## Fuzzing
The fuzzing is done using radamsa, a general purpose fuzzing tool for unix-like operating systems. A small wrapper was built using bash (`fuzz.sh`), which takes a file with the arguments to fuzz and outputs the fuzed result. It contains a few default values (number of fuzzed elements per input, seed) that can be overwritten and tweaked. 
Generating initial test cases    
The first thing to consider when trying to get a high coverage is how we should get the program to exercise different functionality in the application. In command line applications, this is often done by providing flags to the application. To test happy paths, it made sense to try the different flags for the binaries, as documented in the ‘man’-pages.

However, it is not really enough to just try the different flags by themselves, since combining flags can exercise new functionality. For example, providing both ‘-l’ and ‘-a’ flags to ‘ls’, the program will need display the output in a long format, in addition to displaying the hidden files. This means that trying the combinations of flags should be considered. To facilitate the generation of test cases which consider the combinations of flags, we created a tool called mixemup. Naively it would have made sense to try all combinations of all flags. However, this is not practical, since this method suffers from combinatorial explosion. To combat this, we only consider combinations of up to three flags. This functionality is provided as a flag to the tool.

Further arguments where added manually, which is relevant for stuff like printf where the arguments aren’t expressed in the terms of flags. 
Pruning

There were a lot of test cases generated for the different binaries, and even more by the fuzzer. Many of these test cases would end up not contributing to the coverage, which is why it made sense to try to prune these redundant test cases. To determine which test cases to prune, we made use of coverage. If a test case increases the coverage for the binary, it is kept, otherwise it is discarded. This is done inside the `prune.sh` script, which runs each command, checks if coverage is increased and then acts accordingly. 

There is however a problem that had to be considered, which is that we are running binaries with unknown arguments, and we do not know if the command will get stuck waiting for more input, or the command may take a long time to execute, which we can’t afford. To prevent these scenarios, we added a timeout for each command. If it takes longer than one second to execute the command, then it is discarded.


## Search algorithm 
Using the scripts mentioned above, we would fuzz some input data, prune it and then repeat the process with whatever new commands were found to increase coverage. We quickly understood that this process could be automated, and thus `fzpr.sh` was born. For each program it takes an initial file with commands as input, as well as the number of generated fuzzes per command and the depth that it will in turn fuzz newly found commands that increase coverage. The depth parameter is there in order to have somewhat deterministic runtimes - a while loop would work as well. We also avoid fuzzing arguments that have already been fuzzed, and thus only focus on fuzzing new arguments. 

A potential improvement might be to continue to fuzz arguments that have been shown to generate successful fuzzes before as well, although it is important to remember that for each of these arguments the seed would have to be altered. 

## Conclusion and "Take Home Message"
Usually, fuzzing is done in order to find bugs. This task is a bit different, since we are using it to attempt to get good coverage. This project prooves that it is relatively simple to do so at a satisfactory level by chaining existing tools with bash.  

