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

I enjoyed taking your tutorial, it was overall a very good experience! My feedback starts with general suggestions that I believe applies to all slides, and below that, I go more into the depth of each individual slide of what features I liked and where I saw the potential for improvement. 

## General suggestions
Change your slide indexing to start with 1, Katacoda uses 1-indexing and it is a bit confusing when it says "Step 1" directly above your text that says "Step 0". In my feedback, I will use your indexing starting with 0.

Before the final submission, you should go through your text and check for errors in spelling and grammar, there are a lot of small mistakes. Grammarly is a good free tool.

You have some Katacoda related bugs on almost every slide. The `Copy to editor` button seems to be configured wrong in every place it is used since it do not succeed in creating files that does not already exist and it rarely seems to do what is expected. This, of course, could be a problem with the Katacoda environment. After having done my own Katacoda tutorial I know that it is very common for it to behave irrationally, so I do not want to be too harsh on this point. I think you should try to create your tutorial with this fact in mind (the problems with Katacoda) so the user does not get stuck in your tutorial because of something that is not your fault.

I think it was a great tool to use questions in the slides. I think you should consider having one question at the bottom of each slide to force more focus and interaction from the user. 

Except for the problems with Katacoda-features and some languages misses I think the tutorial was very good in explaining the concepts in a way that did not feel overwhelming but instead a fun experience. The topics were often explained in short and concise ways that got the point across. The example tests were smartly constructed in being for the most part easy to read and understandable even without having to spend too much time reading them. They also worked great in explaining the topic at hand.



## Intro

I think the introduction page does a great job telling me the contents and the learning outcome of the tutorial. I also think it is a nice touch that it includes what pre-requisites are needed to do the tutorial.

## Step 0

When explaining what is a meaningful test I think some parts could be explained more clearly. Why, for example, is there a greater risk that I will not run a test if it is slow? I think this point clashes a bit with the section below *What are some test strategies?* that tells us that UI tests are *Slow & Expensive*. Does that mean that UI tests are not meaningful?

I would have liked to see an explanation of what a "flaky test" means. If we are at the level of explaining what a meaningful test is then I do not think "stable/flaky test" is common knowledge. You also use abbreviations for three different tests strategies instead of writing out their full names. You do not have to explain them more in-depth, but at least give me the full names for some more context and make it easier for me to look them up at a later time (for example "STEP test strategy" does not directly give me that specific strategy).

Overall I think this section could benefit from using the pyramid picture as a take-off point and then explain the different types of tests for each layer and the cost/time trade-off for each different type of testing.

There are also some problems with the quiz at the end of step 1. This could be a bug in Katacoda, but the questions do not give me any feedback, it just says that I was wrong. With three different questions and the last one being multiple-choice, it was really hard to know where my error was. I had to look up your source code to find the solution, but after I had completed it and then returned to step 1 then it gave me green check markers on my answers which made me being able to brute force it, if necessary. If Katacoda does not always show where you are right and wrong you can get stuck at a step in the tutorial since it does not let you progress to the next step before the quiz is correctly answered. 
I think this needs to be changed so it:

1. Does not block you from continuing the tutorial.
2. Give tips when you are stuck.
3. Check if the bug with non-visible check marker is in your code or Katacoda. (Probably Katacoda, since it has a lot of problems.)

*Note* I noticed another bug where you can check every box in the last question and it will accept it.

## Step 1

I like your easter egg, it is cute and makes the tutorial more colourful. I also think it was cool that you could run your project in Katacoda, I did not know you could get access to localhost like that in Katacoda. Very nice.

This step could benefit from explaining the structure of the dummy project at least a little bit, this is now left completely up to the reader. I think you could explain the very basics in just a few sentences to make it more accessible, especially since it says in the intro that you could use this tutorial even if you are not familiar with React.

## Step  2

It is very nice that you attach links to other sites for more information on topics. 

In *Give it a try* the `Copy to editor` button does not work. You should be able to set it up so it automatically creates the file for you so the user does not need to manually add the files. Except for that, the language is clear and engaging, which is very nice.

## Step 3

A good introduction to Snapshot tests. I think the examples are good and give a nice introduction to the concept. 

One point of improvement in this slide is that the user needs to find row 40 in `loginForm.jsx` instead of you just creating a replace button in Katacoda for it. You could argue that it makes the user more aware of what is happening, and I could agree. The Katacoda documentation states that the user should ideally never have to write any code in a tutorial, so it could be something to take into consideration. You can read more about this [here.](https://www.katacoda.community/formatting.html#learning-experience-approach) There is also a typo that says that I should look for a folder called `component` but it is called `components` in the project. 

## Step 4

This is a very good slide. It explains the concept easily and the single question at the end of the slide forces me to think about the test and the code and what is actually happening. I think this is something you should apply to all the slides. One single question that forces me to take one extra second to think about what I am doing. This works much better than the first slide when it instead was three questions. 

## Step 5
The first code snippet does not have the `Copy to editor`-feature. Also since the code-block does not have any syntax highlighting and the text does not exactly explain what it is that I should change, this makes it very easy to make a mistake that breaks the code. If you manage to break the code, it is very hard to fix it. The editor you chose to use in Katacoda does not have syntax highlighting which makes it very hard to read code in it. 

This text is a bit unclear 
*"If you run the test suite, one test will now fail. But after the changes you can expect both these tests to pass if implemented correctly."*
It sounds like the two sentences should be separated by some code that changes something. If you mean the changes above, they are already implemented since it was explained before. 

You could force the user to run the tests by sprinkling with executable `npm test` after each step so the user could see the difference. 

Very good that you add a note on how to tackle the problem with e-mail validation in production!


## Step 6, Step 7 and finish
Very good slides. This should be the standard in how you tackle each slide. Good language and easy to follow. 

The Finish page is also very good. I think it is nice to get a summary of what content I have gone through and what steps I should take next if I want to learn more about the topic. Especially good that you include a link to other sources so the user can easily continue exploring. This could be improved by adding even more links to more 