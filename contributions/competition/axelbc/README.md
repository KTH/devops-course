# Grand Fuzzing Challenge 2020!
| | |
|-|-|
| **Name** |Axel Boldt-Christmas|
| **Email**|axelbc@kth.se       |
|**Github**|xmas92              |

## Introduction
There were four distinct strategies used here to generate the inputs to `ffmpeg`. 
 1. Targeted input generation using existing file samples
	 *  **Input-suite**: *Unique*, *Special*
 2. General Fuzzing using existing file samples
	 *  **Input-suite**: *afl-mux*, *afl-enc*
 3. General Fuzzing using modified source
	 *  **Input-suite**: *afl-fast*
 4. libFuzzer based input generation
	 *  **Input-suite**: *libFuzzer*

## Targeted input generation using existing file samples
This is the only part that did not use any fuzzing tools. Instead it consisted of downloading over 100 GB sample multimedia files. (Mostly from [MPlayer's sample archive](http://samples.mplayerhq.hu/) and the [FATE-suite](http://fate.ffmpeg.org/)). Every file was then automatically analysed using `ffprobe`. A script then used the information about the codecs each file used to generate the smallest subset of files that covered the same set of codecs as the whole suite. This resulted in the *Unique* input-suite. Every input is of the form:
```
-i <FILE> -f null -
``` 
The goal of this suite test as many decodings as possible while staying within the `1GB` limit. There are obviously many paths within each decoding that is not explored but it was a compromise.

The *Special* input-suite was instead generated from the `ffmpeg` options. A script generated options combinations of the following structure
```
-i files/all.mkv -c:v <VIDENC> -c:a <AUDENC> -c:s <SUBENC> -f null -
-i files/all.mkv -f <MUXER> /dev/null
-i files/all.mkv -pix_fmt <PIXFMT> -f null -
-i files/all.mkv -[vf|af|filter_complex] <FILTER> -f null -
```
Here `all.mkv` is a short file which contains both video, audio and subtitles.  The generated inputs where then run and analysed. Calls which caused error were manually refined to be more useful. (This was especially true for the filters, many examples were taken and added from the internet)

## General Fuzzing using existing file samples
[American fuzzy lop](https://lcamtuf.coredump.cx/afl/) (afl) was used here. A small corpus was selected consisting of a few small files (both audio, video and subtitles) and minimised using `afl-tmin`.  Two simple programs where then compiled, `fuzzenc` and `fuzzmux`.  Both programs took the fuzzed file as input and used a hash of the first `4k` bytes to seed the options for `ffmpeg` (`fuzzenc` selected different encoding combinations and `fuzzmux` selected different output muxers), then using these options and the input file it launched `ffmpeg`.  `afl-fuzz` was used to explore these programs.

The problem here is that even for small files in the corpus this was really slow (average less than 10 executions / second). There is a lot of overhead in the fact that we are opening closing extra files as well having one step of indirection when launching `ffmpeg`. These fuzzing sessions ran for over six days and only a couple of million executions were performed, it was not even able to complete one cycle. 

The `afl-fuzz` ran for as long as possible and the result was then minimised using `afl-cmin` and resulted in the *afl-mux* and *afl-enc* input-suite.

## General Fuzzing using modified source
To improve upon the executions / second a new `ffmpeg` was complied using a modified source. This used `afl`'s integration with `llvm`'s `libFuzzer` using the `afl-clang-fast` compiler. This gives you the ability to use `__AFL_INIT();` to set a point in the program where a forkserver can start the program (using COW mechanics to save allocation when using `fork-exec`). It also used `ffmpeg`'s `-i pipe:` option to read data from `stdin`.  The problem with just doing this was that `ffmpeg` halts the program from exiting for one second when using it. Which made fuzzing impossible. So instead the experimental persistent feature for `afl` + `libFuzzer` was used. Using `while (__AFL_LOOP(1000))` it creates a point in the program where it assumes the program has been reset (without exiting) to an initial state and can again accept input from `stdio`. While `ffmpeg`'s main loop is far from stateless this was still attempted. `ffmpeg`'s exit function was modified so that after running the cleanup functions it perform a jump back to the start of the program instead of exiting. Similarly to `fuzzenc` and `fuzzmux` the program used the first 20 bytes to decide on both encoding, demuxer and muxer options.

Using this approach the fuzzing could be done at over 500 executions per second (using a very small start corpus). Just running it for three days had it completing multiple cycles. Because the submission format does not allow for sending inputs via `stdin` to `ffmpeg` the inputs had to be converted into files. Because of this the paths that the fuzzer is exploring are different from those that are finally run.  This resulted in the *afl-fast* input-suite.

## libFuzzer based input generation
This was probably the most promising method explored but it was not feasible given the constraints on both the submission size and my available computation power. 

This used the `*_fuzzer.c` tools available in `ffmpeg`. They are able to generate inputs based on a specific demuxer or decoder targets. The *libFuzzer* input-suite was generated using two of these targets. 

The reason I did not use this more was because of the resources it would take and the size of inputs it would generate. There are around 500 different targets and after compiling all of them results in over `30GB` of binaries. Each target is great at exploring specific parts of `ffmpeg` and if I was able to have access to some vast (distributed) compute-time I would definitely use this approach or some similar gray-fuzzing like [AFLSmart](https://github.com/aflsmart/aflsmart). 

I looked at AFLSmart and decided agains trying to use it as well as it would be hard to generate something which I could do in time that also covers as much as possible. Something like AFLSmart would be great to explore the `ffmpeg` filter graphs as they have a distinct structure that general fuzzing has a hard time with.

## Conclusion
It is very hard to efficiently fuzz when the target is very large. Here the target was coverage of the whole `ffmpeg` project with its hundres of muxers, demuxers, encoders and decoders. Not to mention the filter node graph which in itself has almost infinit complexity. Trying to be very general (*afl-enc*, *afl-mux*) can make it slow, or inaccurate (*afl-fast*) , trying to split up the work and  target parts of the program (*libFuzzer*) can quickly require to many resources to be exhaustive and sometimes it is easier to use non-fuzzing techniques to achieve the goal (*Unique*, *Special*)

### Take Home Message
Fuzzing is a great tool (especially for security) if the goal is something targeted like discovering crashes, memory leaks or invalid logic and not necessarily just "coverage". And knowledge about the program or input structure can be leveraged to improve the effectiveness of the fuzzing.

## Appendix

### Results
Generated using the following script:
```bash
lcov -d . -z && \
time  while  read p; do echo  "$p" | xargs ./ffmpeg_g &>/dev/null; done < input.txt && \
lcov -d . --rc lcov_branch_coverage=1 -c -o coverage.info && \
genhtml --branch-coverage -o html coverage.info
```
|   input  | size | real time | branch | line | function |
|---------|------|-----------|--------|------|----------|
| Unique  | 390M | 1m45.739s |  20.2% | 29.4%|    25.9% |
| Special | 2.7M |14m32.953s |  16.8% | 26.9%|    28.0% |
| afl-mux |  55M | 8m56.042s |  11.4% | 16.9%|    16.3% |
| afl-enc | 131M |10m33.107s |  11.3% | 16.0%|    15.0% |
|libFuzzer|  57M | 1m58.278s |   6.1% |  8.3%|     8.5% |
|afl-fast |  30M |17m48.427s |  14.3% | 22.4%|    22.4% |
|Combined | 662M |41m38.631s |  38.5% | 55.9%|    50.0% |

