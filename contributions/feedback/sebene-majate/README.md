# Feedback - Tutorial: Integrate DataDog in existing app

Feedback to the executable tutorial "[Integrate DataDog in existing app](https://github.com/KTH/devops-course/tree/2021/contributions/executable-tutorial/brogard-despinoy)".

- Tutorial proposal PR: [#972](https://github.com/KTH/devops-course/pull/972)
- Tutorial submission PR: [#1330](https://github.com/KTH/devops-course/pull/1330)
- Feedback proposal PR: [#1071](https://github.com/KTH/devops-course/pull/1071)

## Members
* Sebastian Fagerlind - sebene@kth.se - [@sebberh](https://github.com/sebberh)
* Maja Tennander - majate@kth.se - [@majate](https://github.com/majate)

## Feedback

### Overall feedback
In general, the tutorial was easy to follow, and no problems were encountered during the execution. Furthermore, the content was relevant, and the structure seemed thought trough. We especially liked that you included step 2 where one runs the application without DataDog. This step helps demonstrate how cumbersome logs can be and why DataDog is useful.


However, some things could be explained further to give us reader a better understanding of what we do and how it works. If you feel that some explanations are outside the scope of the tutorial, it could also be an idea to link sources for readers who want to learn more. You might also want to add references to images you have not created yourself.

#### Inconsistent language
For some words/terms you are inconsistent regarding how you write them. Throughout the tutorial you mix between:
- "mongoDB" vs. "mongodb"
- "JavaScript" vs. "javascript"
- "Node.js" vs. "nodejs"

You are also inconsistent with the capitalization of your headers. For the majority of the headers, you only capitalize the first letter of the first word. However, in all headers in step 3 and in one header in step 5 you capitalize the first letter in all words.

Even if these points do not make the tutorial less clear or easy to follow, it reduces the quality of the text in general.

### Introduction
- It is good that you present the steps in advance. This gives us a clear view of what to expect.
- In the presentation of the steps, you refer to your to-do app as "the app" in step 2 and 4, but as "the application" in step 5. Using the same term in all steps would be preferable. (This is a minor detail that we don't think is important, but we thought we might as well mention it.)

### Step 1
- The `What is DataDog?` section feels short. It would be interesting to get some more information about DataDog. Is DataDog popular in the field? How does it work? Link to more information?

### Step 2
- In section `The application` you have the sentence "We deploy the app and the database using docker and docker-compose.". When using present tense here, the reader might incorrectly believe that it is a call to action, rather than a comment regarding future actions which are further explained in a later section. Writing something like "We **will** deploy the app and the database using docker and docker-compose." instead might avoid potential confusion.
- In section `Deploy the app` you mention "the compose file". It might be clearer to write "the docker-compose.yaml file" instead.
- Great that you mention that the `docker-compose` command can take some time.
- In section `Simulate users` you write "observe its activity by refreshing the website". It is possible to misunderstand which website should be refreshed. To reduce the risk of someone refreshing Katakoda, it might be good to specify which website should be refreshed. E.g. replace "website" with "the to-do app UI".
- Your bot is a nice addition to the tutorial. It lets you demonstrate how the logs work, without the readers needing to play around with the UI. However, since the bot acts so often, and since the log only shows the id of to-dos, it is hard to see that your actions in the UI affect the logs. If you made the bot act less frequent or included the to-do text in the log, it would be easier for us to see that our actions in the UI affect the log.

### Step 3
- Missing "the" in "find your API key in the same place as red rectangle". Should be "find your API key in the same place as **the** red rectangle".
- "The information besides 'DD_SITE'" sound informal. Something like "The 'DD_SITE' value" would maybe be clearer.
- It is great that you mention that one might need to update the DD_SITE value.
- In the code snippet in section `Application Environment` the indentation of the env variables looks a bit off. Is it possible to fix it, or is that a problem with Katakoda? The indentation is correct if the code is copied, so it is not really a problem.
- Where does port 8126 (in the code snippet) come from? Is this defined by DataDog or by the to-do app? This type of information would be useful for a reader that want to follow the tutorial when implementing DataDog for their own application.
- In the `Next` section it is stated that "In the next step, you will build and run your compose file". However, this does not happen until step 5. This sentence could be removed. If you still want to mention that we will soon be able to run the program you could instead write something like "In the next step, you will ... , which will be the final step before we can build and run ..."
- It could be clearer that the user doesn't need to install anything on their local machine in this step.

### Step 4
- The sentence in the intro is missing a period.
- The formatting of the headers `Implement DataDog in the application` and `What is a tracer?` does not make it clear that `What is a tracer?` is a subsection to `Implement DataDog in the application`. When they are written after each other without spacing and with the same font size, it looks like the two sentences makes one single header, which is a bit weird. Maybe you want to update the formatting or remove one of the headers.
- When introducing a new term, it is a good practice to explain it as quick as possible since it is harder to follow along if you read a text with terms you don't understand. However, it is not until the later part of the `What is a tracer?` section that you mention the purpose of a tracer. It might be good to put this information in the beginning of the section instead.

### Step 5
- In DataDog the menu tabs have icons instead of names. Therefore, including an image of the AMP icon would make it easier for the readers to navigate to the correct tab.

### Congratulations
- It is great that you put DataDog in a greater context and inspire us readers to explore other topics within DevOps.

### Nitpicks
There was a couple of warnings during the demo: 
- No decription field, can eliminated by adding to the package.json
- No repository field, can eliminated by adding to the package.json
- npm compadible with lockfileVersion@1, but package-lock.json was generated for lockfileVersion@2.
