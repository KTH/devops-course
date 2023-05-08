# Feedback

By Iosif Koen, Pierre Le Fevre

## Disclaimer
We certify that generative AI, incl. ChatGPT, has not been used to write this feedback. Using generative AI without permission is considered academic misconduct.

---
## Overview
### Strengths
- Overall the paper is well written and easy to understand. It provides some solid points about the use of Machine Learning in security contexts. 
- We like the careful stance towards machine learning and the way it is presented as an extension to existing methods, not a replacement.
- The two methods presented are well argumented and include good explanation about their uses and workings.

### Weaknesses
- While this essay mentions Machine Learning tools, we would like to also have a more low level perspective and see some algorithms mentioned.
- We would also like some more tools to be mentioned, not neccessarily explained but at least mentioned for the reader to look up.
- Some sources about the training data quality issues could be provided for the reader, for example some paper or dataset.

---

## Analysis, section by section
### Abstract
The abstract does a good job at summarizing the essay, however the methods shown in the State of the art section are not mentioned. The abstract could be improved by mentioning these tools.

### Introduction
The introduction is well written and gives an overview of possible breaches in software. However we think the parts about historic reasons do not add much to the essay and could be removed or shortened. The part about machine learning especially presents some good points.

#### Dynamic code analysis
Interesting section but could use an example of a tool that does this. It is not a very common method so most likely the reader has not heard of it.

### GitHub
Looks like a header for the ChatGPT section slipped in there. Perhaps something about the GitHub dependabot should be mentioned here, as it uses the vulnerabilities found to automatically patch the software. We especially like the mention of specific vulnerabilities that are common to this day, like SQL injection. Other than that the part about CodeQL is clear and gives a clear view of what is done by GitHub to identify vulnerabilities.

We like the flowchart about GitHub code scanning but would like to see it put inline with the text.

### ChatGPT
The section about ChatGPT does present good points about using LLMs for code scanning. However, ChatGPT has been found to be a vulnerability itself, something that could have been mentioned in the essay.
[For example, this samsung leak caused by ChatGPT.](https://www.techradar.com/news/samsung-workers-leaked-company-secrets-by-using-chatgpt)

Other than that, the points mentioned are good to think about, like how LLMs are likely better than humans at reviewing code. We appreciate the conservative stance mentioned in the final section, as relying soley on LLMs is likely to have some consequences. 

We would also like to have seen some other LLMs mentioned, like perhaps GitHub Copilot, as they may be more proficient at writing code. 

### Discussions
This section does a good job of summarizing the benefits and risks of using ML within security contexts. We appreciate the mention of the truth that success with ML is defined as a percentage, meaning some error will always slip in. It could be a good idea to talk about vulnerabilities that cannot be detected, like zombie attacks or DDOS. Some low level algorithms could also be mentioned if they are especially effective at detecting vulnerabilities. We like the mention of manipulating the input data and model to breach security. The points mentioned are good and the section is well written.

### Reflection
This section provides some good context on the LLM output, and its limitation. We like the fact that papers from IEEE Xplore were included as they are ususally a good source of information. The part about many developers not having sufficient training is a unfortunate truth of real life and it's good that this is mentioned.

However, the section about ChatGPT's limitations and use as a malware creation tool could be expanded as it is a real issue. Many of these filters can be bypassed by using some creative prompts. 

### Conclusion & takeaway
We like the careful stance, nicely rounding off the essay. The takeaway is good and the conclusion is well written.


