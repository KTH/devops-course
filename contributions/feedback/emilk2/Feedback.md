*I certify that generative AI, incl. ChatGPT, has not been used to write this feedback. Using generative AI without permission is considered academic misconduct.*

# Feedback on essay: Depending on Dependencies: Securing your codebase on all levels

# High-level strengths
The essay is written in a way that makes it easy to understand the topic conceptually, and it brings up many perspectives to the problem of managing dependencies recursively. 

It is split up in parts that make sense where we follow a red line throughout the essay (with a few exceptions), and the essay also includes a few concrete, easy to understand, real-world examples.

# High-level weaknesses
While the essay is easy to understand conceptually, it falls short in some areas. 

1. The essay focuses mainly on when things go wrong and errors in dependencies. But it would be nice to have some section including one or more of:
    - How do we manage dependencies where the development does not keep up with the "latest" features? \
    I believe this could introduce security vulnerabilities, where a dependency is slow at patching or does not patch at all. 
    - How do we manage dependencies that go stale? \
    (due to, for example, lack of maintainer) \
    A recent example of this is the Go package [gorilla/mux](https://github.com/gorilla/mux) that is, according to GitHub, used by over 100k projects. 

2. Wording\
 Finally, as a minor note, the essay are sometimes hard to follow (hence why I wrote "with a few exceptions" before) due to the choice of words and sentences structure. 


# In detail

## Title and subtitle
The title is rather vague, where it first seems that the essay will include other package managers than mentioned in the essay, such as for Linux distribution apt, dnf etc.

The subtitle mentions "Securing ...", but security is barely mentioned in the essay, apart from the *DevSecOps* section. I would have liked a section about issues with trusting your dependencies. [Supply chain attacks](https://en.wikipedia.org/wiki/Supply_chain_attack)?

Could the title have been made more specific? Or could the subtitle have been worded differently to not include "Securing...", but rather in the lines of "Ensuring safety..." or just "Managing dependencies in your codebases..."

## Introduction
This part is well-written and easy to understand. It starts out by taking a step back to explain the core concept, and is initially very broad. It follows a logical transition where we start with package managers, continue with real-world examples, and wrap up with the problem we are discussing in later sections. 

**Summary**\
\+ Informative\
\+ Explains core concept needed for the essay\
\+ Easy to understand\

\- (Minor) I can't find a reference to the "Figure 2: Trend graph of repository uploads to GitHub, 2018". I believe it is related to *Dependency Vulnerabilities*.

## Analysis
Compared to the previous section, the Analysis section is a bit harder to follow. This is mainly caused by the writing style and choice of words, but sometimes I would have liked some clarification.

Overall though, the section is well-written, with a logical structure similar to Introduction. 

**Summary**\
\+ Logical structure\
\+ The content and the order of it is good\

\- Some parts are hard to follow, and could even need to be read a couple of times\
\- Lack some information about the security aspect of dependency management

**Concrete examples**\
2.2 "In order to alleviate the labour done in 2.1"
"labour done" should probably be something similar to "manual process presented"

2.2 "Dependency mapping is a technique ... which allows the developer to keep track of an overview of the entire application *behaviour*"\
It is not what was written in 2.1 though?\
This is a minor error in this example, but having multiple of these, such as writing "behavior" in this sentence, can be misleading to the reader. 

2.2 "There are many tools one can implement to run this process automatically..."\
-> "... such as X and Y"?\
I would have liked some examples of what tools exist here, similar to how there were real-world examples such as LeftPad and Log4j in the Introduction.

**2.3 DevSecOps**\
This section does a good job explaining the DevSecOps, being short and concise, and how it is connected to dependency management. However, since the subtitle says "Securing..." I expected this section to go more in-depth in the topic of security. 
- What attack vectors are opened up when having many dependencies? 
- How do we protect ourselves?
Do we lock the dependency version? Do we test our dependencies? How do we ensure minimal risk for attacks such as [supply chain attacks](https://en.wikipedia.org/wiki/Supply_chain_attack)?

## Conclusion
This section starts out by summarizing the essay, and does so very well. It is easy to follow and it brings up most of what was presented and discussed in the essay. It ends very nicely with a statement that is in-line to what the essay is trying to convey: *We need dependency management!*

The key take-away is short and is in-line with the essay's message.

\+ Well written, concise and easy to understand\
\+ Summarizes the essay nicely (including most of what was said)\
\+ The final statement and key take-away is in-line to what the essay tries to convey

Side note: "... discussed in 1.1 and 1.1, respectively ..." sounds a bit redundant :)

## Reflection
The reflection is clearly based on what was said earlier in the essay and it does a good job summarizing. I particularly like: "One may even assume that the most secure method would be to write all code from scratch ... still does not guarantee a non-vulnerable project", as it highlights a key point with the essay's topic; the trade-off when using dependencies in your project.  

\+ Well written and summarized\
\+ Brought up a key point of the essay


# Pointers
The focus of the essay was mainly on what could go wrong when a codebase has a lot of dependencies, but also how to detect your dependency in a project. However, there is another aspect that would suit very well, given the title of the essay. Instead of focusing on things that should not happen, could we focus on what could happen? (That we, in practice, can't do anything about)

I mentioned earlier in this feedback report that even large projects could go stale, especially that of open-source projects. One could go check out how projects that depended on [gorilla/mux](https://github.com/gorilla/mux) dealt with it being archived. Did they put up a plan if it would happen again?

