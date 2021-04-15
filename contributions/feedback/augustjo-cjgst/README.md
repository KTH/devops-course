# Feedback: Automation of web frontend testing using Selenium (Tutorial)

## Members ##
August Jönsson (augustjo@kth.se) Github: [augustjon](https://github.com/augustjon)

Christian Stjernberg (cjgst@kth.se) Github: [christian-stj](https://github.com/christian-stj)

## Proposal ##
We plan on making feedback for Tutorial: Automation of web frontend testing using Selenium. The merged PR is #1015.

## Execution ##

We provided feedback on PR #1213.

The feedback can be seen below.

# Feedback

Authors:
- August Jönsson (augustjo@kth.se)
GitHub: @Augustjon
- Christian Stjernberg (cjgst@kth.se)
GitHub: @christian-stj

## Overall

Very well done on your tutorial. Performing the tasks went well with only minor issues that are easily fixed. The tutorial flows really well and all the material is relatively easy to comprehend.

The time allocated is appropriate (20 minutes). Some might need more, some need less.

It's good that you use the built-in tools of Katacoda like running a command by clicking it and copying it to the editor. Also, the editor itself is very good so tutorial takers don't have to get lost in Vim.

Overall nice work and a very relevant topic! We only have minor suggestions that you may like to address.

## Introduction

- Very good introduction, it really tells what the problem is and what it is that these tools are trying to solve. This makes it more interesting and valuable for anyone taking the tutorial.
- This could be a place to put sources to other material but they would probably be better suited at the end of the tutorial.
- The sentence "before and after we apply our changes." can maybe be clarified. What changes are we talking about? Is it every feature introduced in production or the entire creation of an application?

## Step 1

- It's good to step through the setup steps so we know which tools we are using.
- The apt-update step takes a long time and might not be relevant enough for the tutorial. As most people have Google Chrome, this setup can be done beforehand in a setup script to not take up too much tutorial time and make the tutorial more concentrated on Selenium.
- Setup scripts can also be used to update Python and get rid of the deprecation warnings when installing Selenium.
- You may want to explain why the installation of Google Chrome is needed for the web driver as it is not clear from the rest of the tutorial. This can be avoided by having chrome "pre-installed" as explained above.

## Step 2

- It's good to be able to copy into the editor so it doesn't have to be manually typed or copied.
- The snippets are small enough to read and understand before continuing which really helps.
- The step is very clear and easy to do. I (August) Also tried to get other websites with the ``driver.get`` tool to see if it has the intended behavior. Could be nice to say that the users can try other websites as I did.

## Step 3

- This step is very clear and readable. There were very few issues with this step.

- There was a typo in this sentence "In addition to getting the title of the web page as we did in the last step we can also getting the page URL."  You might want to add a "try" between "also" and "getting"

- You could add a more detailed description to the Herokuapp, perhaps "these websites include simple behaviors that are easily tested."

## Step 4

- The click example is very good and understandable. It might, however, be hard for users to see the difference of the page source in the terminal if they are inexperienced with HTML but then they would probably not be doing this tutorial. It would anyway be good to point out where the tag can be found and the difference from the previous one.

- It is very good that you included sources to where to find out more about XPath.

## Step 5

- It's nice that you have used unit tests here with the standard framework, just as one would in most real-world development.

- In these steps, it might be harder to keep up if one is unused to python, this could be helped by more explanation. For an inexperienced python coder, indentations can be difficult and cause problems in runtime (like when putting a line outside the loop because of wrong indentation). Perhaps the placement of code snippets could be better clarified.

- If one uses the copying tool from Katacoda that automatically copies the code snippet into the file then it will always be placed at the end of the file which might cause problems. You may want to include a warning about this behavior so that the users know what to expect. To be extra clear, you could say that the test should be added into the same class as the other test.

- Also, Katacoda does not seem to syntax highlight the "class" keyword in the snippet which made me (August) miss it (gray text on white background) on the first try.

## Step 6

- The behavior of the tests is easy to follow and explained nicely.

- The last snippet ``self.assertEqual('click', click_element.text)``  could be explained more detailed where to put it.

- Also here the copying tool can produce indentation errors like in the previous step, it would be nice to clarify and explain how it might work.

- When you refer to the ``element.click()`` it should be ``button_element.click()`` which is written in the code snippet.

## End

- It would be nice if you included resources and links for where to read more about the tools, just like you have with XPath. For example, you could add a link to the [wikipedia](https://en.wikipedia.org/wiki/Selenium_(software)) site of Selenium the homepage of the [Selenium framework](https://www.selenium.dev/).

- I really learned the basics of frontend testing using these tools just as I was promised. The content is a great kick-start for anyone who wants to get into the world of front-end testing.

## GitHub README

- In the submission README you should add the repository of the scenario so it is easy to find.

- In the GitHub repo of your scenarios or in the submission, you could have a more descriptive README of your scenarios and why you chose specifically that topic.

## Summary


The tutorial is well constructed and easy to follow for an intermediate user. The steps are not too long and you make good use of the tools that Katacoda provides.

In general, there were not som many errors and bugs that we could find. The text could be a bit more descriptive in some places to avoid misunderstandings. The most critical thing is the use of the auto copying tool that is available. If you only use this tool then the code would not run as intended and you would be stuck on one step.

Try to have a disclaimer about the copying tool in the intro of the tutorial or before code snippets where the placement matters that the copying tool should not be used and instead try to explain where to write/copy the snippet more precisely.
