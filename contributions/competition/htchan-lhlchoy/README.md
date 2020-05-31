Grand Fuzzing Challenge 2020!
Member:
Chan Ho Ting (htchan)
Louise Hui Ling Choy (lhlchoy)

In this challenge, we use the American Fuzzy Lop (AFL) as the fuzzer to ffmpeg. We use the github repository alf-ffmpeg-opus as the starting point. Then we try to fuzze the ffmpeg by the same .opus files, but different codec (libopus) and target format (rm, mp3).

Used Tools
American Fuzzy Lop : A free software fuzzer that helps increase the code coverage of test cases with a smaller testing size. It will compile the ffmpeg code with adding some flag in the code for tracing the code coverage. Then the fuzzing is started by providing a simple test case. Then, trying to insert, reduce and modify bits in the input file to find out any case to check any exception happening and reduce the size of input test case to reproduce the exception. It will record the test case that cause exception for further debugging

afl-ffmpeg-opus : It is a docker file using afl fuzzer on https://lcamtuf.coredump.cx/afl/releases/ to fuzz the ffmpeg by inputting .opus audio file from https://people.xiph.org/~greg/opus_testvectors/ and transform it to wav format by pcm_s16le acodec

Search and Meta-optimization
We have tried to use AFLGo as an alternative fuzzer to AFL. But due to time constraints, we are unable to fuzz it thoroughly.



Customerization and Modification
We had made some modifications from the docker file. As we would like to fuzze the codec ability of ffmpeg, we had tried to change different codec and output format flags in ffmpeg. In our planning, we also decided to fuzze the ffmpeg with different input file formats like mp3, aiff and m4a, but we took too long for fuzzing on the opus files, we do not have enough time to fuzze different input file formats.

Take Home Message
Fuzzing is an advanced technique in testing as it randomly generates test cases and processes them to find any exceptions automatically. It may help developers find out the bugs they ignore. There are some things that people should consider before starting the fuzzing, which part or what abilities you want to test for. In this challenge, file encoding method and format transformation between different types are categories that we considered to test by fuzzing and we choose file encoding method as our focus. We think it is one that most probably exists some bugs that can be captured by fuzzing.
