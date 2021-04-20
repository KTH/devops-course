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

## Feedback by Anders Nilsson

The tutorial is well written and easy to follow. It was interesting as well as instructive, which resulted in a delightful experience. I would argue that most of the steps were nicely formatted and ordered in a logical order. I have written some comments and improvement suggestions for each step below, but remember that they are suggestions and only chose to implement what you think will improve the tutorial.

### General suggestions:
- **Comment:** I like the short metatexts on each page, which increase the user experience.
- **Format:** Change the title of each step. For now, it says *Step i*, which is contradictory to the title above that says *Step (i+1) of 8*. Configure the titles in the file `index.json` by changing the label `title` of each step. Also, I recommend using the subtitles in the steps as step title instead of *step i*.
- **Language:** Make sure to conduct a final language check before the final submission, for instance, with the automated tool [`Grammarly`](https://app.grammarly.com/).

## Intro page:
- **Comment:** The intro page gives a clear introduction to what the tutorial is all about. I also find it convenient that you mention the prerequisites for the tutorial.
- **Content:** Consider adding a statement that attracts the user to take the tutorial. For instance, by answering the question: Why is automated testing necessary? For inspiration, see [this](https://uplandsoftware.com/cimpl/resources/blog/8-benefits-of-using-automated-systems/) blog post.
- **Format:** Consider removing the point before: "You will be focusing on the Log-in flow of a react project where you will learn:".
- **Language:** Substitute "We expect you to also know" to "We also expect you to know".
- **Reference:** As stated above, I enjoyed that you mention the prerequisites of the tutorial. To further improve, you could add links to resources where the user can catch up with JavaScript and learn React; at least a link to a React tutorial would be sufficient. For instance, you could use these resources:
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
  - [Intro to React](https://reactjs.org/tutorial/tutorial.html)

## Step 1:
- **Comment:** The theory in this step is well presented and gives the user an excellent introduction to why testing is practical. Especially the content under the header: *What are some test strategies?* was satisfying.
- **Content:** I would recommend describing the difference between a stable and a flaky test. I believe that it would be enough with one or two sentences for this. For inspiration, see [this link](https://docs.gitlab.com/ee/development/testing_guide/flaky_tests.html).
- **Content:** It's great that you give some examples of different test strategies. To further improve, you could mention that *step ...* covers TDD later in the tutorial.
- **Format:** I suggest changing the title to "What is a meaningful test?", remove the header "Short on testing", and write its content in italic style.
- **Format:** It's nice that you get an introduction to testing, but you might want to fast forward to the next step without answering the quiz if you are already familiar with testing. Thus, a shortcut is beneficial for experienced users.
- **Language:** Substitute "To be able to" to "To" for clarity.
- **Language:** Consider changing the word "read" in "The test is easy to read." to either interpret or understand.

## Step 2:
- **Comment:** I enjoyed that you have utilized the Katacoda {{execute}} keyword for the commands since it makes them much easier to execute and further the smoothness of conducting the tutorial.
- **Comment:** It was nice that it is stated that the installation might take a while and that you provide the user with things to do during the installation.
- **Content:** Remove "We have created a dummy project for you to work on within this tutorial. It is a react project describing a login flow." from point 1 in the setup. It is a bit superfluous since it's stated in the paragraph above.
- **Content:** Remove the `ls` command.
- **Content:** I was a bit confused when nothing happened when pressing the `Submit` button. I suggest mentioning the expected behavior of the login form.

## Step 3:
- **Comment:** The content of this step is clear and well written, especially the description under the header: *React Testing Library*.
- **Comment:** I really appreciated the link to the `Jest CheatSheet`, which definitely is useful while learning testing with Jest.
- **Content:** Make the command `ctrl+c` executable, like previous commands.
. **Content:** Mention that `Copy to Editor` copies the content and creates the file for you. This is not obvious if you are not used to Katacoda.
- **Language:** Missing "are" or "," after "Here" in "Here six good reasons why:".
- **Language:** Clarify the sentence: "It runs test in parallel which makes it has a high speed of test execution". You could rewrite it to something similar to: "It runs tests in parallel, which makes test execution more efficient".
- **Reference:** Even though I strongly like the introduction under *React Testing Library* and I believe that you cover enough in its description, I am missing a link to where you can read more about it. I would recommend adding a link for this. For instance, you could add: "[Click here to learn more about React Testing Library](https://testing-library.com/docs/react-testing-library/intro)" to the end of the paragraph.
- **Reference:** In addition to the `Jest CheatSheet` link, I would recommend referencing the well-documented [`Jest API`](https://jestjs.io/docs/api).

## Step 4:
- **Comment:** It was satisfying to test both correct and incorrect code to understand the behavior of the Jest framework further.
- **Content:** The Katacoda command {{open}}, can be used to open files automatically in the editor. I would recommend utilizing it when asking the user to open the file `loginForm.jsx-`. You can read more about it [here](https://www.katacoda.community/scenario-syntax.html#katacoda-s-markdown-extensions).
- **Content:** Change the instruction: "In components/loginForm.jsx on row 40, change the title from Login form to just Login." to make use of `Copy to Editor` as done in previous steps. For instance, you could create a code block and make use of insert, which replaces <code>Login from</code> by <code>Login</code> with the following code when `Copy to Editor` is clicked:
```html
<pre class="file" data-filename="{FILE_PATH}" data-target="insert" data-marker="Login form">Login</pre>
```

## Step 5:
- **Comment:** Overall, an excellent page!
- **Content:** The only thing I think could be clarified is the Jest tests. A short description of each test is sufficient, especially for users who are not used to testing with Jest.

## Step 6:
- **Content:** The first code block is a bit messy. You could use the keyword `replace` to get it nicely formatted and highlighted, as in the case of the other code blocks. You can read more about it [here](https://www.katacoda.community/scenario-syntax.html#katacoda-s-markdown-extensions).
- **Content:** As part of the first quiz, the correct answer of test naming does, in my opinion, not match well with the naming of the implemented tests. Resolve this by making the naming in the quiz more general and not specific to the input numbers.

## Step 7:
- **Language:** Substitute "will" to "with" in: "Integration test will full mocking".

## Step 8:
- **Comment:** It is satisfying that you include test coverage. Well done!
- **Content:** Even though the part about `Docker` is well written, it feels a bit out of topic.
- **Content:** I think it is convenient to write a short statement about the other coverage measurements as well. At least branch coverage should be covered.
- **Language:** Missing "tests," after Jest in the sentence: "To check the Code Coverage of our written Jest we have added a code coverage command in our scripts in the package.jsonfile:".

## Summary page
- **Comment:** It is nice that you have included a few suggestions of what to do next. To further improve it, you could include additional links to some resources you find good for each topic!