# Demo: CD of Node Express App on Google Cloud with designated release branch using GitHub actions

In this demo, we will demonstrate how to create a continuous deployment workflow using GitHub Actions that automate deployment of a simple Express server to Google App Engine (GAE), a fully managed, serverless platform for developing and hosting web applications at scale. We will go through the following:
1. How to create a project on Google Cloud
2. How to deploy the Express server to Google App Engine (GAE)
3. How to create a CD workflow to automate deployment using GitHub Actions

## Members

Kalle Pettersson (kalpet@kth.se)  
GitHub: [KallePettersson](https://github.com/KallePettersson)

Anders Nilsson (andnil5@kth.se)  
GitHub: [andnil5](https://github.com/andnil5)

## Screencast link
[YouTube link(old)](https://www.youtube.com/watch?v=lY5Uj_VzClc).
[YouTube link(new)](https://www.youtube.com/watch?v=xieUj9TSewA).

## GitHub repository
[GitHub link](https://github.com/KallePettersson/Continous-Deployment-on-gCloud).

## Motivation

The motivation for why this demo matters to DevOps is twofold.
- It shows how to deploy an application on Google Cloud, which increases productivity and flexibility, frees up developers by taking away the demands of managing infrastructure, and provides automatic scaling.
- It demonstrates how to create a continuous deployment workflow using GitHub actions, one of DevOps' cornerstones.

## Take home message

Make sure to **NOT** commit your `gcloud_secret.json` file to GitHub. This could give malicious actors remote access to your Google Cloud account.

## Grading - We strive to meet the following grading criteria

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The demonstration is clearly motivated (why it matters for Devops?) | X |  | |
|The video is sublime (eg visually appealing) | X |  |  |
|There is a code repo to run the demo  | X |  | X |
|The video must contain subtitles which are clear and in proper English | X |  |  |
|The video includes a take-home message | X |  | X |

## Feedback 

- [X] **The GitHub link also doesn't work if the commands were posted there (+2)**

**Solution:** The repo was changed to be public so that the link now works.

- [X] **The video quality and resolution (+3).**

**Solution:** We improve the video quality of the uploaded video.

- [X] **Difficult to read code/terminal text.**

**Solution:** Zoomed in on the relevant parts of the terminal code to make it easier to see and read the commands.

- [X] **There were also some sections where we need to copy commands and it isn't really highlighted in any way to make it easier to see.**

**Solution:** Same as above.

- [X] **I think the motivation is great however I do believe that you need to include it in the video. (+1 Having a "why" is important.)**

**Solution:** Added motivation for implementing a CD pipeline at the beginning of the demo.

- [X] **Add a summary at the beginning**

**Solution:** Added a "in this video we will.." page to give the viewer an overview of what will be covered in this demo.

- [X] **I would suggest adding an opaque background for your explanation text since in various frames it's hard to read it because it overlaps the text displayed in the browser.**

**Solution:** Added background to subtitles for each frame where there was overlapping background text.

- [ ] **Don't have the subtitles in CAPITAL letters.**

**Comment:** We have used iMovie to make this video with subtitles where we only have capital letters as an option, so we decided not to make the change this time. However, we will consider using another tool next time we make a demo.

- [X] **Some steps were explained in a bit too much detail though, such as how to log in to Google by pressing 'Allow'.**

**Solution:** Removed this specific frame and shortened the explanation of some frames where reasonable.

- [X] **Too fast, pauses necessary. Perhaps intended though, and**
- [X] **Not having a voice-over was an intended decision I assume, but this means that the pacing of the video is much slower than it needs to be. Some say it's too fast, but pausing to write code should be the indeed way to consume video tutorials in my biased opinion.**

**Solution:** Since we got mixed feedback about the video speed, we opted to keep the overall pace as it was. However, to further improve the demo quality, we went through the demo again and trimmed down the parts that felt too long and slowed down the pace where we thought that a pause was necessary.

The changes are based on the feedback from [PR #1200](https://github.com/KTH/devops-course/pull/1200)