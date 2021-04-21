# Feedback: Learn to integrate Jest in your React projects

[Tutorial directory](https://github.com/KTH/devops-course/tree/2021/contributions/executable-tutorial/agnespet-adahen)  
[Tutorial proposal - #1242](https://github.com/KTH/devops-course/pull/1242)  
[Feedback proposal - #1113](https://github.com/KTH/devops-course/pull/1113)  

## Members:

Name: Anders Nilsson (andnil5@kth.se)  
GitHub: [andnil5](https://github.com/andnil5)

Name: Niklas Wessman (nwessman@kth.se)  
GitHub: [nwessman](https://github.com/nwessman)

## Grading - We strive to meet the following grading criteria

|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The feedback includes both strengths and weaknesses about the task | X |  |  |
|The feedback is provided 4 business days before the task deadline | X |  | X |
|All points are clearly actionable | X |  | ? |
|The feedback is substantiated | X |  | X |
|The feedback contains pointers to additional material | X |  |  |
|The students act upon the feedback they receive | X |  | X |

# Feedback by Anders Nilsson

The tutorial is well written and easy to follow. It was interesting as well as instructive, which resulted in a delightful experience. I would argue that most of the steps were nicely formatted and ordered in a logical order. I have written some comments and improvement suggestions for each step below, but remember that they are suggestions and only chose to implement what you think will improve the tutorial.

## General suggestions
- **Comment:** I like the short metatexts on each page, which increase the user experience.
- **Format:** Change the title of each step. For now, it says *Step i*, which is contradictory to the title above that says *Step (i+1) of 8*. Configure the titles in the file `index.json` by changing the label `title` of each step. Also, I recommend using the subtitles in the steps as step title instead of *step i*.
- **Language:** Make sure to conduct a final language check before the final submission, for instance, with the automated tool [`Grammarly`](https://app.grammarly.com/).

## Intro page
- **Comment:** The intro page gives a clear introduction to what the tutorial is all about. I also find it convenient that you mention the prerequisites for the tutorial.
- **Content:** Consider adding a statement that attracts the user to take the tutorial. For instance, by answering the question: Why is automated testing necessary? For inspiration, see [this](https://uplandsoftware.com/cimpl/resources/blog/8-benefits-of-using-automated-systems/) blog post.
- **Format:** Consider removing the point before: "You will be focusing on the Log-in flow of a react project where you will learn:".
- **Language:** Substitute "We expect you to also know" to "We also expect you to know".
- **Reference:** As stated above, I enjoyed that you mention the prerequisites of the tutorial. To further improve, you could add links to resources where the user can catch up with JavaScript and learn React; at least a link to a React tutorial would be sufficient. For instance, you could use these resources:
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
  - [Intro to React](https://reactjs.org/tutorial/tutorial.html)

## Step 1
- **Comment:** The theory in this step is well presented and gives the user an excellent introduction to why testing is practical. Especially the content under the header: *What are some test strategies?* was satisfying.
- **Content:** I would recommend describing the difference between a stable and a flaky test. I believe that it would be enough with one or two sentences for this. For inspiration, see [this link](https://docs.gitlab.com/ee/development/testing_guide/flaky_tests.html).
- **Content:** It's great that you give some examples of different test strategies. To further improve, you could mention that *step ...* covers TDD later in the tutorial.
- **Format:** I suggest changing the title to "What is a meaningful test?", remove the header "Short on testing", and write its content in italic style.
- **Format:** It's nice that you get an introduction to testing, but you might want to fast forward to the next step without answering the quiz if you are already familiar with testing. Thus, a shortcut is beneficial for experienced users.
- **Language:** Substitute "To be able to" to "To" for clarity.
- **Language:** Consider changing the word "read" in "The test is easy to read." to either interpret or understand.

## Step 2
- **Comment:** I enjoyed that you have utilized the Katacoda {{execute}} keyword for the commands since it makes them much easier to execute and improves the smoothness of conducting the tutorial.
- **Comment:** It was nice that it is stated that the installation might take a while and that you provide the user with things to do during the installation.
- **Content:** Remove "We have created a dummy project for you to work on within this tutorial. It is a react project describing a login flow." from point 1 in the setup. It is a bit superfluous since it's stated in the paragraph above.
- **Content:** Remove the `ls` command.
- **Content:** I was a bit confused when nothing happened when pressing the `Submit` button. I suggest mentioning the expected behavior of the login form.

## Step 3
- **Comment:** The content of this step is clear and well written, especially the description under the header: *React Testing Library*.
- **Comment:** I really appreciated the link to the `Jest CheatSheet`, which definitely is useful while learning testing with Jest.
- **Content:** Make the command `ctrl+c` executable, like previous commands.
. **Content:** Mention that `Copy to Editor` copies the content and creates the file for you. This is not obvious if you are not used to Katacoda.
- **Language:** Missing "are" or "," after "Here" in "Here six good reasons why:".
- **Language:** Clarify the sentence: "It runs test in parallel which makes it has a high speed of test execution". You could rewrite it to something similar to: "It runs tests in parallel, which makes test execution more efficient".
- **Reference:** Even though I strongly like the introduction under *React Testing Library* and I believe that you cover enough in its description, I am missing a link to where you can read more about it. I would recommend adding a link for this. For instance, you could add: "[Click here to learn more about React Testing Library](https://testing-library.com/docs/react-testing-library/intro)" to the end of the paragraph.
- **Reference:** In addition to the `Jest CheatSheet` link, I would recommend referencing the well-documented [`Jest API`](https://jestjs.io/docs/api).

## Step 4
- **Comment:** It was satisfying to test both correct and incorrect code to understand the behavior of the Jest framework further.
- **Content:** The Katacoda command {{open}}, can be used to open files automatically in the editor. I would recommend utilizing it when asking the user to open the file `loginForm.jsx-`. You can read more about it [here](https://www.katacoda.community/scenario-syntax.html#katacoda-s-markdown-extensions).
- **Content:** Change the instruction: "In components/loginForm.jsx on row 40, change the title from Login form to just Login." to make use of `Copy to Editor` as done in previous steps. For instance, you could create a code block and make use of insert, which replaces <code>Login from</code> by <code>Login</code> with the following code when `Copy to Editor` is clicked:
```html
<pre class="file" data-filename="{FILE_PATH}" data-target="insert" data-marker="Login form">Login</pre>
```

## Step 5
- **Comment:** Overall, an excellent page!
- **Content:** The only thing I think could be clarified is the Jest tests. A short description of each test is sufficient, especially for users who are not used to testing with Jest.

## Step 6
- **Content:** The first code block is a bit messy. You could use the keyword `replace` to get it nicely formatted and highlighted, as in the case of the other code blocks. You can read more about it [here](https://www.katacoda.community/scenario-syntax.html#katacoda-s-markdown-extensions).
- **Content:** As part of the first quiz, the correct answer of test naming does, in my opinion, not match well with the naming of the implemented tests. Resolve this by making the naming in the quiz more general and not specific to the input numbers.

## Step 7
- **Language:** Substitute "will" to "with" in: "Integration test will full mocking".

## Step 8
- **Comment:** It is satisfying that you include test coverage. Well done!
- **Content:** Even though the part about `Docker` is well written, it feels a bit out of topic.
- **Content:** I think it is convenient to write a short statement about the other coverage measurements as well. At least branch coverage should be covered.
- **Language:** Missing "tests," after Jest in the sentence: "To check the Code Coverage of our written Jest we have added a code coverage command in our scripts in the package.jsonfile:".

## Finish
- **Comment:** It is nice that you have included a few suggestions of what to do next. To further improve it, you could include additional links to some resources you find good for each topic!

# Feedback by Niklas Wessman

I enjoyed taking your tutorial, it was overall a very good experience! My feedback starts with general suggestions that I believe applies to all slides, and below that, I go more into the depth of each individual slide of what features I liked and where I saw the potential for improvement. 

## General suggestions
Change your slide indexing to start with 1, Katacoda uses 1-indexing and it is a bit confusing when it says "Step 1" directly above your text that says "Step 0". In my feedback, I will use Katacoda's indexing starting with 1.

Before the final submission, you should go through your text and check for errors in spelling and grammar, there are a lot of small mistakes. Grammarly is a good free tool.

You have some Katacoda related bugs on almost every slide. The `Copy to editor` button seems to be configured wrong in every place it is used since it do not succeed in creating files that does not already exist and it rarely seems to do what is expected. This, of course, could be a problem with the Katacoda environment. After having done my own Katacoda tutorial I know that it is very common for it to behave irrationally, so I do not want to be too harsh on this point. I think you should try to create your tutorial with this fact in mind (the problems with Katacoda) so the user does not get stuck in your tutorial because of something that is not your fault.

I think it was a great tool to use questions in the slides. I think you should consider having one question at the bottom of each slide to force more focus and interaction from the user. 

Except for the problems with Katacoda-features and some languages misses I think the tutorial was very good in explaining the concepts in a way that did not feel overwhelming but instead a fun experience. The topics were often explained in short and concise ways that got the point across. The example tests were smartly constructed in being for the most part easy to read and understandable even without having to spend too much time reading them. They also worked great in explaining the topic at hand.

## Intro
I think the introduction page does a great job telling me the contents and the learning outcome of the tutorial. I also think it is a nice touch that it includes what pre-requisites are needed to do the tutorial.

## Step 1
When explaining what is a meaningful test I think some parts could be explained more clearly. Why, for example, is there a greater risk that I will not run a test if it is slow? I think this point clashes a bit with the section below *What are some test strategies?* that tells us that UI tests are *Slow & Expensive*. Does that mean that UI tests are not meaningful?

I would have liked to see an explanation of what a "flaky test" means. If we are at the level of explaining what a meaningful test is then I do not think "stable/flaky test" is common knowledge. You also use abbreviations for three different tests strategies instead of writing out their full names. You do not have to explain them more in-depth, but at least give me the full names for some more context and make it easier for me to look them up at a later time (for example googling "STEP test strategy" does not directly give me that specific strategy).

Overall I think this section could benefit from using the pyramid picture as a take-off point and then explain the different types of tests for each layer and the cost/time trade-off for each different type of testing.

There are also some problems with the quiz at the end of step 1. This could be a bug in Katacoda, but the questions do not give me any feedback, it just says that I was wrong. With three different questions and the last one being multiple-choice, it was really hard to know where my error was. I had to look up your source code to find the solution, but after I had completed it and then returned to step 1 then it gave me green check markers on my answers which made me being able to brute force it, if necessary. If Katacoda does not always show where you are right and wrong you can get stuck at a step in the tutorial since it does not let you progress to the next step before the quiz is correctly answered. 
I think this needs to be changed so it:

1. Does not block you from continuing the tutorial.
2. Give tips when you are stuck.
3. Check if the bug with non-visible check marker is in your code or Katacoda. (Probably Katacoda, since it has a lot of problems.)

**Note:** I noticed another bug where you can check every box in the last question and it will accept it.

## Step 2
I like your easter egg, it is cute and makes the tutorial more colourful. I also think it was cool that you could run your project in Katacoda, I did not know you could get access to localhost like that in Katacoda. Very nice.

This step could benefit from explaining the structure of the dummy project at least a little bit, this is now left completely up to the reader. I think you could explain the very basics in just a few sentences to make it more accessible, especially since it says in the intro that you could use this tutorial even if you are not familiar with React.

## Step  3
It is very nice that you attach links to other sites for more information on topics. 

In *Give it a try* the `Copy to editor` button does not work. You should be able to set it up so it automatically creates the file for you so the user does not need to manually add the files. Except for that, the language is clear and engaging, which is very nice.

## Step 4
A good introduction to Snapshot tests. I think the examples are good and give a nice introduction to the concept. 

One point of improvement in this slide is that the user needs to find row 40 in `loginForm.jsx` instead of you just creating a replace button in Katacoda for it. You could argue that it makes the user more aware of what is happening, and I could agree. The Katacoda documentation states that the user should ideally never have to write any code in a tutorial, so it could be something to take into consideration. You can read more about this [here.](https://www.katacoda.community/formatting.html#learning-experience-approach) There is also a typo that says that I should look for a folder called `component` but it is called `components` in the project. 

## Step 5
This is a very good slide. It explains the concept easily and the single question at the end of the slide forces me to think about the test and the code and what is actually happening. I think this is something you should apply to all the slides. One single question that forces me to take one extra second to think about what I am doing. This works much better than the first slide when it instead was three questions. 

## Step 6
The first code snippet does not have the `Copy to editor`-feature. Also since the code-block does not have any syntax highlighting and the text does not exactly explain what it is that I should change, this makes it very easy to make a mistake that breaks the code. If you manage to break the code, it is very hard to fix it. The editor you chose to use in Katacoda does not have syntax highlighting which makes it very hard to read code in it. 

This text is a bit unclear 
*"If you run the test suite, one test will now fail. But after the changes you can expect both these tests to pass if implemented correctly."*
It sounds like the two sentences should be separated by some code that changes something. If you mean the changes above, they are already implemented since it was explained before. 

You could force the user to run the tests by sprinkling with executable `npm test` after each step so the user could see the difference. 

Very good that you add a note on how to tackle the problem with e-mail validation in production!


## Step 7, Step 8 and Finish
Very good slides. This should be the standard in how you tackle each slide. Good language and easy to follow. 

The Finish page is also very good. I think it is nice to get a summary of what content I have gone through and what steps I should take next if I want to learn more about the topic. Especially good that you include a link to other sources so the user can easily continue exploring. This could be improved by adding even more links to more sources.
