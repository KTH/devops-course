# Feedback proposal (Tutorial) for #1158 - Continuous benchmarking using Github Actions

I would like to give feedback on the tutorial about Continuous benchmarking using Github Actions by jhammarstedt


## Feedback

I have now provided the feedback, see PR #1358. Also included here below

---

## Feedback on Continuous benchmarking with Github Actions

Awesome tutorial and a really nice area of choice. The tutorial really expand the knowledge on setting up workflows. You are using great pictures explaining the workflow and some subtle funny images (always appreciated). I did decided to do the tutorial on Katacoda and it took about 20 minutes ( a bit more, but 20 is a good estimate). Took a while to setup github on katacoda, although can't blame you for that, turns out that it's my own fault, since my work apparently has enforced sso whenever i login from somewhere... It is nice that you provide two ways of doing the tutorial.

Below are some actionable points for you to consider on some of the steps:

### Step 1
Step one is clear and fairly concise.

A minor annoyance was that the config of email was set to a katacoda execute field, making execute with the wrong email, suggest that you change it into a copy-paste only, since there is no real point in executing that.

The permission script (chmod) seems more like a chore that has to be done, it does not really feel very relevant to the tutorial. if possible put in in a script that is executed when the step starts automatically instead.

I also tried the other option, to not write any code manually, however this caused problems, since all the files were committed the first time, making the outputs of the action a bit confusing since they were not what was said.

### Step 2
Nicely explained with a good image. Great that you take out parts of the bigger image you shown in the beginning, it made it clearer to see what part I was working with.

I have one complaint on this page that follows to some of the other pages. It's not really about the actual content. Rather katacoda. The formatting when copying the code is not correct, which made it a bit annoying to do. I guess one could rewrite it manually but I think it would be nice if you took a closed look at the formatting of it. The issue is consistent on most fields where you copy the longer texts. Works better when you copy the whole file once, maybe let the user copy the whole thing first and the explain everything. There is also a katacoda command to copy things straight into a file (check it out here https://katacoda.com/scenario-examples/scenarios/clipboard).

### Step 3
Good explanations and nice with links pointing to additional material. However, noticed that the content of the workflow file on top is different from the one at the bottom. I didn't notice this until the workflow failed when I pushed it, please fix that (missing "src/" prefixed in the python command).

### Step 4
Very clear images showing what todo, a nice addition would be to explain the steps shown in the log (how the relate to the steps in the workflow file) making it more intuitive why that subsection should be selected.

### Step 5
The steps are explained clearly, would be nice if you gave some more info about what python benchmark does (what measures it takes a.s.o), I know that there is a link, but a short inline explanation would be nice. Also suggest you add a note what the functions do and why you chose them (it is fairly obvious if you know python, but not everyone do) .

### Step 6
Same thing with the copying of code messing with the indentation, other than that the content is good. This is where I had an issue with a merge conflict though. Previous steps seems to have produced files that i had to pull before i could push it. Not sure if that was supposed to happen, if not, look into it. If it is on purpose, then I suggest you add a note about it.

### Step 7
Nice seeing the continuation of the image series and a clear and concise explanation about github pages. Since you say that the tutorial does not cover bs4, which is completely reasonable, but it feels weird to copy or manually write that code, if it is not explained. Maybe you can include that file automatically and only tell the user that it exists.

### Step 9
Awesome with a summary page, and it is really nice that you've used the image overview throughout the tutorial.

### Outro
Feel bad that I missed the easter egg, had to go back and try it. It was a really cool one, definitely subtle and fun. Maybe include some kind of hint earlier somehow, or just get the user to check out the scripts folder.

### Overall points
- There are a few spelling mistakes, make sure you read through carefully one more time.

Great work and felt like well spent time doing the tutorial. Definitely learnt something new, even though I was a bit familiar with github actions from the course automation task. Hope the feedback can help you make it even better! Best of luck with your final submission!

/ Simon

## Members
Simon Persson (siper@kth.se)

