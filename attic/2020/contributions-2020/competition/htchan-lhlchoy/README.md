# Grand Fuzzing Challenge 2020!

## Member:

- Chan Ho Ting (htchan)
- Louise Hui Ling Choy (lhlchoy)

In this challenge, we make our own fuzzer to ffmpeg. We use the github repository. We aim to try as much codec, encoder, decoder as we can in this fuzzing.

## Used Tools / reference tools

We used python and referring to afl-ffmpeg-opus to make our own fuzzer.

Python : it is a scripting language, we use the subprocess library to run different commands by command line interface. We set timeout variable and receive the return code for result.

Afl-ffmpeg-opus : We had used it in our fuzzing at first, but we found that it takes a long time to fuzze, but not giving any result, we change to make our own script by learning the setting of the project. As we have no idea on what command to fuzz, we read the docker file and makefile and see what test and file they used to fuzz the ffmpeg. As we cannot download the test file which is downloaded in the makefile, we find another website for our initial test vectors.

ffmpeg : in our fuzzing, we use the ffmpeg file download and unzip from the kth box. It is a version 4.2 ffmpeg target to work in ubuntu 16.04.

We develop a dump, mutation base fuzzer, which will not check on the input format valid or not and we will generate new file base on the base file and other generated file. It is a python script for running the ffmpeg in the command line interface by the test file we search online. First, the python script will put the original file to ffmpeg without any changing and assert the return code. If the output return code is not 0, the command will be marked as “error command”, the command with return code 0 will be marked as “work command” and command takes more than 10s to execute will be marked as timeout command. After classifying commands, we will flip the bytes randomly from the test file and save it to another file. For the amend file, we test the work command on them only to make fuzzing process faster and able to reach more different file.

## Search and Meta-optimization

At first, we will classify commands into 3 types “worked”, “error” and “timeout”. Although the ffmpeg commands execute automatically and assumed to have no hanged case, we keep the “timeout” categories for any special case. 

After we fuzz the base case with commands, we will randomly flip some byte (as we are using the bytearray class in python to flip the flie) in the base file and save it as a new file and run the “work” commands from base file on the amended. We only run the “work” command because the “error” command should also give “error” and “timeout” keeps “timeout” even some byte is flipped. We think it cannot increase the code coverage or help us find any special case repeating the “error” and “timeout” commands on a similar file.

After we find different error commands and error files, we will minimize the error file size by processing it by ffmpeg with random bits reduced and keep same output result. To make the fuzzer more powerful, we develop a dump mutation base fuzzer, which will not check on the input format valid or not and we will generate new file base on the base file and other generated file.

## Customerization and Modification

We have tried different command when we fuzz the ffmpeg, we tried to change the format directly, change the format with specify acodec, save the ffmpeg result to file by default, let ffmpeg output the result to console directly but not saving it, let ffmpeg output the result directly and pipe it to a file. We found that the ffmpeg more likely to report error in the case that we change file to another format with specific acodec. We cannot find special behavior base on the output method so we decided to fuzze on the commands that change file to another format with specific formats and let result output to file by default, as it should be faster than output to console.


## Take Home Message

Fuzzing is an advanced technique in testing as it randomly generates test cases and processes them to find any exceptions automatically. It may help developers find out the bugs they ignore. There are some things that people should consider before starting the fuzzing, which part or what abilities you want to test for. In this challenge, file encoding method and format transformation between different types are categories that we considered to test by fuzzing and we choose file encoding method as our focus. We think it is one that most probably exists some bugs that can be captured by fuzzing.

