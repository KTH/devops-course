# Grand Fuzzing Challange 2020!

This report explains our solution to the fuzzing challange in the course [DD2482 Automated Software Testing and DevOps](https://github.com/KTH/devops-course).

[Fuzzing](https://en.wikipedia.org/wiki/Fuzzing) is about automatically provide un-expected, random, or invalid input to a computer program with the goal to detect anomalities and bugs. Fuzzers are often used to test a program and detect errors, but in this challenge the goal was to create as large code coverage of the program as possible. Due to this, the fuzzing approach in this assignment is not exactly the same as normal fuzzing.

### Members:
Stina Långström (stinalan@kth.se)

Tommy Samuelsson (tommysam@kth.se)

## Assignment

The assignment was to submit a solution for fuzzing testing on a binary, with the goal of achiving as high code coverage as possible. The fuzzing was done on the static build of FFmpeg 4.2, and a [docker image](https://hub.docker.com/r/kthassert/fuzzing-competition-reference-build-ffmpeg42) of that build was provided together with the static binary with debugging symbols (ffmpeg_g). 

The rules for the competition is that run time may not exceed one hour and inputs may not be larger than 1GB. Other than that, we are free to do whatever we want (as long as we follow the [code of honor](https://www.kth.se/en/eecs/utbildning/hederskodex), of course).

## Approach

### Initial approach
The work environment was a pre-setup docker image with a special FFmpeg binary, allowing it to track/count code-covrage. Since we both were new to the world of fuzzing and docker, we started with researching.

We found that a strongly recommended tool for this task was AFL ([American Fuzzy Loop](https://github.com/google/AFL)).
AFL is a brute-force fuzzer that mutates the inputs to create new tests to the program. Since AFL is good at fuzzing binaries we decided early on that we wanted to try it out. 

We soon realised that instrumenting our FFmpeg binary for use with AFL was harder than anticipated for two beginners. [AFL](https://github.com/google/AFL) has a good and explanatory readme but we obviously did something wrong. Because of that, we decided to create our own fuzzing tool. With this approach we anticipated that we might not get as good coverage as with a tool, but we knew that we would at least have some input to submit in the end. 


### What we did

To create our own fuzzing tool for the FFmpeg binary we first started reading the [documentation](http://ffmpeg.org/documentation.html) to get an overview of FFmpeg. We soon realised that FFmpeg is a file convertion and modification tool and that we could get lot of covrage by simple converting a file format to another, which is what we started with. We generated commands that would convert a file (.mov) to every available format that FFmpeg supported. 

To generate commands we made a tool to create permutations in order to reach more branches in the code.
The idea is, given a command, that the program helps create versions of it, doing the "busy work" work for us. An example of this woud be convert a file from format A -> B. The tool would output a list with B -> A, A -> C, C -> D and so on, to incrasse the covrage.

In order to get this to work, we created help utilities for our fuzzing tool to mange large text. The tool hade some basic capabilities like reading and writing to text files. 
It also helped us modifying large clusters in text files, by specifying parameters like row numbers and words etc.

To make our fuzzing tool more general we used the ```-help``` command of FFmpeg, which listed all the main functions that it supports.


```
Getting help:
    -h      -- print basic options
    -h long -- print more options
    -h full -- print all options (including all format and codec specific options, very long)
    -h type=name -- print all options for the named decoder/encoder/demuxer/muxer/filter/bsf
    See man FFmpeg for detailed description of the options.

Print help / information / capabilities:
-L                  show license
-h topic            show help
-? topic            show help
-help topic         show help
--help topic        show help
-version            show version
-buildconf          show build configuration
-formats            show available formats
-muxers             show available muxers
-demuxers           show available demuxers
-devices            show available devices
-codecs             show available codecs
-decoders           show available decoders
-encoders           show available encoders
-bsfs               show available bit stream filters
-protocols          show available protocols
-filters            show available filters
-pix_fmts           show available pixel formats
-layouts            show standard channel layouts
-sample_fmts        show available audio sample formats
-colors             show available color names
-sources device     list sources of the input device
-sinks device       list sinks of the output device
-hwaccels           show available HW acceleration methods
...
```
By this command we could easily find out which filters, encoders, decoders etc. that our version supported and could work our way forward from that.



**To summerize what we did:**

* Generated commands for the core functionality of FFmpeg. This includes for example to convert files to other formats, commands to apply different filters or commands to use all available encoders and decoders.
* Browsed through the documentation and used all the pre-defined commands. Some of them needed to be manipulated a bit to fit our submission, which had to be done manually.
* Observed the coverage and removed commands that did not improve the coverage.



## Customization and optimization

While generating inputs to FFmpeg that would improve the coverage we did a lot of customization and optimizations of the inputs as well.

We realised quickly that valid commands generated significantly larger improvements in coverage than commands that failed. Because of that we did not randomly combine commands, we only used commands we got from the documentation or exploration of the internet, since they would have much larger probability to be successful. We also realised that it was more beneficial for the coverage to have different commands, than using different parameters to the same command. By this fact we generated new commands instead of tweaked ones.

Since fuzzing is about providing a lot of commands randomly to a program, many of our commands does not work correctly. We observed that the coverage would improve even if the command would fail eventually, hence we kept failing commands and allowed out tool to generate new ones as well. 

To optimize the execution time we modified our provided files. We lowered the resolution and the framerate to create very small files that only contained a few images. The other formats are created from the orginal .mov file in each run, so they got the optimization autmatic as well. By that optimization we improved the execution time by about 50%. 

A customization we wanted to do, but did not, was to enable more libraries. In our build in the docker we lacked a lot of libraries, which made it impossible to run several of the commands. To enable more libraries we needed to pass the ```--enable-”library-name”``` to ./configure. That would configure our local build, not the one used when grading. By this fact we ignored all the libraries that were not configured in our build, which might have been a mistake since more libraries would enable us to run a lot more commands and thereby increase coverage.  

## Future work

We believed that we would get a larger coverage if we would use an existing fuzzing tool. From the last year contributions we realised that the best aproch is the combination of your own tool, an known tool and manual labor. If we had the more time, we would focus on that, since we think we probably would have gotten a more satisfactory result.

We would also add more files as input, preferrably more uncommon formats. That would probably enable us to run more functionalities of FFmpeg, which would improve the coverage.

## Tools

### Docker

The course administrators provided us with a docker image consisting of the static build of FFmpeg together with one with debugging symbols, ffmpeg_g. We used this container throughout the assignment to run our commands agains ffmpeg_g and analyzed the coverage. 

### DynamoRIO
[DynamoRIO](https://dynamorio.org/dynamorio_docs/) has a [coverage tool](https://dynamorio.org/dynamorio_docs/page_drcov.html) that we used to examine the change in coverage for our commands. With this coverage tool we were able to observe the change in coverage for every command we added. The tool can also create a coverage report that shows which line of the source code our inputs uses.

How to use DynamoRIO:

1. Download DynamoRIO from [GitHub](https://github.com/DynamoRIO/dynamorio/wiki/Downloads) into your docker container, we used ```DynamoRIO-Linux-7.1.0-1```. Once downloaded you can run all the binaries from the command line.

2. Generate a log file (drcov.SOMETHING.log) for an input

```/root/.../DynamoRIO-Linux-7.1.0-1/bin64/drrun -t drcov -- /root/.../ffmpeg-build-script/packages/ffmpeg-4.2/ffmpeg_g SOME INPUT```

3. Process the log-file into a lcov format, saved in the coverage.info file

```/root/.../DynamoRIO-Linux-7.1.0-1/tools/bin64/drcov2lcov -input ./drcov.SOMETHING.log -output coverage.info```

To process several log-files at the same time (generating a coverage report for all commands), use:

```/root/.../DynamoRIO-Linux-7.1.0-1/tools/bin64/drcov2lcov -dir . -output coverage.info```

4. Generate a coverage report

```/root/.../DynamoRIO-Linux-7.1.0-1/tools/bin64/genhtml --ignore-errors=source coverage.info```

Now you will have a coverage report named index.html.


## Take-home message

We struggled a lot in the beginning since both of us were totally clueless of what to do. None of us had any experience with neither docker or any fuzzing tool. But we felt like this was a very important topic to learn and decided therefore to give it a serious attempt. Even if we are not that satisfied with our final coverage, regardless of a high or low result, we are very glad we didn't miss out. This has been a great learning experince and we encourage future student to take on this challenge! 
