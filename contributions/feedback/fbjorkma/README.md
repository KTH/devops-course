# Feedback

## Members
Fredrik Björkman (fbjorkma@kth.se) Github: https://github.com/fbjorkman

# Feedback Automated tests for infrastructure code
Essay: Automated tests for infrastructure code [#1415](https://github.com/KTH/devops-course/pull/1415)

Thank you for the interesting read!
Here follows my feedback divided into the same parts as the essay:

## In general
Overall a good outline for the essay and I could follow a clear structure throughout the entire essay. You wrote about an interesting subject and did not stray away from that subject throughout the essay.
The total word count for the essay is 2197 words when using the linux word count command, which I guess according to previous years example essays would be an acceptable word count.
I think you did a really good job with the language in this essay and it feels like it is well academically written. There were only a few remarks from my side when it comes to some phrasing or spelling and those are marked in each section below (some are just my personal opinion).


## 1 Introduction
In my opinion a very well written introduction. It was at a very good length and brought up a good amount of content in the essay, without going into it thoroughly which made me more interested in continuing reading the essay. 


## 2 Background
I think that the Background overall is good and covers relevant subjects and information that is needed for the rest of the essay. 

I feel that there are some parts here that needs to be supported by some kind of source:
- In the first piece of section 2:
“The appeal of using cloud providers, instead of investing in the hardware yourself, is the predominantly used pay-per-use model and the possibility to scale and provision resources as needed.”
- In 2.1:
I think that what is written about consistency, reusability and transparency, either needs some kind of reference, or an explanation why each of them contributes to its benefits.
- In 2.2:
“By testing the code,confidence in it grows which can empower developers to dare make changes and add features.”
- In 2.3:
The first piece could also need some kind of reference, like for example:
“If the software is not built from the start in a test-driven approach, introducing these concepts later in the development stages could lead to technical problems when trying to apply the automation tools to the project.”

## 3 Types of tests
“On the one end, there is static analysis and unit testing which can give some confidence in the code on the other end... ”
I would have written “At one end" and "at the other end”, but I think I would have personally used “On one hand” and “on the other hand”

Comment on Figure 1. Questions that arose when I first looked at the figure:
What do the pyramids represent? 
What does it mean that the cross-sectional area is larger for each pyramid? 
One could make qualified guesses here, but I think a clarification about what the figure represents, why they look the way they do and the correlation between them would be nice here. Even though I think I understand the figure after looking at it and rereading the text a couple of times, I think that it would be good if you explained the figure a bit more.

In 3.2
“The problem with unit testing in the context of IaC is that it is hard to test units without deploying the code since the code’s functionality often is to talk to the outside world.”
What is the outside world in this piece? I felt that it was a bit unclear what that meant.

In 3.3
“Integration tests pick up from where unit testing lefts off…”
I would rewrite “lefts” to “left”.

No sources at all in section 3.4 End-to-end test, I feel like a lot of the content in that part is written as fact, but has no real support from any sources, so I think it would be appropriate to add some sources there. 

## 4 Conclusion
I wonder where the conclusion from this piece is drawn from? 
“ Instead of deploying it, running test, and then undeploy it each time, we can instead just redeploy each module that we have changed to save time.”
I don’t really feel that I can connect that piece with what has been presented in the essay. This might be me that has missed something and if that is the case, maybe make that part a bit more clear.

Otherwise I think you have written a good conclusion. It is pretty short and concise without straying from the subject and you are reviewing what you have written previously in the essay and also drawing your own conclusion in the end.

## References
I think you have good and seemingly reliable sources. Pretty much all sources were sources that I would trust and many of them were from published academic works, which improves the reliability in my opinion.

I think as mentioned earlier in the sections that there are some texts that would need some references. Those are mentioned in their respective section above.

I am a bit unsure about putting the reference outside the punctuation as you have done in the following two cases:
In 2.3:
“...then it could lead to deploying bad code to production. [6]”
In 3.2:
“...each unit performs as expected. [8]”

Depending on what reference style you are using, you might want to be wary of how you reference here. In general I think that it might cause confusion about what actually is included in the reference when you put the reference outside the punctuation. I understand that you might want to include multiple sentences in the reference and instead of putting the reference after each sentence you can for example in 3.2 (reference 8), you can start by presenting the reference e.g. you present that the website guru99 describes unit testing this way and adds the reference in that sentence. Then you can refer back to guru99, when speaking about unit testing without having to add the reference. This might be a bit tricky to fix, but I would personally feel that that would clarify what information is taken from other sources and what information is coming from yourself. 

Link to [9] if you are interested to include it:
https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:24765:ed-2:v1:en
