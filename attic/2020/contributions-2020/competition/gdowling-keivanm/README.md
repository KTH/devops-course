# Devops competion entry by Gdowling and Keivanm

## Names and emails

Gustav Dowling gdowling@kth.se phone nr: +46767050704

Keivan Matzineh keivanm@kth.se

## Introduction

We have been working on fuzzing the program FFMPEG v4.2. FFMPEG is tool used for media manipulation, for example converting video between different formats or scaling an image. Fuzzing is a software testing technique which involves sending misformed or invalid data in order to crash the program and therefore see when the program fails.

## Tools we looked at

### American Fuzzy Lop

American Fuzzy Lop (AFL) is a fuzzing tool which uses a genetic algorithm in order to increase the code coverage and then employs different strategies such as random bit shifts. 

AFL ended up not being useful for us as no matter how we set up our input files the fuzzer wouldn't find any new paths. It did however give us the code coverage for one test case, but we were unable to feed it multiple cases which made it pretty useless for analyzing our full test suite.

### Writing our own fuzzer using python

Since we know the structure of a valid input to ffmpeg is "ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}" we realized that we could create a test suite automatically that covers all the functionality of the program.

Our fuzzer picks a number of options randomly and places it at one of the correct positions. For example if the randomly picked option is "-vol" the fuzzer knows that it takes an integer as value and can be an option both for the input and output.

## What we did in detail

### input.txt line 0 - 350

One of the main functionalities of ffmpeg is converting media between different formats.

First we attempt to convert a small mp4 file into all the different formats available, ffmpeg has 350 different formats that we got from "ffmpeg -formats"

### input.txt line 350 - 700

Here we attempt to convert all the formats back into mp4. To do this we use the files generated in the previous 350 steps because that will give us 350 new files to try to put in the other end, converting from those formats and therefore using different code.

### input.txt line 700 - 90000

#### Using our fuzzer

Our fuzzer works as follows: first all options are collected from the source code of the file ffmpeg_opt.c in the fftools directory. This source code also has parameters for each options such as "HAS_ARG" which means that it takes an argument, "OPT_INT" which means the argument is an integer or "OPT_OUTFILE" which means that this is an output option. The options are associated with these parameters.

The randomization in the fuzzer works as follows: integer values are between 0 and 256, floats are between 0.0 and 1.0 as these are valid for most FFMPEG options, strings were at first a random amount of random lowercase and special characters, but the special characters caused a lot of crashes in the parser, we use this for a small part of the input to test what this is but not too much as we are afraid it may take too long for the machine running the tests as it stalled when we tried running a few of these. After a argument value has been associated with the option it is placed at a random valid "placement" according to the rules "ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}". The input file is constant, a 2 second mp4 with both sound and video, the output file is constant too. We use the "-y" global option to say "yes" to overwriting this output file.

#### Line by line

line 700 - 1000 has 1-3 random options where none of them take strings as values.

line 1000 - 1300 take 1-5 options and options that take strings as values are allowed

line 1300 - 2300 takes 1-10 options but none with strings as values

2300 - 2350 takes 1-6 arguments with random strings as values but allows special characters.

2350 - 90000 takes 1-6 options with random strings as values.

### Cleaning up

Some lines may be duplicated, the duplicates was removed using a simple webtool https://www.textfixer.com/tools/remove-duplicate-lines.php 

We decided to use ~90 000 lines assuming that each input takes 0.1 seconds and there are 3600 seconds in an hour we have pretty large margin. Some inputs may be parsed very fast as they get some kind of simple parsing error.

## Analysis

We have created a test suite for FFMPEG. The first 700 lines is not really fuzzing, since the inputs are not randomly generated. This important feature of FFMPEG, converting between formats, can probably not be tested using only random inputs. 

One major problem with our fuzzer is that the options that take strings, the random strings are very unlikely to be something specific that means something to the program. An option that takes a string as value is usually asking for some kind of specific string, which is almost impossibly unlikely to be generated randomly. This could be fixed if we for example had lists of valid strings for each option, but analyzing this code we could not do this automatically and doing it manually would be too much work for this competition.

Our approach is somewhat specialized for fuzzing FFMPEG, whereas something like AFL should work for testing many different programs as the input structure wanted for other programs probably wont be "ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}".

We also do not fuzz the actual input video files, we just fuzz the CLI. AFL for example can change a single bit of data in one of the video files and find some sort of bug that way. Another thing to note about fuzz testing in general is that it doesn't provide a test oracle in the sense that we could potentially for example convert a video file from .mp4 to .webm and have some sort of bug that doesn't crash FFMPEG, that would be unnoticed when running many of these inputs.

## Summary

Our approach of generating random options with random values to test a CLI program is a fine way to create a test suite with high code coverage but it has a few drawbacks. Intuitively the approach makes sense, if we use the program to do everything the program can do all the code should have been used. 

While going forward with this approach we started to realize some of the drawbacks, for example it is very hard to know what different values can go with the options, for example, a completely random string of 0-20 characters is extremely unlikely to be exactly "mandelbrot" (the name of one of the filters in ffmpeg). We did get around this somewhat since we could use the information in ffmpegs option parser code to automatically determine the datatype of the value associated with the option and if it's and infile, outfile or global option and place it accordingly. Another drawback is that we are not fuzzing the input files, and that we still have restrictions on the structure of the input for example only using integers between 0 and 256.

So we ended up quickly creating a test suite for FFMPEG with a technique that if done well should be able to test all the functionality, but can not find more intricate bugs for example misformed input files etc.


## Criteria

The solution is correctly formatted: I hope so...

The README well explains the used tools: I think we explained fuzzer we created pretty well, we even explained AFL which we tried to use but failed to get any meaningful results from.

The README well explains the employed search and meta-optimization: The search is the large amount of random inputs and the meta optimizations are choosing the right parameters for our fuzzer, for example trying with and without options with string values.

The README well explains the undertaken customization / modification: I think it's all explained, look at the line by line section. 

The README contains a good and concise take-home message: Our summary explains what our method can do and what it can't do.







