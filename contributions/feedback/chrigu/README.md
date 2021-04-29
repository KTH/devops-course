# Feedback on #1215 Serverless Applications on Heroku
This is feedback on [#1215](https://github.com/KTH/devops-course/pull/1215), a tutorial about serverless applications on Heroku. Created by Axel Pettersson (axp@kth.se) and Felix Seifert (fseifert@kth.se).

## Members
Christopher Gustafson (chrigu@kth.se)
Github: [ChristopherGustafson](https://github.com/ChristopherGustafson)

## Strengths

Overall this tutorial is great and was a pleasure to work through. One of the things that you managed to do really well was the structure and presentation of the tutorial. The tutorial has clear headings and sections which divide the tutorial into thought-out parts. Code snippets and shell commands are presented clearly which makes it easy to follow along in your own shell. The table of contents makes it easy to navigate to different parts of the tutorial.

Another thing the tutorial does well is to link to additional resources. This is a great way of making life easier for the reader if there is some part which you are either less knowledgable in or just want to know more about.

## Potential Improvements

One part which I believe could be improved is the introduction and the explanation of serverless. The concept of Serverless and FaaS is only described briefly in the beginning. Since this is the main topic of the tutorial it would be nice to have a longer description of Serverless to help the reader really understand the concept. It would also be nice to have some examples of how serverless can be used, and practical examples where serverless is a good option. That way, the reader knows while going through the tutorial the benefits that knowing what you present in the tutorial, beyond the practical aspect of setting it up on Heroku. I know that there are some readers who don't want to read this kinds of things however, so also add a note and link to skip right to the tutorial if one would like.

When you explain how to create the Heroku app I believe the command "heroku create example" should be changed to "heroku create" since the current command tries to create a project called example, which is a taken name. You describe the naming aspect in the paragraph so I assume this is the command you intended.

The section "Trigger HTTP Requests" also has room for improvement. When I walked trough the tutorial I found myself typing the commands in the order you presented them, which as you explain in the tutorial, resulted in errors since the first set of commands where not complete. I believe that this might become annoying for the reader. A better way to do it could be to instead present the final complete command in the beginning of the section, and then go on to explain it step by step. This would be good for two reasons. Firstly the reader would be aware that the first command is what should be executed in the end, and that the partial commands are not what is supposed to be typed, avoiding the scenario where the reader gets a bunch of errors. Secondly if someone reading the tutorial only is interesting in getting it up and running and already know what the command does, it is a nice way to provide the final command without having to read trough the individual steps of the command.

### Summarized actionable improvements
* Add a longer description with examples of Serverless to give the reader a better understanding of the concept.
* In the section "Upload Code to Heroku", change "heroku create example" to "heroku create".
* In the section "Trigger HTTP Requests", add the full command in the beginning of the section to avoid confusion and help eager readers.


## Grammar/Spelling mistakes
I figured I would write down some grammar/spelling mistakes I found which are easy to fix.
* "Architecture", paragraph one, row one: "create serverless function" &rarr; "create a serverless function"
* "Architecture", paragraph one, row two: "withing" &rarr; "within"
* "Trigger HTTP request", paragraph one, row two: "inser the name" &rarr; "insert the name"
