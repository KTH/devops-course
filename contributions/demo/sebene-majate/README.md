
# Demo Submission: Setting up Drone CI with Bitbucket


## Contributors
* Sebastian Fagerlind - sebene@kth.se - @sebberh
* Maja Tennander - majate@kth.se - @majate


## Links
[Video](https://youtu.be/YGKKG6ZDQhc)

## Description
Our video demonstrates how to set up a simple CI pipeline with [Drone](https://www.drone.io/) for repos on [Bitbucket](https://bitbucket.org). We show how to configure your own Drone server to connect to a specific Bitbucket repo and demonstrate how Drone will automatically start building your code whenever you push to the repo.

## Subject motivation
The demonstration is clearly relevant to the DevOps subject. One major part of DevOps is automation, which is what Drone helps achieve as a CI/CD software.

## Criteria that we think we fulfil
- **The demonstration is clearly motivated**
  - See motivation in section [Subject motivation](#subject-motivation).
- **The demonstration is difficult to do** *(with distinction)*
  - For this demo we used multiple tools and services such as ngrok,  Docker, Bitbucket and Drone. Configuring all these tools to work together was not trivial. Since Docker, Bitbucket and Drone were all new things to us, we had to learn how to install, configure and use these tools on both Mac and Windows for the first time, before we were even able to create content for the video. Furthermore, editing the video and audio to construct a good 3 minute long video demonstrating a process that took more than 3 minutes to perform was a great challenge.
- **The demonstration is original** *(with distinction)*
  - There are short demos showing how to setup a Drone server with Github, but we cannot find a single video demo online actually demonstrating all steps to configure a CI pipeline with Drone together with Bitbucket.
- **The video is sublime (eg visually appealing)** *(with distinction)*
  - We spent a lot of time designing the slides and editing the video and believe it is sublime.
- **The video contains an easter egg**
  - The C++ program in our repo prints out the link to the DevOps github page. This print can be seen in the build log in Drone at the end of the video.
- **The video must contain subtitles which are clear and in proper English** *(with distinction)*
  - There are subtitles that can be turned on in youtube.
  - There is a voice over that is clearly understandable.  We put effort into writing a good script and recoding the voice over.
- **The video includes a take-home message**
  - In the end of the video we have included a slide with clear actions for a viewer to take if they try to do the setup on their own and find any troubles on the way.

## Changes after feedback
- The "thumbnail" of the first slide is removed from the lower right corner of the second slide.
- A description of Bitbucket is added near the Bitbucket logo on the second slide.
- The video now zooms in on the settings for the OAuth consumer at timestamp 0:50.
- To reduce the "noise" of having too many windows on the screen simultaneously, irrelevant parts of the screen have been cropped out.
- The slide in the outro is updated. The old content (the list of actions for a viewer to take if they try to do the setup on their own and find any troubles) is moved to the video description.
- The typo in the video description was fixes.
