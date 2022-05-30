# Feedback on Executable tutorial proposal: Automated email notification for IP change in SSH server: https://github.com/KTH/devops-course/pull/1844

# High level strengths and weaknesses

## Strengths 
the use case for this tutorial seems to be pretty useful, especially for people who want to set up their own server to which they might not always have access to
the tutorial tackles a fairly simple but really helpful problem
## Weaknesses
The tutorial doesn’t seem to be self-sufficient, in the sense that many times we had to search for workarounds and definitions of concepts that were not really explained too thoroughly. 
Sometimes a bit hard to follow if you don’t have any experience using Linux or simply working with this kind of problem.

# Comment for each section:

## Introduction
Expressive and clear introduction, it introduces you to the problem in a simple way.
Maybe explain a bit more what the DNS service is, a beginner might not know what you’re talking about and it can provide a bit more context to the tutorial even to less experienced users, even a simple sentence is enough.
Something like: “The DNS (Domain Name System) has the purpose to redirect any domain name (eg. google.com, kth.se, etc.) to the correct IP address.”

## How to discover your IP address
One of us found the first paragraph a bit unclear, given limited knowledge in the subject.
Maybe you could explain a way to try this out by setting up an Ubuntu server (on Windows one could use the [Ubuntu VM](https://docs.microsoft.com/en-us/windows/wsl/install) from Windows), otherwise anyone without an Ubuntu server can’t really do that, hence can’t perform the tutorial…

## How to send an email from an Ubuntu server
Even here I think a single line describing what ssmtp is would be nice. A suggestion could be: “ssmtp is a simple program that allows the user to send an email from a local machine to a specific mailhost”.

Could also explain 2 commands on how to edit a file through vim, I found it confusing and made me lose some time cause I didn’t know how to save my changes when editing the file, and exit once I was done. Simple guide [here](https://success.trendmicro.com/dcx/s/solution/1113864-editing-configuration-files-of-linux-based-products?language=en_US&sfdcIFrameOrigin=null).

"Allow less secure apps" explain more and how to do it cause I think many are going to face this problem. A simple guide can be found [here](https://hotter.io/docs/email-accounts/secure-app-gmail/).

One thing that made us feel happy is to see that we could send an email to our inboxes from the command prompt.

## How to schedule the execution of a shell script

You could have included a brief description of what a cron job is, for instance: “A cron job is no other than any defined task that runs in a given time period”. 
Also the content of the cron file is kind of mysterious with all the asterisks, maybe you could add a little description of why the code looks like that or you could also link this [website ](https://phoenixnap.com/kb/set-up-cron-job-linux)where they explain how to write a cron job.

## Putting it all together

Please clarify that you would like the user to add the code you provide using vim (I know it’s like above, but better to say it twice in my opinion). 
Another thing is the fact that it is not possible to check in a hardcoded way if the code we add at the end actually makes something, unless the IP changes. It could be useful to add a way to make sure that the user can somehow manually simulate what happens when the IP changes, so that the email is sent anyway and we know the code runs correctly.
An idea we had is to also add another version of the code that simply sends an email every 5 minutes, without having to check if the IP address has changed.