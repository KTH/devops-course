# Notes

* [x] Structure (we have a decent one)

* [ ] Motivating introduction

* [ ] Deeply technincal (Suggestion, search based software
      specifications along with different coverage measurements and
      their use cases.)
	  
' [ ] Humour (Sarcasm?)
	> All my programs always works, so running EvoSuite is a perfect
	> way of just creating tests
	
* [ ] Nice illustrations

* [ ] Take home message


# Structure

## Introduction

Search based testing, general purpose stuff

- >

EvoSuite **END**
Liten grej om EvoSuite

**END**

1-1.5 min

## Coverage Metrics

* Which ones are there?

* Purposes?

* How do we know if it contributes to the metrics?

* How do we create tests?

2-2.5 min

## Search based programming

* What it is

* Why

* applications

* Examples, ant colony optimization in TSP

2-2.5 min

## Examples and applications of EvoSuite

Add tests to working application to make sure behaviour does not
change

Academia and bug-fixing

Use to see what's missing in you test suite

detect deviations from expected behaviour

1.5-2 min

## Conclusion

Relevant to DevOps

Take home message

1 min





# Introduction

## Rough sketch
Search based testing, general purpose stuff
- >
EvoSuite **END**
Liten grej om EvoSuite

**END**

## Search based testing

Automatic generation of tests

__All my code is always correct, so I just need them for show__

Are there any tools for this?

EvoSuite!

A search based testing tool with the goal of optimising different
coverage metrics

Over to coverage metrics!

# Coverage metrics

* **Lines**

* **branches**

* **outputs**

* **mutation**

which of the above to include?

# Search based programming

* **What it is?**

	Optimisation problems, often solved through linear or dynamic
	programming, or through the use of metaheuristics

* **Why?**

	Linear and dynamic programming does not always offer good enough
	complexities. Need some faster way of doing it

* **Examples**

	Ant colony optimization is one, pathfinding in general
	
# Examples and applications of EvoSuite

Add tests to working application to make sure behaviour does not
change

* Academia and bug-fixing (Currently the largest application)

* Use to see what's missing in you test suite (it optimises coverage)

* detect deviations from expected behaviour (If the tests show that
  3^2 = 8 something is wrong, covers things that you might not have
  tested).

# Conclusion?

* **Relevant to DevOps?**

	DevOps requires tests, a lot of tests, and we need to know that
    these tests are suitable and ensure the correct behaviour.
	Perhaps help with that?
	
* **Take home message**

	Unit testing is not only writing code, there are tools for it as
    well. 
