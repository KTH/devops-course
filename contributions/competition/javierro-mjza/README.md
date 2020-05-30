# The Grand Fuzzying Challenge 2020
 
## Team Members

- Javier Ron Arteaga (javierro@kth.se)
- Muhammad Jahangir Zafar (mjza@kth.se)

## Introduction
In this document we will explain how we approached and generated our submission data for the [Grand Fuzzying Challenge 2020](https://github.com/KTH/devops-course/tree/master/contributions/competition)
 
The binary to fuzz was 'ffmpeg' a tool created to process video and audio, it is very popular and famous for its countless features, and the great amount of formats supported.
 
## Description
 
For fuzzing our binary, first we picked a tool. That tool was the "American Fuzzy Lop" [AFL](https://lcamtuf.coredump.cx/afl/), a proven tool that relies on instrumentation, genetic algorithms and other very fancy features.
 
AFL suggests the use of an initial corpus as a seed for fuzzing. We gathered a considerable amount of samples from the internet, in as many different formats as we could get.
 
Setting up AFL and starting fuzzing with it is not very complicated. We had to recompile ffmpeg with "afl-gcc", an AFL utility that injects instrumentation in the binary during compile time. And that was basically it, after that we ran the "afl-fuzz" command with the right parameters and it started working.
 
Since AFL provides a way to [parallelize jobs](https://github.com/mirrorer/afl/blob/master/docs/parallel_fuzzing.txt), and take advantage of all available CPUs, the next step was to get our hands on the biggest and meanest computer we could get. With the help of free credit on a cloud provider for a decent machine and a bash script for automation we were reaching 100% CPU usage in no time.
 
Everything was great, except the results were not that great after a whole day of fuzzing. Here we realized that we had to solve several problems if we wanted to improve our results:
 
### Selecting a better initial corpus
 
The corpus that we initially selected had a few problems: The files were too big, and there were too many useless files in our corpus. This was solved in two steps:
1. We reduced the files, using ffmpeg to achieve the smallest size possible of each file while conserving most of their properties: format, number of streams, etc., but reducing time and quality
2. We used the AFL utilities `afl-cmin` and `afl-tmin` to reduce the size of our corpus even further and also remove useless files from it.
 
With a smaller corpus, AFL was able to perform a higher number of executions per second.
 
### Measuring coverage
 
For measuring coverage we used [afl-cov](https://github.com/mrash/afl-cov), a sister project of AFL which uses [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) and [lcov](http://ltp.sourceforge.net/coverage/lcov.php) to analize line coverage and generate reports. In order for this to work we needed the binary with debugging symbols and compiled with coverage flags, which we were able to create without much problems.
 
### Approaching the 'argv' vs 'file' dilemma
 
We noticed that fuzzing ffmpeg with AFL presented this difficulty:
 
ffmpeg has both a big number of supported formats for files, and a very big set of command line options, and AFL allowed us to fuzz _either_ the input file or the command line parameters (argv) _just not both at the same time_, which presented a challenge. We approached a solution for this in 2 fronts that luckily allowed us to achieve a somewhat higher coverage:
 
#### Approach 1: hash -f
 
This approach was based on this [talk](https://youtu.be/qTTwqFRD1H8?t=2268) which proposes randomly choosing the output format of an ffmpeg execution by:
 
1. Creating an array of supported formats.
2. Applying a hash function to the X first bytes of the input file.
3. Using the result of this hash function to pick a random entry of the formats array.
 
We programmed this inside the `ffmpeg.c` file, replacing the argv\[x\] corresponding to the -f option.
 
This allowed the fuzzer to modify the output format automatically as it mutated the input file, and optimistically for us, triggering different parts of the code, generating a higher coverage.
 
#### Approach 2: prepend argv
 
Note: this is very possibly the dirtiest hack we have ever programmed.
 
For this approach we used a single 1.5kb mp4 file as corpus.
 
This approach consisted of prepending the command-line arguments directly into the input file, in the form of a 256-byte block. These bytes were extracted inside the `ffmpeg.c` file, then parsed and injected into the argv array. This allowed AFL to fuzz the argv parameters and the input file at the same time.
 
The corpus file contained valid ffmpeg parameters in these first 256 bytes.
 
### Generating submission strings
 
AFL stores all generated inputs that triggered a different code path. To generate our submission strings and files from these files we performed 2 steps:
 
1. Execute `afl-cmin` again but now on the whole bulk of generated inputs in order to reduce the amount of files and keep the current coverage percentage.
 
2. Since we messed up with ffmpeg.c handling of the argv parameters, and given the format of the submission, we now had to create execution strings compatible with the real ffmpeg in order to complete our submission file.
  - For approach 1 we had to use the same hash function in order to get the correct output format.
  - For approach 2, for each generated file we removed the first 256 bytes and inserted them into the command line arguments, and saved the rest of the file as the input file.
 
This was automated by a couple of simple C programs, and a bash script to loop over each file, and create the submission strings.
 
## Conclusion
 
Given the results we obtained from the 2 approaches, we agreed that we should take another look to the initial corpus in order to reduce even further the size of the files and also generate interesting initial test cases for approach number 2, we think that this would help with the specially low coverage in the `libavfilter` sources. For approach number 1, we should check the hashing function because it seems that it was not producing a uniform output. These changes were not possible to implement within the deadline.
 
This challenge was indeed a challenge. We knew nothing about fuzzing before this experiment, but we ended up learning a lot of how fuzzing works(bit-flips, mutations, etc), how it's used(security bugs, memory bugs, etc) and several great and interesting projects like AFL and the OSS-Fuzz effort by Google.
 
The information about fuzzing tools is limited to non-specific tutorials and documentation. For AFL the documentation is provided as .txt files inside the repository, and even as comments on .h files. There is no chance of finding answers in forums like Stack Overflow, so our documentation reading skills were really put to test.
 
To finish we would like to state this challenge was a great learning resource and now we have a better understanding of fuzzing as a tool within the DevOps ecosystem and how it is used to create more secure and stable software.

