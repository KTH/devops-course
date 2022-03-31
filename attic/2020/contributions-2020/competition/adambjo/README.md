# Fuzzing Competition Entry
Adam Björnberg (adambjo@kth.se)

## Getting started
The competition involved fuzzing a static binary of ffmpeg-4.2 compiled for ubuntu 16.04.
After a fair bit of googling I discovered that ffmpeg had been fuzzed many times before.
Googles AFL fuzzing tool was the most popular from what I could tell.
I also read that the winning team of last year's competition won using AFL, their [article](https://medium.com/@adamhasselberg/the-grand-fuzzing-challenge-a-devops-retrospective-fd89accb7ce0) about their experience was a great read and helped out a lot to get started.
AFL seemed like a great choice so I decided to use it for my fuzzing.

I didn't have any previous experience with ffmpeg or AFL (or any fuzzing for that matter), so the first thing I did was to set up a development environment in which I could try some stuff out.
The target binary were specifically compiled for ubuntu 16.04 and the AFL installation guide made it clear that their tool worked best on Linux.
I went ahead and set up a VM with lubuntu 16.04 using VirtualBox since I don't have any computer running Linux. Also, I figured installing lubuntu 16.04 would avoid any unecessary issues or disrepencies between my own results and the grading.

## About AFL
AFL (like most fuzzers) starts with instrumenting the program that you want to fuzz.
Instrumentation is about adding snippets to a program's source code so that the fuzzing tool (AFL in this case) can read execution paths and measure coverage.
Most fuzzers work by randomly flipping bits in the initial test cases to produce test cases that increase overall coverage.
AFL also works like this. What sets AFL apart is that it begins by performing an array of deterministic fuzzing steps that usually result in good test cases.
The deterministic fuzzing phase can be very time-consuming, so therefore it is important to keep initial test cases very small.
AFL can even start with almost empty test files and still create corpuses with good test coverage.

## Finding test cases
The most important aspect when fuzzing, according to most sources (and the AFL developers [themselves](https://github.com/google/AFL/blob/master/docs/perf_tips.txt)), is to have a good initial test corpus to begin the fuzzing with, so I figured this was a good first step, which it wasn't, more about this later.

After some more googling I found ffmpeg's [huge collection of sample files](https://samples.ffmpeg.org/) for testing.
I wrote a python program that crawled through the collection in order to find the smallest file of each format.
This was the first test corpus I used, but after some testing I came to the conclusion that most of the files still were too large.
I instead found the fate-suite test corpus [here](https://ffmpeg.org/fate.html), which is what the developers of ffmpeg use for their automated testing.
This could be downloaded with a shell script in the ffmpeg repository.
This corpus had a lot of small files, and I created another python program to extract the smallest ones similar to how I did before.

Here's a code snippet of the python program:
```python
def gather_samples():
    fex_dict = {}
    
    # fex = file extension, fex_dict stores list of files for each fex
    for s_name in os.listdir("fate-suite"):
        path = "fate-suite/" + s_name
        size = os.path.getsize(path)
        _, fex = os.path.splitext(s_name)
        fex = fex.lower()
        if fex == "":
            continue
        if fex not in fex_dict:
            fex_dict[fex] = []
        fex_dict[fex].append(Sample(path, size))

    small_samples = []
    for fex in fex_dict:
        small_samples.append(min(fex_dict[fex]))

    for s in small_samples:
        shutil.copy(s.path, "samples")
```

## AFL Workflow
### Instrumentation
AFL instrumentation is done by compiling the target binary with one of their custom C/C++ compilers (afl-gcc, afl-g++, afl-clang, afl-clang++).
For ffmpeg, this was done by setting the compiler in bash:
```
export CFLAGS="-Wall -g" && export CC=afl-clang-fast && export CXX=afl-clang-fast-fast++
```
Or by setting the compiler in ffmpeg's configure script:
```
./configure \
  --cc=afl-clang-fast \
  --cxx=afl-clang-fast-fast++ \
  --host-cc=afl-clang-fast \
  --ld=afl-clang-fast
```
I did both for good measure.

### Minimizing test cases
As previously stated, having small test cases is very important when fuzzing with AFL.
AFL provides two utilities for minimizing the test corpus, afl-cmin and afl-tmin.

- **afl-cmin:** removes files with the same coverage to produce a smaller corpus with the same coverage without modifying the files. Can be used to prune the initial corpus or the corpus created after fuzzing.

- **afl-tmin**: removes blocks of data from a file without lowering coverage.

afl-tmin is very slow, so its a good idea to start with afl-cmin. Might be worth running afl-cmin several times.

### Fuzzing
Fuzzing is then done using this command:
```
afl-fuzz -i init_tests -o findings/ -- /path/to/instrumented/ffmpeg <command>
```
I decided to fuzz the following command:
```
afl-fuzz -i init_tests -o findings/ -- /path/to/instrumented/ffmpeg -i @@
```

### Scaling
Fuzzing is computationally very expensive so you have to divide the work on several machines in order to be effective.

I created 32 ubuntu 16.04 VM instances on Google Compute Engine and divided the initial test corpus between the, ran afl-cmin, then afl-tmin, then afl-fuzz.
I then gathered all the output and ran it through a final afl-cmin.

### Take-home
- Start by examining the program you want to fuzz and find a good target.
- For AFL, use very small test cases, or use the -d option.
- Use some kind of orchestration for the cloud computing. Managing each VM instance manually was not fun.



