# Introduction to Test Coverage
----

## Member
----
- Ho Ting Chan (htchan)
- Martin Gabrielsen (mgabri)

## Proposal
----
we will introducing different type of test coverage in this tutorial, include : 
1. Functional Coverage
2. Statement Coverage
3. Decision Coverage
4. Condition Coverage

and how to generate the code coverage report with jacoco and junit test

## Motivation
----
Testing is an important part in DevOps, it make sure your integrations not changing the past features, but just fixing bugs and adding new features. Test coverage is one of the important criteria in testing as it tells developers which line of codes had been fully tested and which is tested partially or totally not reach in test. It convince developers that the product will work as assumed by high code coverage tests.

## Content
----
- Introduction
- JUnit
- Jacoco
- Functional Coverage
- Statement Coverage
- Edge Coverage
- Condition Coverage
- Coverage on Whitekbox Test
- Coverage on Blackbox Test
- Coverage on protected and private function
- Conclusion

## Answer
----
run `./gradlew clean test -PexcludeTests=**/*Crash* jacocoTestReport`, it will give a 100% jacoco coverage report for whole project in `build/jacocoHTML`
run `./gradlew clean test --tests=library.Crash`, it will run the crash test case to show even a program can be achieve by 100% coverage, it can still have bugs

## Easter Egg
----
run `./gradlew clean run`, the last line of program will print "Devops is interesting !!!!"



The tutorial is post on [medium](https://medium.com/@jacky19980619/introduction-to-code-coverage-with-jacoco-2c2c7ba307c3)

# Repeat
----
## Received comment
1. The `testCaseExample()` method used in tutorial is not a test since it does not include any call to a method under test.
2. The jacoco documentation does not edge and condition coverage [link](https://www.jacoco.org/jacoco/trunk/doc/counters.html)
3. Is it possible to get these coverage metrics? If no do not dicuss them in a jacoco tutorial. If yes, provide the command to get the metrics.
4. The github repo is not well structured. There is a basic example with `main` and `test` folders, but there are many other test classes in the `dev-ops` folder, which is not connected to specific project under test.
5. Whitebox, Blackbox, protected/private are three short sections, which include no code or command.
6. There is not enough background information to setup the environment, navigate in the repo. Also, the tutorial needs to be more interactive.
7. There is not enough background about gradle, automatic build, runtime monitoring or the value of code coverage.

## Modified Part
1. change the `testCaseExample()` from comparing string to comparing string length
2. a. delete the edge coverage and conditional coverage part and add branch coverage part
   b. briefly explain how jacoco get similar result with conditional coverage
4. delete the `dev-ops` directory and change code to run specific class in tutorial
5.  a. delete whitebox and blackbox paragraphs in tutorial
    b. add private and protected methods in `LinkedList` class and write test case for them.
6. a. add paragraphs to introduce Jacoco mechanism
   b. add instruction on how to increase test coverage in the test case mentioned in the tutorial
7. add paragraphs to introduce gradle in tutorial

The updated tutorial had cover the old one on medium and you can find it [here](https://medium.com/@jacky19980619/introduction-to-code-coverage-with-jacoco-2c2c7ba307c3)