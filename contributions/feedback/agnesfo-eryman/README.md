# Feedback executable tutorial proposal #1116

## Members
Agnes Forsberg (agnesfo@kth.se) github: agnesforsberg
Elin Ryman (eryman@kth.se) github: rymane

# Completed feedback

Since the tutorial can be made in two different ways, locally or on Katakoda, we went through the tutorial separately. 

# Feedback by Elin Ryman (running on Katakoda) 

## Intro
- Short and concise introduction that clearly explains what the tutorial will teach us and what the end goal is.
- The first sentence of the second paragraph is a bit too long. Consider splitting it up into two sentences. 
- You could add some explanation to what linting is or add a source that explains it. Considering readers with limited experience in the topic, this might be confusing. Automated tests are self-explanatory, but linting is not.

## Step 1 of 8
- As I run on Katakoda, I skipped most of this part, so I don’t have anything to comment on except that you have given the user a link for documentation for other operating systems, which is excellent.

## Step 2 of 8
- The background is well written and explains every concept relevant to the tutorial. Several of the tools are entirely new to me, but your text was easy to understand anyway. 
- You could add some links to external sources if the reader would like to read more about the tools you use. 

## Step 3 of 8
- The project setup and all included files are explained concisely and are easy to understand. I don’t have anything to comment on here. 

## Step 4 of 8
- The “copy to Editor” does not work in this step, the same goes for “insert-lint” later. All of the other “copy to Editor” in the tutorial works fine though. 
- In the step where we have just created our first test I think there is a typo:
> ... where the name should have the same ~~valid~~ **value** as sent in the request.
- A big plus for walking the reader through the keywords used in a clear and structured way.

## Step 5 of 8 
- Great initial description of what mocks are and why you use them.
- This step is straightforward with two new files and two commands to run and you add value to it by explaining every step that the user might have questions about. Great job!

## Step 6 of 8 
- Step 6 begins with a command for installing ESTLint. After the command, the instruction about making sure we are in the server folder before running the command is added.

Since this is a step-by-step tutorial, the user might actually take **one** step at a time and miss this. Consider changing it to: 

> Install ESLint with npm (Make sure that you are in the server folder before running the following command): 
>
> npm install eslint --save-dev.

- The “copy to Editor” functionality does not work when we are supposed to replace the code for  “insert-lint” in step 6. 

## Step 7 of 8
- Great that you have split the code up into several steps, explaining what they do one at a time. This makes it so much easier to understand and follow along. 

## Step 8 of 8 
I forked and cloned the repo and switched into the branch **express-app-complete**. I edited the README, committed and pushed the changes but nothing happened. In the action tab the message “Get started with Github Actions'' is displayed. I have probably made a mistake, so if you can find the error you might want to clear that up in the tutorial. 
You can have a look at my fork here: https://github.com/rymane/katacoda-scenarios 

## Summary:
The tutorial is well written and easy to follow. The language is overall easy to understand, yet formal and professional. As a user who has limited experience with the tools you use, I think you explain every step thoroughly. You guide the user throughout every step and explain every decision you take. Some minor errors found which, if fixed, will make the tutorial even better but even left as is, it’s a great tutorial. Good job! 


# Feedback by Agnes Forsberg (running locally) 

## Intro
- This is a good intro that is clear and user friendly. However, if this really is a beginner’s tutorial some of the wording and phrases need to be explained further. 

- There is also a small grammar error in “For this, to work”, with an out of place comma.

## Step 1 of 8
- You say to run 3 commands to check if the user has node installed, but there are only 2 commands. You also don’t explain what those commands will provide me. Just to run them to check if I have it installed; maybe clarify that those commands will give the versions of node and npm.

## Step 2 of 8
- Very nice page with good information! Good introduction to the subjects if the user has never before worked with these things.

- Small grammar thing: in: “ESLint is a static code analysis tool used to find bugs, programming, and code formatting errors” it sounds like it finds programming, when I think you want to say it finds programming errors.

## Step 3 of 8
- Good information page about the structure of the project! Nothing to comment on.

## Step 4 of 8
- When providing the user with commands to run, it’s always nice to explain what the command will actually do - especially for someone like me who was running the tutorial on my local machine. 

- In one spot you write “click on Copy to Clipboard” when the button says “Copy to Editor”. In these areas where Katakoda automatically creates a file and writes the code, it is a bit unclear when running locally where the file should be. It can be extracted from the text, but it’s not that straight forward.

- The explanation of the keywords is a great addition that really clarifies some of the trickier areas!

- You talk about tests for valid names, but if the user has not themselves looked around the server application, the user might not know this. A minor thing, but it could make things much clearer.

- The note about data mocking might be good for someone who already though about it, but it mostly confused me as to where it was coming from - maybe write a very short explanation.

## Step 5 of 8
- Very good introduction that very clearly describes why this step is necessary.

- You should add a header to the explanation of the functions.

## Step 6 of 8
- Very clear installation guide!

- About running: maybe explain some of the errors and how they are resolved automatically. I assume you added them on purpose, but might make the user wonder what they did wrong. It also looks a bit scary when lint exits with an error code, so maybe explain that that is normal.

- You write: “Note: The file .eslintrc.json is hidden by default.” and I don’t quite get why. It wasn’t for me, and if it is you give no instruction on how to find it.

## Step 7 of 8
- Same as in step 6, you write: “Note: The directory .github is hidden by default.”. Good note, but then tell the user how to find it!

- Very good explanation of how the jobs are created and the different steps! The last note is also very good and explains some of the questions that might pop up for the user.

## Step 8 of 8
- Unfortunately this page is not that well written. For me who had performed the tutorial locally, it was very unclear if I should stay in the express-app branch or switch to express-app-complete. Also, if you have run the tutorial on Katakoda it is unclear if the user should change anything, or if it will work magically by just cloning and pushing (what?). 

- You write: “The final step is to push the file to your Github repository”, but what file? The branch express-app-complete already has all the necessary files, does it not?

- I tried pushing from both branches, and in the -complete branch lint fails, probably because of the same lint issues that we fixed in step 6. If the branch actually is complete this should not fail.

## Summary
The tutorial is well written and mostly easy to follow. It covers many areas, and sometimes lacks some “focus” or depth. For example testing and linting - it is definitely interesting and relevant to the subject of CI, however on those specific pages it’s not completely clear that’s why we’re doing it. It can at times seem like you wanted to explain a lot of different areas, instead of different aspects of one area (which is what your tutorial actually is).

I also wondered about why the tutorial is labeled “Beginner”. I don’t think this is a beginner tutorial, but that could be up to the definition of beginner. You don’t explain many steps in detail, such as what a repo or branch is, or how someone forks a repo. This is fine since this tutorial seems to cater to users with some programming background - but then it is not a beginner tutorial. It also took me 30-40 minutes instead of 20, however I was writing comments during the tutorial.

In general a very good tutorial and I learnt a lot, but it seems step 7 should maybe also be done locally? Maybe look over the last steps! 
Great job!
