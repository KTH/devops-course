# Hiding in Plain Sight - Python Obfuscation

A tutorial intended to teach what obfuscation is, why it's relevant and how to get started obfuscating, all in the Python programming language.

### Authors
* Balthazar West, bwest@kth.se, Github: balwes
* Christopher Winge, cwing@kth.se, Github: cwinge

### Why obfuscate?

Distributing your application comes with risks. Competitors may get their hands on it, copy your work and redistribute it as their own. Also, malicious users can find and exploit vulnerabilities for their own gain, sometimes compromising the privacy of innocent users.

Applications written in compiled languages like C++ are distributed as runnable binary files containing machine code. Binaries are verbose and difficult to read making them hard to reverse-engineer, especially for non-trivial applications that easily exceed tens of thousands of lines. This is unlike languages like Node.js and Python, where an interpreter runs the source code and executes it. Therefore the distribution of applications written in interpreted languages becomes a challenge when we want to hide the source code. Even when distributing Python's bytecode it's extremely easy to get back the source (see [uncompyle6](https://pypi.org/project/uncompyle6/)). What do we do? We obfuscate.

Obfuscation is simply a process of transforming code into less readable code. It is meant to increase the time and effort required to reverse-engineer, hopefully dissuading competitors and malicious users, but it will always be possible (for as long as PC users have access to look at the program's machine code). Obfuscation doesn't prevent reverse-engineering, it *impedes* it.

An example of this is [Dropbox](https://www.dropbox.com/) who created their own Python interpreter in combination with other techniques. However, this wasn't enough to keep it from getting cracked, [the Look inside the box repo](https://github.com/anvilventures/lookinsidethebox) has a tool that breaks the protection layers.

Is there actual demand for obfuscating Python? [Here's a list of Python software.](https://en.wikipedia.org/wiki/List_of_Python_software) Some of these don't need obfuscation, but the point is that there is plenty of Python software outside a server-side or open-source context (where obfuscation is not needed).

There's not a lot of information about who's obfuscating Python so we reached out to the developers of [PyArmor](https://pyarmor.dashingsoft.com/) and [Oxyry](http://pyob.oxyry.com/), two commercial Python obfuscators. The developer of PyArmor answered and according to him the following companies have bought licenses: NEC, Sony, Panasonic, Fujitsu, IBM, GE, 3DPrinter, Tencent and more. This indicates that Python obfuscation is used more commonly than what might be expected.

Obfuscation should be automated because it's too labor-intensive to do manually.  It can be part of an automated toolchain, for example between testing and distributing. This guide looks at a few tools that can be used, ranging from small educational tools to commercial products.

### Setup
[Go to the Katacoda Python playground.](https://www.katacoda.com/courses/python/playground) We recommend you keep it open alongside this guide. Feel free to use your favorite terminal instead but we assume you have the same setup.

For easy copying and pasting: Triple left click a command to select it, then copy and use Ctrl+Shift+V in the playground's terminal to paste and run it.

One thing we did encounter with Katacoda however is that we ended up with Docker or Jupiter VMs instead of the supposed Python a few times, if you use Katacoda make sure the Python version ``python --version``  is 3.6.7 or higher and that the root directory is empty. Refresh the page if this isn't the case. Furthermore, file contents don't always refresh so if something isn't updating, close and reopen it.

Download the python script that will be used to try out some of the different tools, it will do some simple whitespace counting in a string and print it, as well as some simple sqrt calculations and a class test with some calls to it.

``curl https://raw.githubusercontent.com/cwinge/Obfuscation-testfile/master/tutorial.py --output tutorial.py``

Alternatively manually download the file from this git directory.

You're all set!

### Intensio-Obfuscator

We will look at Intensio-Obfuscator first ([GitHub repo](https://github.com/Hnfull/Intensio-Obfuscator)). It has rudimentary features but is well documented so it serves as an introduction to obfuscating your own code. Unfortunately it's not available on pip so install it from the repo:

``git clone https://github.com/Hnfull/Intensio-Obfuscator.git``

``pip install -r Intensio-Obfuscator/requirements.txt``

The CLI should now be in the path `Intensio-Obfuscator/intensio/intensio_obfuscator.py`. Running it with --help lists the features, but these will all be explained below. Let's add some code to test with:

``mkdir intensio && touch intensio/hello.py``

Paste this code into hello.py:

    # Appends the string and returns the result.
    def add_strings(str1, str2):
        appended = str1+str2
        return appended
    
    string = add_strings("Hel", "lo!")
    
    print(string) # Should print "Hello!"

Verify the output using python:

``python intensio/hello.py``

Intensio-Obfuscator will always remove comments and blank lines. Additionally, you must give at least one of the flags {-rts, -ps, -rfn, -rth}. Let's see what -rts does:

``python Intensio-Obfuscator/intensio/intensio_obfuscator.py -i intensio -o obfusc -rts``

Look at the output in obfusc/hello.py. Comments and blank lines are gone as expected, but -rts also scrambles most identifiers, like variable and function names, making them a chore to read and understand. Let's try -ps:

``yes | python Intensio-Obfuscator/intensio/intensio_obfuscator.py -i intensio -o obfusc -ps``

*(The program will ask you if you want to remove the already-existing directory. We have piped it to ``yes | `` to answer for you.)* As you can see, additional logic has been added to add_strings. But none of it affects the program's behaviour, it's dead code in that sense.

-rfn scrambles filenames, which might be useful if your project is split into many files with descriptive names. It's still not that interesting so we won't try it. Let's try -rth:

``yes | python Intensio-Obfuscator/intensio/intensio_obfuscator.py -i intensio -o obfusc -rth``

This produces the most ridiculous output, but the process is quite simple. The feature just (1) stores the entire file contents in a string, (2) converts the string to a byte string, (3) stores the byte string in a variable, and (4) executes it. The exec() function reads the string which makes up our source code and executes it.

This is actually so easy to reverse we can do it from the python terminal:

``python -i obfusc/hello.py``

The python terminal does not close due to the -i flag which is what we want. Using the builtin locals() function we can look at the variable that stores our source code. We will use pprint to format the output nicely:

    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(locals())
    quit()

Paste the entire code snippet and press enter to run all the lines and exit the python session. Now, if you scroll up a bit there should be a variable that contains our source code.

Finally, there's an -mlen flag. It decides the length of all scrambled strings (eg identifiers and filenames). It can be set to {lower, medium, high} (default is medium) and can be useful to control the resulting file sizes because the scrambled variable names are quite long.

How much do the features increase file size anyway? We fed the program part of its source code (intensio_utils.py) and used all features except for -rth and the default -mlen. This 90-line, 3 KB program turned into 470 lines and 60 KB. But that's nothing because using -rth and the longest -mlen produces obfuscated code where the first row is 450 thousand characters long! The output makes sense actually because -rth basically assigns the entire source code to a single variable.

As a final note it should be clarified that Intensio-Obfuscator is limited. First, some of these features are quite easy to reverse-engineer (namely -rth). Second, the repo's README says that the obfuscation is weak when used alone and it mentions specific constraints.

Now that we have used an educational tool, let's move on to a professional tool.

### PyArmor
[PyArmor](https://pyarmor.dashingsoft.com/) is a CLI tool that is used to obfuscate python scripts, with various optional features available. The transformed script still works like a normal python script and can be executed as such, with the requirement of an additional module and a few extra runtime files. 

There is a free trial version of the tool, which has some limitations around maximum code length and numbers of functions, as well as that all trial installations of the tool use the same 1024 bit RSA key public capsule. It is available for purchase for the price of USD $56.25, which removes the previously mentioned limitation as well as provides a 2048 bit RSA key private capsule. The price tag might scare some people away, but if compared to e.g. [Oxyry](http://pyob.oxyry.com/) which is a relatively similar tool whose CLI tool cost a whopping USD $1998, it might be considered quite affordable. When we asked the author of PyArmor about how many licenses have been sold, we got the answers that there are about 500 registered users at this point (including many big companies mentioned in the first chapter). He also stated that there are about 60 github projects that are using PyArmor.

Time to give PyArmor a try, install it using pip

``pip install pyarmor``

Make a directory called pyarmor and copy the tutorial file into it, and then cd into that directory

``mkdir pyarmor && cp tutorial.py pyarmor/ && cd pyarmor``

To obfuscate our python script we now run

``pyarmor obfuscate tutorial.py``

Which creates a subfolder *dist* that contains the obfuscated version of the input script, as well as another subfolder *pytransform* which contains the required files to be able run the script. The obfuscated script now looks something along the lines of

```python
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'\x50\x59\x41\x52\x4d\x4f\x52\ … \xb7', 1)
```
The obfuscated script can be run exactly like normal

``python dist/tutorial.py``

To make distribution easier if wanting to run the scripts on other systems, it is possible to pack everything into a single executable through the follow two commands

``pip install pyinstaller``

And then

``pyarmor pack -e " --onefile" tutorial.py``

The executable file will now be inside of the *dist* folder, and we can test running to see that it now works as a standalone file

``dist/tutorial`` 

Which should produce the expected output. This file can now be sent to others and ran effortlessly, without them being able to decode it into its original form in an instant.
It is possible to go even further and have the script stop working at a set date and time with the license feature. Create an expired license and replace the old one with the commands below

``pyarmor licenses -e "2020-04-20" example.py``

``cp licenses/example.py/license.lic dist/pytransform``

Which prompts the error ``RuntimeError: License is expired`` if you try to execute the file again 

``python dist/tutorial.py``

In addition to this, it is also possible to bind the license to certain machines by binding one or multiple identification metrics, such as the hard disk serial number, the system's mac address or even an ip address. To check the system info the follow command can be used

``pyarmor hdinfo``

Which then can be used together with the *licenses* command as additional options in the following way

``pyarmor licenses  --expired "2020-04-20" --bind-disk "S1E08MVE" --bind-mac "02:42:ac:11:00:1f"  --bind-ipv4 "172.17.0.31" example.py``

Which would give an error if anything doesn’t match or if it is expired when trying to run the obfuscated script. This is it for [PyArmor](https://pyarmor.dashingsoft.com/), to read more about the tool you can click on the name to visit its website. It will briefly make an appearance in the Nuitka section of the tutorial.

### Nuitka
[Nuikta](http://nuitka.net/pages/overview.html) is a Python compiler written in Python. It takes Python source files, transpiles them to C and produces a binary with the help of a C compiler. This enables you to leverage the speed of C, Nuikta claims to be about twice as fast compared to regular Python. As a warning, compiling C with Nuitka doesn't strip away things like comments and assertions by default, making binaries easier to reverse-engineer. This behaviour can be changed using flags. Coupling Nuitka with other obfuscation techniques like PyArmor adds another protection layer, more on that later.

Enough about the technicalities, let's get our hands on some actual code. Install Nuitka with the following command

``pip install nuitka``

Make a directory called nuitka and copy the tutorial file into it, and then cd into that directory

``cd && mkdir nuitka && cp tutorial.py nuitka/ && cd nuitka``

We will now use the installed module to compile our test script

``python -m nuitka tutorial.py``

As seen in the current directory, it created a *tutorial.bin* executable as well as a *tutorial.build* folder that contains a bunch of files used during the compilation. Either take a look manually through the GUI in katacoda, or use the command below to take a look into the build folder.

``ls tutorial.build``

Run the executable to see that it is still working as intended

``./tutorial.bin``

To make the standalone file actually be independent on the local Python installation, the ``--standalone`` flag must be used

``python -m nuitka --standalone tutorial.py``

The resulting executable is now within the *tutorial.dist* directory, without any file extension, run it with

``./tutorial.dist/tutorial``

Not much work at all to get a fully standalone executable with increased performance as well as harder to reverse engineer compared to regular Python bytecode. Now lets try combining it with PyArmor.

Clean the directory using

``rm -rf dist tutorial.bin tutorial.build tutorial.dist``

And then run the command below to obfuscate the file. 

``pyarmor obfuscate --restrict 0 --no-cross-protection tutorial.py``

The ``-restrict 0`` and ``-no-cross-protection`` options are necessary, without those the resulting C program from Nuitka won’t run. Now we just use Nuitka as usual, but on the obfuscated file

``python -m nuitka dist/tutorial.py``

The resulting file will have to be copied to the *dist* folder before execution, as it needs the files in the pytransform folder that was created by PyArmor ot be able to run the script 

``cp tutorial.bin dist/tutorial && ./dist/tutorial``

Now we have an executable Python program that is obfuscated, compiled mostly into a C level program.

### End of the line

Obviously obfuscation comes at a filesize cost, but what about performance? To compare performance, a benchmark was run five times per tool as shown in the graph below. The benchmark file can be seen [here](https://github.com/cwinge/Obfuscation-testfile/blob/master/benchmark.py).

![](https://github.com/cwinge/Obfuscation-testfile/raw/master/performance.png)

As seen, there can be some pretty sizable performance hits to your script, depending on the tool of choice. The tools provide different levels of security and runtime differences, what's worth doing ultimately depends on the goal of the program and the decision on what to use isn't clear-cut.

We have now covered some useful tools for code obfuscation and to help against reverse engineering of Python applications. There are plenty more obfuscation tools out there to look at, but the majority are unmaintained, hard to install, or lack documentation and a good built-in ``--help`` page. There are also a few that only have paid versions and many of these are far from cheap.
