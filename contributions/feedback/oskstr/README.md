# Implementing AWS Lambda and invoking it with AWS SES [#1160](https://github.com/KTH/devops-course/pull/1160)

## Members:

Name: Oskar Strömberg (oskstr@kth.se)
GitHub: [oskstr](https://github.com/oskstr)

## Proposal:

I plan to give feedback on tutorial [#1160](https://github.com/KTH/devops-course/pull/1160).

## Feedback

### Overview
It was a very nice tutorial. I was somewhat familiar with the subject before so navigating AWS's confusing user interface wasn't too bad for me. But that is hardly something I can blame you for anyway. The pictures helped a lot with that as well.

I like that the steps are very concise and easy to follow. 

According to the Katacoda Design Guide, a scenario should have the form of a "loosely defined story" to create some emotional response making the learning more likely to stick. So maybe "why" we are learning this or at least what we are trying to do is worth adding.

I think the length of the scenario was good.

### Intro
Following the tutorial I realise that it is a homage to [NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts), in particular `kumar-asshole.sh` (funny easter egg btw). Knowing that I can see why having problems with "receiving emails and processing them" is an issue. But since we don't have the background at this stage that doesn't really matter.

Maybe have some more context here. If you go the story route you could have a scenario where we are trying to solve a particular problem. For example having someone bothering us via email with a trivial task over and over again - and we want to automate that. For that we can use a Lambda function and why we would choose that.

### Step 1
Very simple step. Easy to follow. I already had an AWS account which made this trivial. I just had to log in. I didn't bother to create another account for the purposes of this feedback, I'm sure you'll understand.

### Step 2
Most of it was straightforward except for 
> "...create a new role for `Lambda`..." 

as AWS calls it a Use Case. So you could perhaps clarify that with something along the lines of 

> "... create a new Role and select the `Lambda` use case. Then add the `WriteEmails` permission policy ... " 

You can probably think of some better wording. 

Between the permissions page and page where you give the role a name there is a "Tag" page. I don't know if it is necessary to tell people to skip that page to "Review" (where you name the Role). Something to think about perhaps. I was a bit confused at least, but that is more of an issue with AWS than with your tutorial.

### Step 3
Good thing that you have a short explanation of SES again in case the user didn't read the intro thoroughly :+1:. 

Even though it is easy to add two email addresses you can simplify this step a bit by just sending and receiving using the same address. I would also like to see some more explanation here. The reason why you have two is because you need to verify addresses you can send to as well, right? How do I send to any email address?

### Step 4
Again, a fairly straightforward step. You might want to add a word or two about which runtime to use (even though we are using the default). That we are going with Node.js because we are doing a Lambda in Javascript. But you could technically choose from a bunch of languages here.

I also found setting the permission in AWS here a bit confusing. You could explain that with a few more words. For example:

> "... by pressing `Change default execution role` and then pick `Use an existing role` and select `LambdaEmail`... "

You could also explain with a few words what the code is doing and what you might have to change if you have used other email addresses than the ones provided.

### Step 5
Good explanation and good troubleshooting step. 

### Step 6
Any reason why we are going with an `HTTP API` instead of a `REST API`?

I would also like to see some more information about what a trigger is. 

If I would like to trigger it based on incoming emails, how would I do that? If you go with explaining that is what you ultimately would like to do. Maybe point me in the right direction at least.

## Changes made based on feedback

- [6c9ebab](https://github.com/oskstr/katacoda-scenarios/commit/6c9ebab) Change verbatim text to code blocks 
- [084bc62](https://github.com/oskstr/katacoda-scenarios/commit/084bc62) Format policy snippet as JSON
- [563582d](https://github.com/oskstr/katacoda-scenarios/commit/563582d) Change from replace to append/insert
- [aea9485](https://github.com/oskstr/katacoda-scenarios/commit/aea9485) Fix typo
- [ed6f7ec](https://github.com/oskstr/katacoda-scenarios/commit/ed6f7ec) Add explanation to image
- [f59c842](https://github.com/oskstr/katacoda-scenarios/commit/f59c842) Add warning about error messages
- [f1d6222](https://github.com/oskstr/katacoda-scenarios/commit/f1d6222) Explain bug where command isn't being run
- [7109af6](https://github.com/oskstr/katacoda-scenarios/commit/7109af6) Make curl calls executable
- [64dda2c](https://github.com/oskstr/katacoda-scenarios/commit/64dda2c) Explain which header we are looking for
- [e0a040d](https://github.com/oskstr/katacoda-scenarios/commit/e0a040d) Explain how to set up an AWS user
- [9c0e73a](https://github.com/oskstr/katacoda-scenarios/commit/9c0e73a) Add more spacing
- [2444cbf](https://github.com/oskstr/katacoda-scenarios/commit/6c9ebab) Remove space that caused graphical bug
- [85ad312](https://github.com/oskstr/katacoda-scenarios/commit/6c9ebab) Increase expected time for scenario

Diff log: https://github.com/oskstr/katacoda-scenarios/compare/756b829...85ad312