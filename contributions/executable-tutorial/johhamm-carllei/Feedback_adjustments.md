# Feedback adjustments

 **Extra fix**: Got a question from another student that did the tutorial about the possibility to benchmark the two functions simuntaniously. So modified the tutorial, scipts and benchmarks to compare both of them in the same workflow. Also added support for this in the GitHub pages table

### Step 1

A minor annoyance was that the config of email was set to a katacoda execute field, making execute with the wrong email, suggest that you change it into a copy-paste only, since there is no real point in executing that.
* **No need to have specific user email so added defaults that are configured automatically in the beginning**

The permission script (chmod) seems more like a chore that has to be done, it does not really feel very relevant to the tutorial. if possible put in in a script that is executed when the step starts automatically instead.

* **Fixed by running the clone and permissions as a script beforehand.**

I also tried the other option, to not write any code manually, however this caused problems, since all the files were committed the first time, making the outputs of the action a bit confusing since they were not what was said.

* **Fixed by adding a disclaimer that the option 2 would not allow to run the partial workflow**

### Step 2
I have one complaint on this page that follows to some of the other pages. It's not really about the actual content. Rather katacoda. The formatting when copying the code is not correct, which made it a bit annoying to do. I guess one could rewrite it manually but I think it would be nice if you took a closed look at the formatting of it. The issue is consistent on most fields where you copy the longer texts. Works better when you copy the whole file once, maybe let the user copy the whole thing first and the explain everything. There is also a katacoda command to copy things straight into a file (check it out here https://katacoda.com/scenario-examples/scenarios/clipboard).

* **Fixed by only giving one snippet that will be formated correctly instead of dividing them up** 

### Step 3
The content of the workflow file on top is different from the one at the bottom. I didn't notice this until the workflow failed when I pushed it, please fix that (missing "src/" prefixed in the python command).

* **Fixed by correcting the paths**

### Step 4
A nice addition would be to explain the steps shown in the log (how the relate to the steps in the workflow file) making it more intuitive why that subsection should be selected.

* **Fixed by adding a explanation for why each step exists in the log**

### Step 5
Would be nice if you gave some more info about what python benchmark does (what measures it takes a.s.o), I know that there is a link, but a short inline explanation would be nice. 

* **Fixed by adding a section about benchmarking and what it outputs**

Also suggest you add a note what the functions do and why you chose them (it is fairly obvious if you know python, but not everyone do) .

* **Fixed by adding comments explaining the purpose of the functions in the benchmarking.py script.**

### Step 6
Same thing with the copying of code messing with the indentation, other than that the content is good. 

* **Fixed by adding explanation and a fully formatted snippet at the end**

This is where I had an issue with a merge conflict though. Previous steps seems to have produced files that i had to pull before i could push it. Not sure if that was supposed to happen, if not, look into it. If it is on purpose, then I suggest you add a note about it.

* **Fixed by adding note about merge conflict**

### Step 7
Since you say that the tutorial does not cover bs4, which is completely reasonable, but it feels weird to copy or manually write that code, if it is not explained. Maybe you can include that file automatically and only tell the user that it exists.

* **Fixed by adding the generate_output.json file so user won't have to do it**

### Outro
Feel bad that I missed the easter egg, had to go back and try it. It was a really cool one, definitely subtle and fun. Maybe include some kind of hint earlier somehow, or just get the user to check out the scripts folder.

* **Added a little note on page 8 to again remind the user to check the script folder, still want it to be somewhat discrete and subtle**

### Overall points
- There are a few spelling mistakes, make sure you read through carefully one more time.

* **Looked through the full text again and ran every page through a spelling check**
