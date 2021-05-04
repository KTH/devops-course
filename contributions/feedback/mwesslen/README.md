# Feedback #

## Members ##
Markus Wesslén (mwesslen@kth.se), Github: [m4reko](https://github.com/m4reko)

## Proposal ##
I plan to do feedback on #1025

## Execution ##

I provided feedback on [#1332](https://github.com/KTH/devops-course/pull/1332). It can be seen below:

---

# Feedback
Author: Markus Wesslén (mwesslen@kth.se)

## Overall
- This tutorial is nicely put together and the chosen platforms and tools work well together.
- The time estimate is good. I managed to do everything in just under 20 min even though I had to restart one time early on due to some problems with Play-with-Docker.
- The instructions are divided into logical steps and most of the instructions are easy to follow.
- Its good that you have an introduction and some sort of concluding text but those parts can be improved. More on that further down.
- Sometimes it's distracting to manage the three tabs that are needed for this tutorial but I guess that's hard to do anything about with the tools you chose. In [Katacoda](https://www.katacoda.com/), that I used for my tutorial, you can have everything in the same browser window and even have the TeamCity web interface in the same window.

## Sections
### Introduction
- It's nice that you include an introduction but I feel that it falls short in the content. In an introduction I want to be intrigued and get some background on whats included but your intro is purely technical. I, that have never encountered TeamCity before, have no clue what I'm going to learn after your introduction which also makes it harder to grasp the steps the first tie you work through them. Give some background on TeamCity, tell me what its used for and make it interesting so that i want to fulfil the tutorial.
- It good that you describe your tools (like Play-with-Docker) in the intro but I feel like the creation of a new instance belongs in the first step.
- Your instructions on how to copy and paste does not work on my mac but good old `cmd-c` `cmd-v` works fine. Maybe you don't have to include this since it's pretty basic? If it's more complicated on Windows, you can specify the operating system at least.
- The folder creation also belongs in it's own step according to me.

### Step 1
- This part is very clear and straight to the point which I like.
- The explanation of all the command flags for `docker run` is great to have but maybe a bit verbose. You can always reference the docker manual here if the reader want to know more. It feels like some of the parts are outside the scope of this tutorial.
- It's awesome that you include the commands `docker images` and `docker ps` which makes it easy to check one's work and also gives some more insight on how docker is working.

### Step 2
- This step is also clear and includes a lot of pictures of the GUI which makes it easy to follow. You could maybe have used some sort of graphics software (like Paint or [GIMP](https://www.gimp.org/)) to mark the relevant buttons or fields in the pictures.
- The tips are a nice addition but it would be awesome if you added some resources/links here pointing you to blogs or manuals for further reading. Some quick Google searches led me to [this link](https://www.jetbrains.com/help/teamcity/integrating-teamcity-with-docker.html#Docker+Disk+Space+Cleaner) which could maybe be added in your first tip.

### Step 3
- Here we suddenly introduce an agent and I would have loved some background on why we have Agents connecting to our server and what there respective roles are. After some quick reading I understand that it is good if we want to parallelise our builds. A very short description on this either here or in the introduction would be very nice.
- It's good that you only describe the new command flags here. I think all of the are relevant.

### Step 4
- For me it took some time before the agent showed up in this step after starting the agent in the terminal. This made me a bit confused and it would be nice if you were given a heads up on this in the initial part of this step.
- I also missed pictures of some of the popup dialogs from the GUI in this step which also halted my progress a bit. Pictures, preferably with markings for the important buttons, would be awesome.

### Step 5
- You could specify here also that it takes some time before this part is done even if it's much clearer here that something is happening and that you should probably wait.
- Here you also explains that TeamCity can do more than this which is intriguing but a follow up with a link to some resource would be awesome.

### Conclusion
- It's very nice that you include a concluding part but I feel like the content are lacking here in the same way as in the introduction. You provide a short summary of what we learned which is nice but it feels like repetition from the intro since it's presented in a very straight forward way. Wrapping it in some more descriptive and concluding paragraphs would improve the feeling.
- I would also say that this is a perfect place to put even more interesting resources (which I am sure there are lots of) and a call to action to dive deeper into the subject or something like that.

## Summary
In summary this is a very nice tutorial that is easy to follow and have a very clear goal. It makes use of very nice tools and platforms to present and execute the material which is always a plus. The average developer would have no problems executing all the steps and getting TeamCity to run with Docker.

However, it lacks a bit in the introduction and conclusion which both would need some more background, resources and less technical descriptions. This would also help the user to grasp the rest of the content quicker since the tutorial right now contain very little description on what TeamCity is and how it is used.

Overall, you have done a very nice job on this tutorial and I look forward to see your improvements.
