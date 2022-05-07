# Feedback on Katacoda: Secure Server Tutorial
This document was used to note down our thoughts and suggestions for the Katacoda tutorial authored by Philip Hamelink.
Link: https://www.katacoda.com/phamelink/scenarios/secure-server-tutorial

As soon as Philip's proposal was accepted, we got in contact to figure out his schedule for the tutorial. Since he was planning on finalizing his work on Friday (29. April), we worked on giving him pre-delivery feedback the day before. At this point, 3/4 steps of his tutorial were already done.

We then reviewed the 4th and last step of the Katacoda in an extra session on Sunday, 1. May.

Philip had access to this document at any time. Additionally, we scheduled a meeting on Thursday, 29. April, to discuss the current state of the tutorial.


## Summary (High-Level Feedback)
Our overall impression of the first draft is that Philip focused on applying the suggestions given in the [Formatting and Design Guide](https://www.katacoda.community/essentials/formatting.html) of the Katacoda documentation. He fragmented his complex topic into 4 relevant subsections (steps), providing a clear path to follow:
1. Deploy webserver
2. Apply reverse-proxy
3. Apply Firewall
4. Secure remote SSH access

The individual steps were easy to follow, with minimal effort, but gave room for some own explorations on the side. To further support those explorations we would suggest embedding some more links to relevant material.

Over the entire tutorial, he kept a consistent, unformal, and friendly authoring style that motivated the executee to keep going. The use of analogies was incredibly beneficial to our shared understanding.


#### Strengths
- Well-structured sections with intuitive workflows
- Very practical and relevant content
- Artful use of analogies to explain challenging concepts
- Regular tie-ins to the broader field of DevSecOps
- Transitions between sections demonstrate how all the pieces tie together


#### Weaknesses
- More links to relevant material
- Estimated time of 90min could discourage people to start tutorial
- A couple of instances of non-inclusive language ("White/Blacklist")
- Small typos throughout the tutorial
- More relevant titles, i. e. "Deploy webserver" instead of "Step1"

## General suggestions
Two pointers we feel could be useful across all steps of this tutorial


- Useful tool for checking grammar and spelling: https://www.grammarly.com/
- We recommend adding some form of a troubleshooting page
    - Or list steps at the top of each page that need to have been executed before a certain point
    - Example: `npm run start` on step two because we had forgotten to run `npm install`
- Try to avoid using non-inclusive language such as "blacklist", "whitelist". [This guide is a good resource for finding alternatives.](https://itconnect.uw.edu/work/inclusive-language-guide/)

## Introduction

The intro gives good information on what to expect from the tutorial and why it is relevant to explore this topic. Overall it felt a bit wordy in the beginning. After reading it, we understood that this was because of the chosen narrative style, which is unformal and takes the reader by the hand. We could imagine that it would be an improvement to add an outline of the agenda in bullet points, for people that would otherwise skip the intro.

## Step 1

Step 1 of the tutorial is about getting the webserver we will work on up and running. It is concise, straightforward, and well-written. However, we recommend that the author:

1. Removes the `npm test` command from package.json to keep the tutorial focused.
2. Explains when the executee is to stop/start the server.
3. Points out where specific security vulnerabilities lie as they are created.

## Step 2
Step 2, configuring the Nginx reverse-proxy, is one of the more verbose sections of the tutorial. While dense, we believe this is necessary to explain the functionality of the Nginx protocol and appreciate the author's use of the McDonalds analogy. We also appreciated the transition paragraph into step 3 at the end.

Potential improvements to the section include:

1. A diagram showing the reverse proxy's role in the application would be quite helpful.
2. Adding links to official Nginx documentation.
3. Stating more explicitly that the user is to open a new Katacoda tab (not browser).
4. Allowing more options in the choice of text editor.
5. Potentially changing the location of the Nginx config files to the project directory (confusing why they have to be in the /etc dir).

## Step 3
In this step, Philip explained, what a firewall is used for and gives an excellent example of why it is needed as an addition to the reverse proxy. He chose the popular firewall UFW and guided the executee to set it up. Everything was clear and easy to follow. However, there was one thing, that we are not sure if it works as it should.

When doing the HTTP Get request to port :8000 before setting up the firewall, the response is "Cannot GET /". We could not find out, if we did something wrong or if this is a bug, as we would assume that it outputs "Hello World! This is the Express API". It would have been appreciated to add a section for the expected output as it was done in other sections.

## Step 4
Step 4 delves into SSH server access, a very-commonly used practice in development workflows. Philip did a great job explaining why it is an improvement over password-based authentication and was able to include a small easter egg (`"Linus/Torvald"`) that made us chuckle. Two points of feedback on the section are:

1. We are not sure of the validity of the claim that it is "very likely that an attacker [using brute force methods] will succeed" in hacking a machine with PW-based authentication.
2. It's worth mentioning which user you are by default on the Katacode machine (`root`)

## Conclusion
Philip's conclusion does a great job of tying all the principles learned in the tutorial back to DevOps, while leaving the executee with a passion to learn more. We think there are a couple of potential areas for improvement, but overall believe it's a perfect synopsis of the previous 4 steps, why they are important, and how to extend these learnings:

1. There are a few typos in the conclusion.
2. We would appreciate links relevant to the additional functionalities discussed (`nginx load balancing`, for example).
3. The claim that the steps learned are needed on the original deployment is not true, at face value. These steps are needed only if you want to not get hacked (Users can deploy the server from Step 1 instantly).
4. Worth mentioning that Nginx is still developing as a project - more security features are coming!

## Pointers to additional material
- [Comparing SSH Encryption methods](https://goteleport.com/blog/comparing-ssh-keys/)
- [Nginx HTTP Request Load Balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)
- [Nginx Github Repo](https://github.com/nginx)
- [Inclusive Languate Guide](https://itconnect.uw.edu/work/inclusive-language-guide/)
- [Nginx Contribution Guide (open-souce contribution idea!)](http://nginx.org/en/docs/contributing_changes.html)
- [Nginx documention](https://docs.nginx.com/)
-





## Appendix (Raw notes from tutorial run-through)

### Introduction

- a lot of text
- maybe highlight some keywords
- good paragraph for explaining the motivation
- nice friendly writing style
- Maybe outline the agenda in bullet points (so people can easily parse the plan for the tutorial)
- Maybe add optional-for-user Wikipedia links for complex terms (like a reverse-proxy, firewall)

### Step 1

- Can eliminate the npm test script
- Probably want a newline char in the API response
- Should we stop the server? Does it auto-refresh when we make code changes?
- Narrator style is nice
- Maybe point out the security vulnerabilities that we arent addressing yet?
- Unclear why we are serving a static website at this point, why is this necessary for the project? How do we start it?
- When doing the HTTP GET request, it is not necessary to be in the same directory
- In the section, where you let the user stop the server, you could tell them to switch back to the terminal tab, that the server is running in

### Step 2
- Add link to nginx docs you are citing
- "Now, in press on the + button" - maybe add further instruction, that you meen the +, that opens a new terminal window
- love the analogy
- Inclusive language check (change "blacklist" to "blocklist")
- In the "why does this make our server more secure," could tie back in to analogy (e.g nginix prevents customers from using the fryer to cook a shoe)
- Is it possible to place nginx config files within the projects dir?
- Do we rly have to use nano? Nobody knows how to do this
- If we wanted to change what our server serves, how would we do that?
- Maybe you can remove all the unnecessary parts from the sites-available file
- I like the tie-in to CD at the end of the step!
- Cannot copy/paste into nano with a Swedish keyboard?
- "cd /home/projects/express-api && npm run start" - add npm install for the people that skipped step
- Good last paragraph where you transition to step 3

### Step 3
- Inclusive language ("Blacklist")
- I think requests to :80 should still be allowed - in the tutorial, should say :8000 (edit: Error with HTTP GET to port :8000 "Cannot GET /")
- Quite a few typos - check out Grammarly!
- Where is UFW configuration defined? Is that in the same files as nginx config?
- When was UFW installed?
- Add link to UFW documentation?

### Step 4
- Not sure of the claim that it is "very likely that an attacker [using brute force methods] will succeed" in hacking a PW-based auth system
- Worth mentioning which user you are by default on Katacode machine (root)