# Feedback proposal (Essay): property based testing #1177

## Members

Charlotte Andersson (charande@kth.se)

## Proposal

I plan to give feedback to the essay proposed in PR [#1177](https://github.com/KTH/devops-course/issues/1177).

## Initial PR
Essay: property based testing [#1177](https://github.com/KTH/devops-course/pull/1177)

## Essay submission PR
Essay Submission: Introduction to Property-Based Testing [#1345](https://github.com/KTH/devops-course/pull/1345)

## Feedback for essay

### General comment
Overall, the essay is very interesting and it manages to capture the essence of what property-based testing is in an informative way while still keeping it under 2000 words. A general comment as something that could be improved is the transitions between different sections and trying to create a red thread through the essay so that it flows better and becomes easier to read. 

If anything in my feedback feels unclear, don't hesitate to reach out to me and ask questions :) Email: charande@kth.se

### Title 
The title is very simple and clear which makes it easy for the reader to know beforehand what the essay will be about. An interesting alternative could also be "Introduction to Property-Based Testing and how it compares to Traditional Testing." 

### 1. Introduction
The introduction is easy to follow and gives a brief overview of what the essay will contain which is exactly what you want the introduction to do. 

You also clearly point out how this topic relates to DevOps.

Some suggestions:
It could be a good idea to mention and introduce a few topics that you will discuss in your essay such as generators and shrinking in the introduction. 

The last sentence comes off a bit weird. A suggested change: "This essay aims to introduce property-based testing, explain how it works and how it compares to traditional tests, as well as give suggestions of when to apply property-based testing."

### 2. What is property-based testing?
Has a good segway into the next section.

Some suggestions:
The title of this section is pretty long and could perhaps be shortened to just "Property-based testing" since this section is about explaining Property-based testing.

In the first sentence, "Property-based testing is to generate tests based on property requirements and features", perhaps you could specify examples of what these property requirements and features are, as it is not clear from the text.

Also, "It can detect many bugs in many categories" raises the question of how? Even if you go into more detail later in the essay, if you could explain how it can detect many bugs in many categories in a short sentence in this section then it would make it a lot easier for the reader to understand.  

#### 2.1 Basic idea of Property-based testing
This section is very clear and the figure is a great addition to the text for clarifying properties.

The last sentence is a great segway into the next section!

Some suggestions:
The sentence "As known to all" might come off as subjective and wrong tone for this essay even though I agree with you that this part is common knowledge. Perhaps removing that part and just beginning the sentence as "Multiplication has two important properties:".

#### 2.2 Generator
A good introduction to what generators are and how they relate to property-based testing.

Good using an example of a tool (PropEr) and how generators are implemented in a specific tool.

Some suggestions:
The sentence "Programmers can also utilize the combination of basic generators more complex data" is hard to understand exactly what you mean. Perhaps you can rephrase or elaborate to make it clearer.

#### 2.3 Shrinking
The first sentence is really good and clear in a way that it not only explains what shrinking is (briefly) but also what its benefits are.

Some suggestions:
The paragraph below figure 2 could be rearranged. Right now it is unclear why it doesn't pass the test and it isn't explained until the sentence "In this example, the fault...". If you move this sentence right after the first, it would be more clear to the reader. 

### 3. Comparison with traditional tests
This section is great as it puts property-based testing in relation to something else, in this case, traditional tests. This relation really strengthens the essay. Good work!

The use of figures to differentiate between the two and really demonstrate the difference in terms of LOC makes the message of this section come across stronger.

Some suggestions:
I would suggest exchanging the word "boring" with "tedious" or "time-consuming" to sound less subjective.

### 4. Tools for property-based testing
This section adds to a deeper understanding of property-based testing by taking into account real usage through tools. It's great that you mention many different tools and what programming language they "belong to", as well as go into the difference between two tools, QuichCheck and PropEr, for Erlang and how they differ.

Some suggestions:
The sentence "Then, the authors of the QuickCheck build QuviQ, a company to supply the services of QuickCheck for business customers, and they build QuickCheck for Erlang", is a little unclear what you mean, especially the last line "and they build QuickCheck for Erlang", so perhaps rephrase it. Perhaps instead of authors, "inventors" would be a better word since they invented the tool.

It is unclear why "Developers should choose tools for property-based testing...". Motivate why after that sentence.

### 5. Evaluation and discussion
Good discussion of the pros and cons of property-based testing and also relating it to unit testing.

Some suggestions:
The sentence "If there are a lot of possible combinations of inputs which might cause problem, it would be hard for developers cover in traditional unit testing." is hard to understand. Perhaps you could change it to something like: "If there are a lot of possible combinations of inputs it might cause problems that could be hard for developers in traditional unit testing to cover" (if this is what you mean). Perhaps exemplify what such a problem could look like to make it more understandable.

The last sentence feels incomplete. When you write "whether" there need to be two options, so perhaps changing the sentence to: "Developer teams need to decide  carefully whether or not to apply property-based testing based on multiple factors."

### 6. Conclusion
Great and easy-to-follow summary of the essay.

Some suggestions:
Future research should be in the discussion part of the essay. A good rule of thumb to think of is that nothing new should ever be introduced in a conclusion.
 
The conclusion is summarized but the last sentence should tie the entire essay together. For example: "While there are many advantages with property-based testing, it is not yet a complete replacement for traditional testing."

## Criteria you are aiming for

### Format
The format is in PDF

### Title
The title of the essay is good.

### Well-structured
The structure of the essay follows an easy to read format which makes it well-structured

### Introduction
The introduction is good, but could use some improvements (see the comments I made above)

### Conclusion
The same thing with the conclusion, it is good but could use some improvements (see the comments I made above)

### Self-contained
The essay is definitely self-contained, and one can understand it without having to do research beforehand.

### Figures
The essay contains good figures because they contribute to the reader's understanding

### Sound
Data, statements, examples, and most things mentioned are referenced by credible sources.

### References
Most sources are articles published in scientific journals making the references reliable sources. There are 14 sources.

### Elegant
It is done in LaTeX.

### Relevant
The topic is relevant to DevOps