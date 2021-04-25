Link to original feedback comment: https://github.com/KTH/devops-course/pull/1339#issuecomment-826394653 

# Feedback on tutorial [Set Up a Unity Project with Automated Unit Testing using GitLab CI/CD](https://gchang95.medium.com/tutorial-set-up-a-unity-project-with-automated-unit-testing-using-gitlab-ci-cd-22190161e526#b5e3)
Hi Gabriel, 
I had really fun learning more about Unity and GitLab, thank you for putting this tutorial together!
Below is my feedback on it. I have divided it up for each header in the tutorial for it to be a bit easier to follow. Remember that the feedback is just my ideas on how you can make it even better, it is nothing you have to implement unless you want to. :)

## General feedback
1. Add an approx time it takes to follow this tutorial, it says that it is 8 minutes read but it takes longer to actually follow along. approx. I would suggest 30 minutes to one hour depending on the users’ previous knowledge and installed packages (when things run smoothly ;) ) 
2. Add the level this tutorial is on (beginner, advanced, etc.)
3. Add what knowledge is good to have prior to this tutorial? What languages do I have to know? Do I need to understand Git? Do I need to understand Unity? etc. 
5. Fix minor spelling errors and grammatical flaws. Eg “a HTTPS URL” instead of “an HTTPS URL”. I recommend running everything through eg. [grammarly](https://app.grammarly.com/). It is a free and fast tool to check for typos and grammar errors.

## Introduction 
1. Change the unity link to https://unity.com/products/unity-platform to directly redirect the user to the about page
2. Explain in a sentence or two what Gitlab CI/CD is (in addition to the platform link). Eg. “Gitlab CI/CD is a service for continuous integration (CI), which builds and tests the software whenever the developer pushes code to the application, and continuous deployment (CD), which places the changes of every code in the production which results in everyday deployment of production.”
3. Change “human factors” to “human errors”. Human factors is an umbrella term that also includes the positive contributions of the human touch
4. Change `eliminating manual work` to `reducing repetitive work`. Even when you automate your work there is always some level of manual work you need to perform to make it run.
5. If you take on the change of introducing CI as suggested in step 2 you can remove the parts that explain CI in the fifth bullet and just explain that “Automated testing can evolve to Continuous integration”

## Prerequisites
1. Change the first block to be a bit more specific. Maybe somethings in the lines of: "
2. Add an executable command the user can fire in their terminal to check if they already have unity installed and if so what version they are on
  -   If the user has it and runs the correct version tell them to continue to the Gitlab section of the tutorial
  -   If the user doesn’t have Unity installed give them the terminal executable commands with eg. `sudo apt install` to be executed directly in the terminal instead of having to spend time searching on external sources. [Here](https://linuxhint.com/install-unity-2020-2-1f1-ubuntu-20-04/) is a step-by-step guide I used to install it on my `Ubuntu 20.04.2`. The commands can be summarized for this case.

## Creating a GitLab Repository
1. Add the instructions as a numbered list to make it easier for the user to keep track on where they are
  1. Click on the `new project` button in the upper right corner
  2. Select `Create blank project`
  3. Fill in the `project name` and `description`(optional)
  4. Click on the `Create project` button
2. Help the user to fill in the fields by giving them examples and be more specific about which fields the user should fill in and which can be ignored.,
  - Eg. Should the user also change the URL and Slug? Does the visibility level matter? Shall I create a readme too?
3. For extra clarity, you can add print screens with markers to where the different buttons exist. The new project button was unnecessarily difficult for me to find. 
4. Instead of `git clone https://gitlab.com/Gchang95/tutorial-unity-project.git` go for `git clone {yourGitLabUrl}` and add a PrintScreen to where the user can copy the URL from. 
5. Think about the use case where the `./UnityHub.AppImage` is still running in the terminal from previous steps. Should this be closed to be able to proceed or shall an additional terminal window be opened?
6. Explain or mention the `warning: You appear to have cloned an empty repository.` shall it be ignored by the user or acted upon?

## Creating a Unity Project
1. Make it a bit more clear that you expect the users to create the folders "Assets" and "ProjectSettings" inside the repo.
2. I appreciate the prewritten .gitignore file to copy and paste
3. My tutorial experience took a quirky turn in the step “go to the Projects tab and click on add”. When selecting my repo and trying to add it, nothing happens after pressing "add". I've been in contact with you regarding this over email and got the suggestion for a workaround since this is a bug in unity. The guidance I got over email was really helpful and I think that it should also be added as a workaround to the tutorial in case the primary way of creating a Unity project is not working for more users.
4. I ended up creating a new project using UnityHub and putting it inside of my already existing folder. This worked well but introduced some errors further ahead in this tutorial. 
5. Prewritten code is always appreciated because people are lazy! ;) I like how you provided the pre-written test and gave short cut for people who already are familiar with Unity

## Installing the GitLab runner on Your Machine
1. This section was easy to follow which was nice!
2. I liked the explanation as to why we need GitLab runner installed and appreciated how you linked to external guides for additional OS.
3. Good that you used a numbered list for the different commands to execute. 

## Registering the GitLab runner
1. Help the user by showing them where the "settings" button is located
2. Give an example of what a description/name for the runner can be 

## Setting up GitLab CI/CD to work with Unity
1. Since the executable tutorial [must run on Linux](https://github.com/KTH/devops-course/blob/2021/grading-criteria.md#executable-tutorials) I would suggest using it as the main OS of this tutorial.  
  - So instead of “remove | Out-Default it should say to add it if you happen to run windows
  - executable is windows - app image is ubuntu
  - When giving an example of the .yml file, for the path to the unity runner use eg. [...] {{your specific path to your unity}}/UnityHub.AppImage \ [...] so it becomes more clear for the user what exactly we are supposed to replace in that file

## Trying it out
1. Be extra clear for dummies (like me) that you need to be in your project folder to be able to execute the given commands in the terminal
2. I got into the problem of not seeing any jobs running. After being in email contact with you it turned out that I had to do a 'sudo rm /home/gitlab-runner/.bash_logout' since I am using Ubuntu 20.04. Since this tutorial should be aimed for Linux and this is the latest stable version this unity/Linux bug should be mentioned or the link to the workaround stated
3. When solving that error, I ran into issues where my tests were failing even though they were supposed to pass. This is also something you and I have addressed and discussed over email. 

## EasterEgg
I am so happy to see that you have included an easter egg in the tutorial. Fun!!! 
