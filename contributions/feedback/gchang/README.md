# Feedback Essay: DevSecOps - the new DevOps? [#1249](https://github.com/KTH/devops-course/pull/1249)

### Members
Gabriel Chang (gchang@kth.se)
GitHub: [ChangGabriel](https://github.com/ChangGabriel)

### Proposal

I would like to give feedback on the essay *DevSecOps - the new DevOps?*, [#995](https://github.com/KTH/devops-course/pull/995).

# Feedback for essay "DevSecOps - the new DevOps?"[PR #1249](https://github.com/KTH/devops-course/pull/1249)

## General feedback
Overall this is a very well written essay. It was interesting  to read about the importance and challenges of integrating the security aspects in the DevOps process. The essay shows balance in argumentation as it brings up whether DevSecOps is needed as a new term or if security aspects are already included in DevOps.

### Strengths 
* The essay is well structured. The essay starts with introducing the problem with security in software development, then moves on to introduce DevOps and DevSecOps. The later parts bring up concrete examples of DevSecOps practices and discuss challenges that arise when integrating DevSecOps into a company's workflow.
* The essay is self contained. The essay provides all necessary information needed to understand the material presented, very well done!
* Appropriate use of figures and listings that supports the text.
* The language is professional and academic.
* Despite the limited wordcount, the essay has a good conclusion that rounds the essay nicely. You answer the question asked in the beginning.
* Correct use of references and are appropriate in number and quality. References are presented well and clearly.

### Primary improvements
* There are some grammatical errors and wrongly formulated sentences that unfortunately disturbs the flow of the text.
* It would be interesting if the essay expanded on the part about whether DevSecOps is needed as a term. Due to limited word count I can understand why this wasn't elaborated on more.
* If possible include even more figures in your text. e.g in the DevSecOps practices section, have a figure for the tool security incident process' different parts.
* It would be nice to have a single sentence paragraph in the introduction about the purpose of the essay; what will the reader learn by reading this essay?
* The DevSecOps practices section needs improvement. Mainly strengthen the this section's connection to DevSecOps

## Introduction
A very good introduction that contains a good motivating reason as to why there is a need to have secure practices in software development. The motivation is supported by statistics and examples. There is a strong red thread throughout the introduction going from the traditional waterfall model to DevOps and finally why DevSecOps may be needed.

At the end you ask the question "[...] will DevSecOps replace DevOps?" and the question you answer in the conclusion is "Is DevSecOps the new DevOps?". It would be good to have the questions match verbatim. Otherwise it can be a bit confusing at the end. Having the question in italics would also be good.
There is a footnote in the beginning and I don't know if it's proper. It would probably be better to make it into a normal reference.
I will now go through some grammar errors and sentences that can be rephrased to improve the flow better.
### Grammatical errors
* At the end of the second paragraph, the tempus is wrong, I suggest : "It allows requirements to be changed, developed, released, and maintained continuously"
* In the final paragraph, I recommend rephrasing the second half of the first sentence. "e.g sacrifice of security for speed/agility, an afterthought in the process and environment risks" It is a bit unclear. Isn't the challenge to balance between security and speed/agility?
* In the final paragraph, "It takes the continuous development and deployment process of DevOps and implements security
into that process." could be shortened to "[...] DevOps and extends it to include security."

## DevOps
A good overview of DevOps is given in this section. This section presents relevant information that is needed. The "Features that characterize DevOps[...]" paragraph is very well written and concise. 

The second paragraph with examples could use a good leading sentence. Currently the first sentence doesn't relate as much as it could to the rest of the paragraph. Otherwise you give a good background on DevOps.
### Grammatical errors
* The sentence: "The process of DevOps looks as in figure 1" could be rephrased to "The process of DevOps can be seen in figure 1" to be more clear.

## DevSecOps
In this section DevSecOps is brought up and introduced more in depth. I like how DevOps is brought up and how it might be difficult to ensure security with all the new technology that is used to speed up and automate the development process. I also like the transition between DevOps and DevSecOps. Very nice figure. Going through the same points in the last paragraph here as in you did in the DevOps section was a nice touch. It made it easier to follow.

It could be good to bold or italic the four categories culture, automation, measurement, and sharing in the last paragraph both here and in the DevOps section. It makes it easier to distinguish the categories when reading. Other than that there is not much else to improve in this section.

### Grammatical errors
* In the last paragraph the sentence "Measuring also includes measuring monitoring and measuring system metrics as with DevOps." is a bit unclear. It could be rephrased to "Measuring also includes measuring the monitoring process and the system metrics like in DevOps."

* The sentence "This for the security engineers to attack potential problems earlier [...]" should be adjusted to "This is so (that) the security engineers can attack potential problems earlier [...]"

## DevSecOps practices
This section presents examples of tools that can be useful regarding security. I think this section needs the most improvement. You have a good foundation but the critical connection to DevSecOps is missing. Are these tools used in DevSecOps? It is also unclear how the three main building blocks relate to the rest of the section. Perhaps a better transition is needed. I'm unsure what you mean with security practices/DevSecOps practices. How are tools and practices related?

### Grammatical errors
* The word books in "The books ”Hands on Security in DevOps” should maybe be book?
* The same sentence could also be shortened to "The book ”Hands on Security in DevOps” lists three main building blocks when considering security"
* The sentence "These open-source software saves companies a lot of time and money, but it can also pose a security risk." should be changed to "These open-source softwares save companies a lot of time and money, but they can also pose a security risk. "
* "The first part of the document is Preparation." maybe change "document" to "tool".

## Challenges with implementing DevSecOps
I find this section to be the most interesting part of the essay. This is a very well written section. I like that you bring up both internal and external challenges and then go on to also talk about how automation brings further challenges when integrating DevSecOps. Last paragraph discusses whether the term DevSecOps is necessary or if security aspects are already included in DevOps. It is a very interesting discussion, I would love to see this elaborated more upon. But I understand that you are limited on words.
### Grammatical errors
* Could be good to put these words in italics or bold for better readability: "cultural resistance, solidified organizational structure, and high costs"
* "This could indicate that changing workflow from DevOps to DevSecOps will be met with reluctance." I think this sentence is a bit redundant because it repeats the same information that you presented in the sentence before.
* In the third paragraph, the sentence "Developers implement unsafe code that security experts have to fix. ~~,which slows down development.~~" I think the crossed out part is redundant as it is explained in the earlier sentence.
* I think in this sentence "Some of the external challenges with implementing DevOps" you mean DevSecOps?
* The sentence "[...] that has yet found a base in the industry[1]." can be rephrased to "[...] that has yet to find a foothold in the industry[1]."
* "Although, adding security tests could also lead to more vulnerabilities being detected early in the process which could save time later on[4]." rephrase to "However, adding security tests could lead to vulnerabilities being detected earlier in the process, which could save time later on[4]."
* I had trouble understanding the later part of the sentence in the last paragraph: "[...] that improving performance with the help of DevOps does not imply that any cornerstones of software development have been cut out". This probably needs to be rephrased to make it clearer.


## Conclusion
A well written, concise and summarizing conclusion to the essay. I like how you came back around to answer the question you asked in the beginning. As I mentioned in the introduction section I think that the question "Is DevSecOps the new DevOps?" should match verbatim with the question asked in the introduction.

### Grammatical errors
* "However, this does not imply the need for a new term such as DevOps." I think it should be DevSecOps?
* Maybe rephrase "It also becomes easier and easier to implement security in DevOps as there are many tools available to automate the security verification." to "It also becomes easier and easier to implement security in DevOps as more and more tools become available to automate the security verification."

Good Job! I hope my feedback helps and good luck with the final submission!
