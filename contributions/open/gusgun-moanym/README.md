# Review Collector

### Bot/backend

**Repository:** https://github.com/gustafguner/review-collector

Hosted on a free dyno at Heroku.

### Website

**Live link:** https://review-collector.netlify.com<br>
**Repository:** https://github.com/gustafguner/review-collector-web<br>

Made with Gatsby and hosted on Netlify.

## Description

We have created a Slack app for notifying team members when they have been added as a reviewer on a pull request on GitHub.

The standard workflow when merging code into master (or develop if you'd like) is to create a pull request, assign reviewers and wait until they see the notification on GitHub or their email, or direct message those same people on Slack to remind them to review. Until they do, the code is on hold.

By further integrating those two, among the most used, tools for developers, our ambition is that the app will streamline the coding workflow and take code into production at a faster rate while minimizing delays.

You can read more about the project in the [repository](https://github.com/gustafguner/review-collector). Since the bot as of today is hosted on a free dyno on Heroku, timeouts do occur when for example executing a command. However, when you try it again it should be working fine since the dyno should have kicked in by then.

For this task we have applied pair programming, a principle perhaps on the softer side of DevOps rather than the hardcore tech side. Pair programming means that each programmer in the pair takes turns either writing or reviewing the code and coming up with suggestions along the way. The idea of pair programming is to give both programmers deeper understanding of the code and minimize mistakes before the standard code review.

## The app

To use Review Collector, you simply click the "Add to Slack" button on the website and you will directed to a Slack page telling you what privileges the app is asking for with a choice of either accepting or rejecting it. Once accepted, the Review Collector bot will be added to your workspace and you will be redirected to the page "Step 2: GitHub Authorization". By clicking the "Add to GitHub" button you will be directed to an authorization page again, but this time for GitHub. Once you've accepted the app the initial setup is done.

You will now be able to watch repositories using the slash-command `/watch`, but for people in your slack workspace to be notified about review requests and such they will have to connect their Slack user with their GitHub user. To do this, run `/connect` and you will be prompted with the button "Connect with GitHub". Once you've clicked it and accepted the OAuth2 app, you're all set. Notice: Both users (both the review requester and the requested reviewer) must be connected for the notifications to work properly.

# Original proposal

### Slack bot with GitHub integration

### Members

Gustaf Gunér (gusgun@kth.se)<br>
Moa Nyman (moanym@kth.se)

### Task

We are going to develop a Slack bot/app that integrates with GitHub. The purpose of the bot is to notify people directly via DM when they are reqested to review a pull request.
