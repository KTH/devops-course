# Overall impression
You have written a good and **relevant** essay for DevOps. The essay has the correct **format**. The **title** is relevant to what the essay is about. You are consistent with your sections and the paper has a nice flow throughout which makes the essay have a **well-structured**. The essay contains **figures** that strengthen the arguments presented in the essay. Throughout the essay, you provide relevant background, examples, and proposals which contributes to the essay having a good **sound**. You use relevant **references** and proper citation. The paper is **elegant** as I can see that you have used LaTeX.

I think you have produced a good essay and I don’t have any critical feedback. I have two suggestions. Firstly, I would suggest is to include an **introduction** before you go into your background. Secondly, you could expand some more on your **conclusion**.

My feedback for the different sections is presented below. Great job with the first draft! :D  

# Feedback for the different sections
## 1.1 Background
The background provides a good explanation of docker containers that makes a uniformed reader well enough informed to understand the rest of the paper. This makes this essay self-contained. I would consider either elaborating or changing figure 1.2. The figure refers to the _client_, _docker_host_ and _registry_. However, you only go into detail regarding what happens in the _docker_host_. Hence I would add a paragraph regarding the _client_ and _registry_ or changing the image. Since you mention the _registry_ in 2.1 I would add a paragraph about it in the background.

## 2.1 Faulty parameter settings
You explain clearly the potential security vulnerability of an image having root access to the host machine. It is good that you are concrete by example with the usage of “-privileged”. You suggest that developers should provide better documentation to inform the end-user of potential risks. I don’t know if it is necessary, but you could maybe try to find an example of poor documentation online that might result in users exposing a security vulnerability and give a suggestion of better documentation.

## 2.2 Malicious container images
Interesting and relevant example with the coin mining example. You provide more than one example of how a user can avoid malicious container images and reflect on the scalability to do a static or dynamic analysis. This illustrates that you think critically. You end this section by mentioning that users should you images from trusted sources, I would suggest to maybe add a few sentences about what users should look for in a trusted source.

## 2.3 Breaches in software dependencies
Great paragraph where you explain the problem and what users should do to avoid it. My only suggestion would be to strengthen your argumentation with a real-life example of what can happen when you don’t patch your dependencies. Alternatively, you could provide some stats or graphs regarding how often leading technology companies patch their dependencies.

## 2.4 Good habits to improve security
I like that you in 2.1-2.3 go into detail about how to prevent specific vulnerability, and then in 2.4 you give general advice of good habits. The habits you recommend in 2.4 are all relevant to the subject. In this draft you have written 1505 words (ignoring the title page, abstract, and references). You could maybe go into further detail about these habits. Additionally, I would suggest you show the full command for when you start an image with limited CPU usage. Use verbatim writing code in Latex:
   docker run -it --cpus=”1.0” image_name

## 3 Conclusion
The conclusion is short but good. In the first paragraph in section 2 you mentioned that you’ve chosen to focus on Docker but that these vulnerabilities might be relevant to other engines. Maybe expand on that?
