# Tutorial Proposal
## Members
Marcus Jonsson Ewerbring (marcusew@kth.se)
Github username: Marcus9512

Diego Leon (dleon@kth.se)
Github username: dieflo4711

## Feedback 
We have now updated the tutorial with the feedback and focused to give better background knowledge and originality. The feedback suggested that we should compensate for the lack of originality by increasing the readability and the technical depths of the tutorial. What we have done to achieve these criteria are the following.

* We extended “Why should we test our program” a lot, what is unit testing now contains example, guidelines on how to create unit tests, real life examples and motivation why the examples are good unit tests. We also added an example in “what is regression testing” to help the reader understand.  We also reformulated sentences all over the tutorial to make it more readable.
* As suggested, we replaced the “additional test methods” with “More advanced unit test methods” where we in detail explain mocking and property-based testing. We give examples in code, explain when to use them and what the limitations of theses methods are. In order to reach originality by technical depths we also added the chapter “Advanced code coverage methods”. In that chapter we present MC/DC coverage, MCC and Equivalence partitioning with examples on how they work and when they should be used. We also added links to additional documents about the methods and how Nasa explains MC/DC coverage. 
* We removed many images that were related to how you create a class, run programs, etc in IntelliJ, because it was suggested in the feedback. The only images we have left that is related to IntelliJ are images at functions that are hard to find. 
* We got the feedback that the cross-links didn´t work. The links works for us and the other ones we asked. We remade all the links and followed guides on how to implement link anchors in medium. We managed to replicate the bug on a computer with older version of chrome and edge. We also found out that other people experience this bug with Medium also, which makes it hard for us to fix. We could either remove all the links or keep them and it might not work for all the reader. We choose to keep them at the moment because they are very useful for the one they work for, and hopefully medium might fix this bug soon.
* We added fun/interesting facts all over the tutorial and created a section in the end where we collected some of them.

We consider this tutorial being original because it shows the reader many different testing techniques for the reader and introduce 5 advanced techniques. Earlier this information was scattered across the internet, but now you can find them all in one long tutorial. We also have tests and motivation to all techniques in order to make it clear for the reader when to use what.

Previously we passed the criteria: The TA can successful execute all the commands of the tutorial
(mandatory), The tutorial is easy to follow.

We now aim to pass: The TA can successful execute all the commands of the tutorial
(mandatory), The tutorial is easy to follow, The tutorial gives enough background, The tutorial is original, no such tutorial exists on the web, The tutorial contains fun facts or easter eggs.


## Topic
An introduction on how to use unit testing, regression testing and code coverage with IntelliJ. 

Testing is an important software engineering practice and necessary to keep the state of quality of the software product or service under test. We will focus on Unit testing and regression testing. Code coverage provides critical information about where to focus testing, and is an important metric in Software testing.

We are planning to publish this on medium.
## Structure

* Introduction
* Why should we test our program
    * What is unit-testing
    * What is regression testing
	* Automated testing
    * What is code coverage
* Preparation, Download GitHub repository and get started
* A guide to testing!
* More advanced unit test methods
* Applying regression testing to the project
* Advanced code coverage methods
* Extra, Automatic unit test generation
* Before you leave, some fun facts/easter eggs
* Final words


## Medium
The tutorial can be found [here](https://medium.com/@marcus.jonssonewerbring/tutorial-an-introduction-to-unit-test-regression-test-and-code-coverage-with-intellij-b08be1268719)