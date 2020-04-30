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
run `./gradlew clean fullCoverage test jacocoTestReport`, it will give a 100% jacoco coverage report in `build/jacocoHTML`
run `./gradlew clean crash test`, it will run the crash test case to show even a program can be achieve by 100% coverage, it can still have bugs

## Easter Egg
----
run `./gradlew clean run`, the last line of program will print "Devops is interesting !!!!"



The tutorial is post on (medium)[https://medium.com/@jacky19980619/introduction-to-code-coverage-with-jacoco-2c2c7ba307c3]