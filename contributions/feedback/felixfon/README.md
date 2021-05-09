# Feedback proposal on essay #1294
## Members
Félix Fonteneau, (felixfon@kth.se), github: [FelixFonteneau](https://github.com/FelixFonteneau).

## Pull requests

Essay proposal pull-request: [#1069](https://github.com/KTH/devops-course/pull/1069)

Essay submission pull-request: [#1294](https://github.com/KTH/devops-course/pull/1294)

Correction proposal to the essay submission pull-request: [#3](https://github.com/isacarvid/devops-course/pull/3)

# Feedback

In summary, it was a good essay to read and learn about this subject. The text was appropriate and present a problem of DevOps and testing. I pinpointed some elements that are good to work on in my opinion!

### 1. Introduction

The introduction is good in the sense that it gives examples and facts to motivate the reader to continue reading. Nevertheless, there are some elements to consider.

In general, the introduction does not define very well the concept of code coverage. This introduction is good if the reader has a certain background but a neophyte can be easily lost. I would define deeper the concept of code coverage, explaining the function, statement, branches, conditions, and line coverage than giving a lot of examples. Otherwise just by answering more precisely to the question “_But, how to know then if a particular line, statement, branch, or decision is covered by the tests or which one isn’t covered in any test?_“

In the same way, the sentence “_Code coverage is a metric that is used for describing the level of coverage by the tests._” [part 1.1]. This sentence tries to explain code coverage with code coverage itself in my opinion, it can be good to have a simple and easy-to-grasp definition before the examples. E.g. “_Code coverage is a metric used for describing the level  of how much of source code of a program is executed/tested in a test plan_.”


### 2. Discussion

This format of the discussion is good by having multiple parts complementing each other. In fact, it’s good to talk about high code coverage and the pro & cons. But in general, one great element that misses in the different parts is the application of code coverage. In other words, what context and what type of application needs high code coverage and what type of application needs less? We can imagine that the software for spacecraft should have a higher code coverage than a simple web server with a risk-less application. Furthermore talking about a risky mission like space software, it is not even sure that 100% of code coverage is reasonable, see [[1]](#References).

I think it was good to insist on the fact that 100% code coverage can be still problematic and not guarantee perfect software. In addition, you could also have insisted on the irrelevance of this behavior, writing a test is a cost and you cannot waste time, effort, and money to achieve a precise percentage of code coverage. It could be interesting to find data on the money/time wasted to keep high code coverage compare to the maintenance of low code coverage projects. But it is not an easy task since it is confidential data on companies.

The part about the auto-generated tests is great, I can add a citation of Martin Fowler to that: “_I would be suspicious of anything like 100% - it would smell of someone writing tests to make the coverage numbers happy, but not thinking about what they are doing._”  [[2]](#References)

This part 2 was great, but always think to give a precise example and keep it to demonstrate your ideas.

### 3. Conclusion

The conclusion is good and sums up very well the essay.

### 4. References

I like the presentation of the references, the page is clear and dated. However, to upgrade it and make it easy to manipulate you can create two types of clickable links for them. First, hyperlinks that connect the “[nb]” in the text to the right reference on the last page. Then, links to connect the URL of references on the last page with the website. The two can be done easily with latex using the “_hyperref_” library.  [[3]](#References)

Note to read your essay again before submitting, there some typos and easy mistakes to correct. (e.g. “_for instance, let say_” without majuscule at the second paragraph of part 2.4).

Also, I didn't see any occurrence of the reference [9].


Good work overall! :)



# References

1. [Is 100% Test Coverage a Reasonable Requirement? Lessons Learned from a Space Software Project](https://www.researchgate.net/publication/319141355_Is_100_Test_Coverage_a_Reasonable_Requirement_Lessons_Learned_from_a_Space_Software_Project), Christian R. Prause, November 2017.
2. [TestCoverage](https://martinfowler.com/bliki/TestCoverage.html), Martin Fowler, April 2012.
3. [Hyperlinks in latex](https://www.overleaf.com/learn/latex/hyperlinks), Overleaf.



# Criteria I think I fulfilled (Aiming for P+)

| Criteria
| -----------------
| The feedback includes both strengths and weaknesses about the task
| The feedback is provided 4 business days before the task deadline
| All points are clearly actionable ([PR on PR](https://github.com/isacarvid/devops-course/pull/3))
| The feedback is substantiated (676 words)
| The feedback contains pointers to additional material
| The students act upon the feedback they receive

