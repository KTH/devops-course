# DD2482- “Ethics of Canary Testing: Users as Guinea pigs” Feedback

*Gatien Ducornaud (gatien@kth.se) - 16/05/22*

## Overall feedback

### Strong points:
- The essay really hammers down its key points: after a good reading, it is easy to state the author’s point of view of the matter, whether it is key problems or their solutions.
- The flow of the essay seems very natural (what it is, what is solved, what are the problems, how to mitigate them), the structure is easy to follow and the sections don’t encroach on each other while still answering well to one another. 
- The essay also has a look at both sides of the issue, so from the service provider’s perspective, and from the user’s.

### Weak points:

- The language is not adapted for an academic essay. There are a lot of typos and word use that seem out of place in the context (examples are given in the following sections of this feedback). Repetitions are also often present in sentences following each other. The references also seem to be broken.
- The essay does not truly answer its question: it is often mentioned that it could lead to “ethically questionable practices”, but does not elaborate on why they are questionable, and what ethical principles are at use.
- The examples and the literature given are too broad: a example with data (if it is available) would empower the argument, or at least a pretend scenario to explain the utility in concrete terms

*Some possible way to address the weak points and consolidate the strong ones is given after the detailed feedback section.*  

## Detailed feedback

### Introduction
The introduction seems appropriate for the essay as it gives a general overview of the topic, but somewhat morphs into a conclusion in itself, as it presents the topic, the issues and the solution. A better approach may be to state the main question clearer (what are the kinds of ethical problems), and leave the solutions to be developed longer after.  
Another point is the following sentences : ”When developers are presented with the ability to target things towards specific users certain ethical concerns presents themselves. When the power to target users and to evaluate how they respond to different things appear developers may run the risk of engaging in ethically questionable practices”
These two sentences are a clear repetition of one another, without adding much additional information.

### What is Canary Testing

There are some capitalization problems (“Coal miners”), and some typos. For example “. the new version of the service to a small subset of users of the application or service and if evaluation metrics indicate [...]” is not a proper sentence. The references also seem to be broken (not the one meant to appear).

However the topic presentation is clear enough and benefits from the visual explanation.

An actual example or a pretend example would have been a great addition to see how to use it. See [[2]](https://launchdarkly.com/blog/what-is-canary-testing-a-detailed-explanation/)  for an example of that.
On a less important note, a quick difference between it and other release methods like the one started in that part with Rolling release may add some clarity for people already familiar with other methods (see [[1]](https://thenewstack.io/deployment-strategies/) for an example).  

### Benefits of Canary Testing 

The first paragraph is a lengthy repetition of the same idea, and could benefit from the “to the point” style present in the rest of the essay.  
The introduction of the comparison with other release methods is an interesting idea that could be developed further (see the previous section).

The next two paragraphs are a clear and concise presentation of the key aspects of Canary testing and do a good job communicating some of the more complicated aspects of the topic.

### Potential Ethical Concerns

This is the section that needs most work in my opinion.  
Paragraph 2 includes lots of repetition with some very slight nuances in each sentence. Different points in the explanation need to be differentiated further, and repetition kept to a minimum (the reference is also broken).

Some sentences like “It’s the users that will be effected when performing Canary tests and they are the ones running the risk of running into issues when a new update rolls out.” are symptomatic of the form issues in the essay (“It’s” for “It is”, “effected” for “affected”, “running the risk of running”). Running the whole essay through a grammar and structure checking tool (like Grammarly) is a necessity.

The main issue is the fact that the ethical issues are not explained at all. This part gives a very thorough and important explanation on how these issues arise in that context, but not what they are. For instance, not once in the essay the word “consent” is written, and it appears (to me at least) that it is a key concept of the topic (whether the user gives consent to be tested upon).  
These notions are only implicitly mentioned (like lack of autonomy in the last paragraph, or opt-in/out in the next section).

However the fact that both points of view of the effect of the issues are mentioned is a very interesting and thought provoking aspect.

### Possible Mitigations

The issue of the objective of the tests are not really specific to Canary testing (or at least I don’t see the specificity that it brings to the problem, except the fact that users will experience the negativity earlier).   
The same goes for the framework presented in the 2nd paragraph. This section would benefit from clearer explanation on how it relates to Canary testing.

The example given is an interesting one; however it would be interesting to explain the difference between Canary testing, and the use of alphas, betas, snapshots and so on. And if they are similar then a lot of other possible examples can be given.

However the discussion about transparency is a crucial one and is very well explained, and the fact that the company and upper management is included in this analysis is a very strong point of this essay.

The debate of opt-in vs opt-out should probably be mentioned as well. For instance, if the Canary test gathers more private information about the user, then under GDPR, it probably needs to be opt-in, as giving information should be an opt-in process (with also an opt-out option at any point that is not obfuscated). See [[3]](https://www.cookielawinfo.com/opt-in-vs-opt-out/) 

As a last example on why one should read back their text : “Most companies are for profit organisations and of course companies need to make monkey”; unless you were talking about a simian goal of companies that I was not aware of (which, to be fair, would probably be better for the environment).

### Conclusion

The conclusion seems a bit geared too much towards the mitigation part of the essay, and not really what problem each solution mitigates. Adding them would allow for a proper wrap up of the essay, while avoiding the repetition between the list and the last paragraph.

## Personal Advice
This is a number of points of advice I think may be relevant to the whole essay.

- Run the whole essay through a tool like grammarly to check for typos and other similar issues.
- Re-read your essay from the bottom paragraph up to break monotony and be more aware of unclear sentence structure and other issues the grammar checker might have missed.
- Try to find/point towards more technical references to give example: scientific papers (even though I have not had much luck finding them myself), or at least technical blogs/ company blogs that discuss the implementation of Canary testing. Also fix the formatting of the references (it doesn’t seem to show enough/ the right ones)
- Going a bit further on the ethical aspects themselves and the current state of the debate regarding them would be a great add to the essay.

## Conclusion

The draft of the essay I received clearly had some issues.
I do however think that most of them are fairly superficial and all of them can be solved if given more time. The structure in itself was easy to follow.
What I want to highlight is the fact that the essay provided a valuable addition on the topic with the ability to consider different points of view (user, developer, company…).
If the main issues are fixed, the essay will make for a pleasant and thought provoking read.

## References
For differences between deploy [1] https://thenewstack.io/deployment-strategies/  
For example of canary [2] https://launchdarkly.com/blog/what-is-canary-testing-a-detailed-explanation/  
For opt-in/opt-out [3]  https://www.cookielawinfo.com/opt-in-vs-opt-out/ 

