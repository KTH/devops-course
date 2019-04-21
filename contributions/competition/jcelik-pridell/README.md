# Grand Fuzzing Challenge

<p align="center">
	<img alt="Monkey doing fuzzy testing" src="fuzz-testing-monkey-img.jpg">
</p>

This report covers the solution to a school assignment. It was executed by Julius Celik ([juliuscc](https://github.com/juliuscc)) and Patric Ridell ([pridell](https://github.com/patricr)) The assignment was to perform fuzzing on the binary files from 20 commands from GNU coreutils 8.25:

-   /bin/cat
-   /bin/cp
-   /bin/date
-   /bin/dd
-   /bin/df
-   /bin/dir
-   /bin/echo
-   /bin/false
-   /bin/ln
-   /bin/ls
-   /bin/mkdir
-   /bin/mktemp
-   /bin/mv
-   /bin/pwd
-   /bin/sleep
-   /bin/printf
-   /bin/touch
-   /bin/true
-   /bin/uname
-   /bin/vdir

The fuzzing was performed with a custom fuzzing program, enhanced with intensive manual labour to achieve high coverage. The cusom fuzzer extracts meta-information from manpages, which it uses to generate different possible commands. This is not necessarily a good method to find as many bugs as possible, however the assignment requirement was to achieve as high test-coverage as possible.

## Attempts That Failed

American Fuzzy Lop (AFL) was recommended by course teachers, so our first attempt was to use AFL. Because of poor documentation and lack of tutorials, we struggled with installing AFL in a container for safe use. We also concluded that AFL was great for discovering bugs, but not necessarily for effectively enhancing test coverage, which was the actual assignment. Therefore AFL was abandoned.

KLEE LLVM Execution Engine (KLEE) is a symbolic execution tool with the purpose of automatically generating tests that achieve high coverage. KLEE was developed with GNU coreutils in mind. We followed a [tutorial](http://klee.github.io/tutorials/testing-coreutils) and read [documentation](http://klee.github.io/docs/). From this we could successfully perform tests, however the code coverage was vastly worse than the one achieved in the tutorial, even after extensive exploration of the KLEE API. Therefore we abandoned KLEE.

## Custom Fuzzier and Helping Tools

We created our own fuzzying engine, which we enhanced with manual labour. The fuzzyer used manpage parsing for generating commands to test. By testing valid inputs and testing every command option once, a good coverage can be achieved.

We wrote a script with Node.js that extracted meta-information from man pages for every command, and then extracted valid command options for every command. From this we achieved files where every line of the file provided a valid command, and by running all of these we could achieve quite good coverage. This does not test invalid commands, combination of command options, or interactions with files on the system though.

To extend the coverage we manually read manpages, and wrote purposely failing commands, and command option combinations that we thought would increase coverage. We also tried to write specific edge cases, and manually created and wrote commands to interact with files. To simplify this process we used docker that could help us test the commands in a safe environment.

```
# cat.txt from custom fuzzyer, based on meta-information extracted from man pages:

-b
-e
-n
-s
-t
-u
-v
```

```
# cat.txt after manually reviewing and adding command arguments:

files/temp_do_not_exist_cat.txt
files/temp.txt
-A files/temp.txt
-b files/temp.txt
-e files/temp.txt
-E files/temp.txt
-n files/temp.txt
-s files/temp.txt
-t files/temp.txt
-T files/temp.txt
-u files/temp.txt
-v files/temp.txt
--help
--version
--abc
-a
```

## Conclusion and Take-Home Message

The used method was not effective for finding bugs. It was however effective for achieving high coverage, as a very satisfactory coverage was reached. Usually high coverage is not a good metric, and this method should not be used in that case, however if high coverage is the goal metric, this method was a very effective option.

## License [![MIT license][license-img]][license-url]

> The [`MIT`][license-url] License (MIT)
>
> Copyright (c) 2019 Patric Ridell
>
> Copyright (c) 2019 Julius Recep Colliander Celik
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
>
> For further details see [LICENSE][license-url] file.

[license-img]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://github.com/juliuscc/fuzzy-challenge/blob/master/jcelik-pridell/doc/LICENSE
