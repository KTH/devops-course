# Demo submission: Chaos testing in a deployed environment

## Member 

Niklas Wessman (nwessman@kth.se)

Github: [nwessman](https://github.com/nwessman)

## Description

This demo shows how to use DevOps practice **Chaos engineering** to conduct **Chaos testing** in a deployed environment to test the robustness of the system. This demo includes a simple system and its usage and then go through the steps of setting up and conducting Chaos tests on the system while explaining the benefits of the practice. The tool used for chaos testing is **Chaos Toolkit**.

## Demo Video

[Chaos Engineering Demo using Chaos Toolkit](https://youtu.be/6Oq9Zq6DVeg)

## Demo code

[Chaos Engineering Demo](https://github.com/nwessman/Chaos-Engineering-Demo)

## Easter Egg

Switch to French subtitles for a fun time! :tada:


## Grading - I strive to meet the following grading criteria

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The demonstration is clearly motivated (why it matters for Devops?) | :heavy_check_mark: Yes |  | Testing systems robustness is an important DevOps problem. |
|The demonstration is difficult to do | :heavy_check_mark: Yes |  | :heavy_check_mark:  Had to create my own system. |
|The demonstration is original | :heavy_check_mark: Yes |  | :heavy_check_mark: The are less than 10 demos on the topic on Internet - I could only find  ~ 5 showing the specific tool Chaos Toolkit. |
|The video is sublime (eg visually appealing) |:heavy_check_mark: Yes, if you like sharks! 🦈  |  | 🦈  Excellent narrative - Incorporated animations which explains the tests |
|The video contains an [easter egg](https://github.com/OrkoHunter/python-easter-eggs) | :heavy_check_mark: Yes, switch to French subtitles for a fun time. :tada:  |  |  |
|There is a code repo to run the demo  | :heavy_check_mark: Yes |  | :heavy_check_mark: [Code repo with a solid readme](https://github.com/nwessman/Chaos-Engineering-Demo) |
|The video must contain subtitles which are clear and in proper English |:heavy_check_mark:  Yes |  | :heavy_check_mark:  Clearly understandable voice over |
|The video includes a take-home message | :heavy_check_mark:  Yes |  |:heavy_check_mark: Actionable takeaway - Start using Chaos Testing on your systems. |


## Changes made after feedback

[The feedback I received can be viewed here!](https://github.com/KTH/devops-course/pull/1498)

The biggest point of feedback that I recieved was that the voice volume was inconsistent at times:

>Voice volume is inconsistent at times

> Audio is a bit inconsistent between different parts of the video. While it's never bad, it is quite noticeable and distracts a little

> The audio is a bit all over the place. Especially jumping from the intro to the code. I'm not an expert but perhaps normalizing the audio levels would fix that issue?


 I solved this by re-record some of the voiceover lines and I also normalized the audio volumes so they would be consistent throughout the video.

 > I like how you explain the toolkits experiments in detail. However, From 1:20 to 2:00, I feel like there is a lot of information given at the same time. To help the audience to remember everything I would personally add definitions for example "steady state" and "probes". An alternative solution would also be to show the "steady-state" code while explaining what it is. I think either of them would be great!

This was a great point. I solved this by changing my graphics to include a one-line definition of the shown concepts. I removed the part of Actions and Probes because I felt with the time limit it did not make sense to go into the depth of those concepts. Instead, I added a part that explains the order of operations of the Chaos Experiments since it is a much more important aspect of the experiments and is crucial for the understanding of the tests.

> I like that you show the code. To visualize the servers, even more, providing an image with boxes representing the microservices and the communication between the user would help a lot!

Also a great point. I fixed this by changing the graphics to an animation that shows the flow of the system instead of showing the code when explaining how the system works. The point of the demo is not to show the code, but to show how to conduct the testing. The code can be found at my linked Github for the curious. This change made much more sense. 

I also added animation on top of the section where I show the structure of the Chaos Tests that I created. So as to highlight how each part of the experiment is connected to my system.

> A summary or takeaway in the end would help tie up the video. If this is not possible perhaps it can be added in the description.

I added a takeaway at the end of the video.

> Adding background music would be good to fill in the moments of silence in the pauses (for instance in the intro by the 5, 6 second mark; the silence is quite noticeable otherwise)

I think that background music would make the video too cluttered. T think this would hurt more than it would help. Instead to fix the issue with moments of silences I cut the demo narrower. This gained me a couple of extra seconds in the end so I could fit in a takeaway at the end as well. Great!

> Voice over (except some audio levels) are good. So are the subtitles. I wouldn't say it was the easiest to follow along, but I find it hard to pinpoint why. Perhaps using images/animations to show what you are trying to do in broad strokes would make it easier to understand.

As explained above, I added animations that explained the flow of the system instead of seeing quick snippets of code to make it more clear. I also switched the part on Actions/Probes to the order of operations of the experiment to make this part much clearer.

> You say that the code can be found on your GitHub using the link in the description but that link doesn't work. Private repo?

It was set to Private, it is now Public. Good catch!

