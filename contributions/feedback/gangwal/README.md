# Feedback proposal on PR # 1305

## *Tutorial for feedback: CI workflow for C++ project using Travis CI and CxxTest for automated building and testing #

## Member 

Megha Gangwal (gangwal@kth.se)
GitHub: [gangwalmegha]( https://github.com/gangwalmegha/)

# Proposal
I plan to give feedback to [# 1305] https://github.com/KTH/devops-course/pull/1305 


## Overall feedback

The tutorial is a on a subject of interest. The Katakoda platform is quite structured, and it also provides the bash environment to run the code in a simple way with access to the tutorial instructions on the same screen

I was quite engaged with the tutorial. Overall nice work and a good topic. I only have minor suggestions that author may like to address
 
1.	Though the flow of tutorial and instruction is simple and logical, the instruction could have been broken into smaller numbered steps for better readability. 

2.	The time allocated is 15 min is little, short if one wants to read the instructions, create the files using Vim and run the code as well. I believe a 30 min duration will be more realistic as it will give the tutorial learner good time to perform all the steps properly.

3.	As the focus of the tutorial is continuous integration using the Travis CI and Cxxtest, it would have been good to provide the needed learning sources  links in the introduction itself. It would have kept the focus of tutorial taker on the objective of the tutorial

4.	There were issues in performing the actual activities in step 2 and 3, which I am highlighting in the feedback for specific steps.


## Introduction

Introduction is easy to understand and goal oriented. It gives the learner an overall idea of the flow of the tutorial. As mentioned in point 3 of the overall feedback, it can be further enhanced by including some information about Travis CI and CxxTest as this will be a new topic for most of the tutorial taker like me. 

## Step 1

Step 1 was mainly focused on creating various code files and header files. The sub steps were explained well and provided link to relevant material if someone wants to understand a bit more about C++ programming. This step put me at ease as I have limited coding experience on C++. I took some time to understand the various commands on Vim. 

In complex.cpp file inclusion of iostream was missing, now it is included in revised version. 

## Step 2

Step 2 was dedicated for creating the test cases and running the CxxTest. The instructions in this step could be broken down into smaller sub instructions for better readability. However, the information provided in this section was good from understanding the structure of the code and rationale behind it.

This step got bit complicated due to indentation issues in the makefile. It required some effort to fix the errors with the help of tutorial author. The makefile did generate the complex.o file, but it did not generate simple_test.out file.  I try to debug the error for 4 to 5 times and also updated the environment using the following command provided by the tutorial auther

“ apt-get update -y” and “apt-get install -y cxxtest”

I then did all the steps again, but it did not help. The tutorial author was quite helpful while I was trying to fix the issue.

## Step 3

I was not able execute the Step 3 completely because of the above mentioned issues. I could only execute the first command on step 3 and then the next command was not getting executed. If the errors in previous are debugged, then Step 3 could be performed in a quick succession.

However, the activities provided in step3 with regards to Travis CI are  clear and easy to understand.  Link to the repo has been given, which is helpful for the tutorial learner.

## End

It would be helpful for the tutorial learner if you include resources or links to read more about topic for e.g. Travis CI: https://docs.travis-ci.com/user/tutorial/ , difference between Travis CI and Jenkins: https://www.guru99.com/jenkins-vs-travis.html for understanding CxxTest: https://cxxtest.com/

Overall it is a good tutorial, nice efforts by the author..

