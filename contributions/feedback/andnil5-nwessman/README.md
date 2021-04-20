# Feedback: Learn to integrate Jest in your React projects

## Links

 - [Tutorial directory](https://github.com/KTH/devops-course/tree/2021/contributions/executable-tutorial/agnespet-adahen)
 - [Tutorial proposal (given feedback to) - #1242](https://github.com/KTH/devops-course/pull/1242)  
 - [Feedback proposal - #1113](https://github.com/KTH/devops-course/pull/1113)  

## Members:

Name: Anders Nilsson (andnil5@kth.se)  
GitHub: [andnil5](https://github.com/andnil5)

Name: Niklas Wessman (nwessman@kth.se)  
GitHub: [nwessman](https://github.com/nwessman)


# Feedback


# Feedback by Niklas Wessman

## Overall
Change your slide indexing to start with 1, Katacoda uses 1-indexing and it is a bit confusing when it says "Step 1" directly above your text that says "Step 0". In my feedback I will use your indexing starting with 0.

Before the final submission you should go through your text and check for errors in spelling and grammar, there are a lot of small mistakes. Grammarly is a good free tool.

## Intro

I think the introduction page does a great job telling me the contents and the learning outcome of the tutorial. I also think it is a nice touch that it includes what pre-requisites that are needed to do the tutorial.

## Step 0

When explaining what is a meaningful test I think some parts could be explained clearer. Why, for example, is there a greater risk that I will not run a test if it is slow? I think this point clashes a bit with the section below *What are some test strategies?* that tells us that UI tests are *Slow & Expensive*. Does that mean that UI tests are not meaningful?

I would have liked to see an explanation on what a "flaky test" mean. If we are at the level of explaining what a meaningful test is then I do not think "stable/flaky test" is common knowledge. You also use abbreviations for three different tests strategies instead of writing out their full names. You do not have to explain them more in depth, but at least give me the full names for some more context and make it easier for me to look them up at a later time (for example "STEP test strategy" does not directly give me that specific strategy).

Overall I think this section could benefit from using the pyramid picture as a take-off point and then explain the different types of tests for each layer and the cost/time trade-off for each different type of testing.

There is also some problems with the quiz in the end of step 1. This could be a bug in Katacoda, but the questions does not give me any feedback, it just says that I was wrong. With three different qeustions and the last one being multiple choice, it was really hard to know where my error was. I had to look up your source code to find the solution, but after I had completed it and then returned to step 1 then it gave me green check markers on my answers which made me being able to brute force it, if necessarily. If Katacoda does not always show where you are right and wrong you can get stuck at a step in the tutorial since it does not let you progress to the next step before the quiz is correctly answered. 
I think this needs to be changed so it:

1. Does not block you from continuing the tutorial.
2. Give tips when you are stuck.
3. Check if the bug with non-visible checkmarker are in your code or in Katacoda. (Probably Katacoda, since it have alot of problems.)

*Note* I noticed another bug where you can check every box in the last question and it will accept it.

## Step 1

I like your easter egg, it is cute and make the tutorial more colorful. I also think it was cool that you could run your project in Katacoda, I did not know you could get access to localhost like that in Katacoda. Very nice.

This step could benefit from explaining the structure of the dummy project at least a little bit, this is now left completely up to the reader. I think you could explain the very basics in just a few sentences to make it more accesible, especially since it says in the intro that you could use this tutorial even if you are not familiar with React.

## Step  2

It is very nice that you attach links to other sites for more information on topics. 

In *Give it a try* the `Copy to editor` button does not work. You should be able to set it up so it automaticly creates the file for you so the user does not need to manually add the files. Except from that the language is clear and engaging, which is very nice. 