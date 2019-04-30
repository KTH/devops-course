# Introduction 0.5min FR


## Who we are
### Fredrik Flovén, D13, Software Engineering
### Filip Jansson, D14, Software security

- What to say:

Hi guys, my name is Fredrik, this is Filip.
You may know these guys, that's not us, but we share our names with them, which is cool I guess.


---

# Non-deterministic-, aka Flaky tests 2.5min  FR
- On the slide:

(Slide1)
Title: Non-deterministic tests 
Subtitle: More commonly referred to as "flaky" tests
Background: *funny gif

- What to say:

Today, we are going to talk about non-deterministic tests, or as they say in the biz, flaky tests.

The run-down will go like this:

First we will describe what it means for a test to be flaky, as well as why it happens, followed by how to deal with them, in a good way.

Then we will discuss options for detecting flaky tests.

Finally we will round up with some thoughts for you to take with you in your future development careers.

Let's go.

-------------------------------

## What is it? 0.5min FR
- On the slide:

(Slide1)
Title: What are flaky tests?
frag: A test which could pass or fail for the same configuration.

- What to say:

So, what is a flaky test? 
Well, in short, a flaky test is a test which could pass or fail for the same configuration, it is non-deterministic.

## Why does it happen? 2min FR

- On the slide(s):

(Slide1)
Title: Why does it happen?
frag: Bad programmers.
frag: Because we rely on non-deterministic or undefined behaviors

(Slide2)
* Usual reasons:
* Asynchronicity - UI, Dynamic content
* Concurrency - Data races, Atomicity violations, Deadlocks
* Dependencies - State, Execution order
* Resource management - Setup, Cleanup, Caching
* Time - Time zones, time gathering, special occasions

(Slide3)
* Less common reasons:
* Random numbers 
* Imprecise floating points 
* Infrastructure
* Unordered collections

- What to say:

Alright, so now we know what a flaky test is, but why do they happen?
Generally, because of bad programmers, such as I. And this guy. And you.
No, not really, we're not bad, we just don't think of the catastrophic issues that might occur at times when we rely on non-deterministic or undefined behaviors.

So what are the most common reasons for flaky tests?

**Asynchronicity**: 
This is the most common reason for flakyness. Either asynchronicity isn't dealt with at all, or a sleep statement is used. Both are suboptimal. Common in UI tests when tests need to wait on dynamic content.

**Concurrency**:
Writing thread-safe code is hard. Many tests that run with several threads have non-determinisic behaviour due to this, which might happen every other run or every one in a hundredth. Hard to detect.

**Dependencies**:
If a test is dependent on other tests to function, it might start failing from changes in the code which might be completely unrelated to the new test.

**Resource management**:
Test that has resource leaks, improper setups or cleanup might cause flakyness. Tests might run out of memory, encounter unexpected files or have some important part of the setup missing due to poor resource management.

**Time**: Usage of system time, time zones, maintenance times, time gathering

The less common issues are:

**Infrastructure**: Bugs in testing frameworks, browsers versions, CI node failures, network issues, database outage, I/O ops, OS dependencies, hardware specs

Non-seeded random numbers, Imprecise floating points, Unordered collections: Assuming order may cause flaky behaviour

-------------------------------

## Why is it an issue? 1min FI
- On the slide:

Title: Why are flaky tests an issue?

Overall the insertion rate is about the same as the fix rate

> Non-deterministic tests have two problems, firstly they are useless, secondly they are a virulent infection that can completely ruin your entire test suite.

* Difficult to debug, hard to reproduce
* Time-consuming
* Reduces confidence in test suite.

- What to say:

With a flaky test suite comes many problems. For example, If you are relying on a CI where all tests needs to pass before a code change is allowed to be merged, flaky tests becomes a nightmare deal with. Having a flaky test suit will also lead to less confidences in your tests. When builds of the code goes red regularys, the programmers trust in the tests gets reduced. It becomes hard to determine wheter a fail is due to a flaky test or a bug.

Another reson why flaky tests become a huge problem for developers are that they usually hard to resolve. It can be hard to understand why test are flaky and at times they are hard to reproduce.

-------------------------------

![](https://i.imgur.com/UcGiEPh.png =x512)

> It is human nature to ignore alarms when there is a history of false signals coming from a system.

---



# How to deal with it 1.5min FR
- On the slide:

(Slide1)
How to deal with flaky tests

(Slide2)
* Quarantine
* Document 
* Analyse
* Fix

(Slide3)
* Async - Don't use: sleep, Do use: Callbacks, polling
* Concurrency - Depends!
* Dependencies - Isolate the tests
* Resource management - Ensure cleanup and proper setup
* Time - Don't use system time

(Slide4)
* Random numbers - Seed
* Floating points numbers - Don't use it??
* Infrastructure - Mock external resources
* Unordered collections - Don't assume order

- What to say:

**Quarantine**: 
Tests that are flaky should be quarantined until they are fixed. This is important to keep the test suite healthy (get good feedback). 

An alternative is to run a quarantined test suit after the healthy one to gain more data on the quarantined tests. 

**TODO**
**Document**:
It is good to create an issue for the flaky test, and document relevant data about it. Relevant data may be when it happened, what happens when it doesn't do what it should do as well as any data logs. This eases the possibility to reproduce the flaky behaviour.

**Analyse**:
There needs to be an analysis of the flaky tests to find the root cause that it happens. Is the test flaky or is it a bug in the code?
A bug’s best place to hide is a flaky test that developers would assume that something is wrong with the test and not the code.

![](https://i.imgur.com/Uf0HFQM.jpg)

**Fix**:
Finally, the flaky test should be fixed. It is important to resolve quarantined test quickly, otherwise this strategy will lead to reduced test coverage and aquiring more flaky tests, as developers will care less about the overall test suite quality.  Many times, rewriting it from scratch is a good option.


**Asynchronocity**: 
Wait for the content to load. Not perfect, but better.
Do not use sleep. Use callback or polling.

**TODO**
The callbacks solution means that the application can signal back to the test when it can start executing again. The advantage of this solution is that the test doesn’t wait longer than necessary. However, this solution is rarely supported by the testing library and if it is, the application needs to support it too.

Polling is based on a series of repeated checks of whether an expectation has been satisfied.

**Concurrency**: 
There is no good general solution to this problem, it depends on the context. Add locks, fix dataraces, make the test more robust, accept more states etc...

**Dependencies**: Isolate the tests. Clear state. Run tests in random order. Use immutable test data.

**Resource management**: Always clean up after a test, e.g. deallocate meory if needed 

**Time**: Don't use system time if the program will run on other machines. Otherwise, wrap the system clock with routines that can be replaced with a seeded value for testing



**Infrastructure**: Mock the data, enforce closing of resources and synchronization for shared resources.

**Unordered collections**: Don't assume order, check for existence of element
**Random numbers**: Seed 
**Floating point numbers**: Avoid underflows, overflows, or issues with non-associative addition.

-------------------------------


# Detection of flaky tests 3 min FI
- On the slide:

What can we do to detect flaky tests?

- What to say:

### Rerun 1min
- On the slide:

Option 1: Rerun
[Maybe something here]

- What to say:
Let's talk about detection of flaky tests. There exists a few different strategies  how one can detect tests that are flaky. The simplest strategy is known as RERUN.  This strategy is when you run your failed tests a few extra times. If the same test returns two different result, it is marked as flaky.Rerun is supported by many testing frameworks such as Android, Jenkins, Maven, Spring, and Google TAP.

This Strategy is problematic for a few reasons.
Firstly, it creates a large overhead for bigger projects, since the amount of failed tests increases with the size of the test suite
Secondly, there is no real research done on optimal rerun-strategies, we don't know the best timnigs and intervals between reruns
Lastly The rerun strategy finds a rather low % of flaky tests compared to some other methods. Mavens RERUN was evaluated on over 20 projects with known flakes, and it only found 23% of these tests.



-------------------------------

### DeFlaker 2min
- On the slide:

(Slide1)
DeFlaker

(Slide2)
Simplified version to easier explain DeFlaker?

(Slide3)
![](https://i.imgur.com/l4EyAp4.png)

- What to say:
So what's the alternative? Let me present the DeFlaker strategy for detecting flaky tests. Instead of reruning test, this method uses the coverage differentials between versios of the code to find test with flaky behaviour.

This process is done in three different steps(show picture):

First the differential coverage analysis is done, this is done by checking the syntax difference from the Version control system and then an abstract-syntax tree for each changed file to determine where we need to track execution of each change.

In the second phase, which is the coverage collection, the deflaker monitors the identified sections in the previous step during test execution to see when they are executed.

In the last phase the deflaker algorithm marks tests as flaky if:
it previously passed, now fails, and did not cover any code that changed or if it failed, now passes and does not run on any changed code.

The deflaker apporach comes with a few benefits. Most impornantly it has better performance than the RERUN strategy, In the previous talked about evaluation of RERUN, a Java implementation of the DeFlaker found 95% of all flaky tests compared to RERUNS 23%, this is a large improvement. The DeFlaker also scales well with larger test suits, since the overhead per test is very low.

The drawbacks of the deflaker strategy is the complexity it brings, and the larger overhead compared to RERUN for projects with smaller test suits. 


---

# Summary 1min
- On the slide:

Title: Things to take with you

(Slide1)
* Use Callbacks and polling, don't use sleep
* Isolate tests
* Proper Setup and Cleanup policies
* Don't use System Time
* Rerun for small projects, DeFlaker for large projects

(Slide2)
Follow the "DeQuDAF"-principle!
Detect - **Quarantine** - **Document** - Analyse - **Fix asap**
> All temporary solutions tend to become permanent.

- What to say:
Stay away from using sleep together with asynchronous calls, use callbacks or polling instead to keep your tests efficent and unflaky.

Isolate your tests, not test should be dependent on another test to run. 

Have good setup and cleanup policies for yout  tests, this helps a lot for keeping your test suit healthy

Don't use system time, has a tendency of creating flaky tests which are hard to nail down.

For large projects with a large test suite - DeFlaker is a good stategy for flaky-test detection, but for smaller projects a rerun strategy should be sufficient.

Follow the DeQuDaf principle when dealing with flaky tests.
It is of high importance to remove the flaky test from the test suite to keep it healthy, a flaky test suit will lead to reduced trust in the tests. Make sure that the flaky tests are documented so they can be fixed easily. It is important to have a team culture where flaky tests get fixed fast, otherwise this will lead to reduced code coverage.

Quarantine flaky tests (but fix them soon!)


-------------------------------


