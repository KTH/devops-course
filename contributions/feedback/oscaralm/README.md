# Feedback proposal on essay #1080
## Member
Oscar Almqvist (oscaralm@kth.se)    
Github: [oscaralmqvist](https://github.com/oscaralm)

## Pull-requests 
Essay proposal pull-request: [#1080](https://github.com/KTH/devops-course/pull/1080)    
Essay submission pull-request: [#1316](https://github.com/KTH/devops-course/pull/1316) 

# Feedback 

In general, this essay was engaging and highly relevant to DevOps. The first chapter contains not only a  well-writtern and gentle introduction to the subject, but also relevant information needed to understand what the essay is about. One thing that I felt could be investigated further was in the last paragraph of this chapter, where you mention the "Five-9s". For instance, what does 99.999% *usability* signify? How common is it for services to uphold this availability criterion, and is it somewhat of a standard? Also, as the topic is about the role of DevOps, it could be interesting to mention it somewhere in the beginning. 

At `Loss of productivity` in the second chapter it was a bit unclear what is meant when having the employees working at night would lead to low productivity; is it because of the service shutting down or because of tired employees? Something you could mention in the same section is that shutting down at night is also not feasible for companies that operate on a global scale as there always are active users. All things considered, this chapter contained concrete examples of consequences, which I appreciated. I was also intrigued by the concept of SLA penalty and its role in system downtime. Interesting!

`3. Use of DevOps to minimize the downtime` shows interesting strategies to minimize both planned and unplanned downtime. Something that would be interesting is a bit more in-depth discussion across the different zero downtime deployment strategies. For example, in which cases would one prefer one over the other? Also, this paragraph could reformatted to a bullet list (or something similar) for each strategy, instead of writing them all "inline". This would improve the readability of this section and give the reader a greater overview, perhaps similar to how each impact was its own paragraph in the second chapter!

`4. Pros & Cons in CI/CD pipeline` displays a satisfying discussion of the advantages and disadvantages of CI/CD. In addition, this ties together with how CI/CD enables lower downtimes. I would have liked if the cons/challenges would have been reasoned with downtime in mind. Also, the first sentence (*"CI/CD being a subset of Continuous Integration [...]"*) should be reworded as it could be interpreted as CI/CD being the subset. The content of  `5. Development Trend` seems a bit out-of-place, especially the second paragraph; what are some examples and use case of IA, ARO, and APM tools? The first paragraph could almost fit in the introduction somewhere, just to prepare the reader about DevOps and its overall aims. Lastly, I enjoyed how the conclusion returned to the topic of downtime and how DevOps affects it!

As most of your sources are from blogposts/less formal articles (which is totally understandable!), I tried to find a study or scientific article that relates to your work and that you could possibly use. *[Comparison of zero downtime based deployment techniques in public cloud infrastructure](https://ieeexplore.ieee.org/abstract/document/9243605)* [1] is one. This contains discussions of how rolling zero downtime deployment strategies (specifically Rolling deployment, Blue-Green Deployment and Canary deployment) all relate to each other, which is certainly relevant to this topic. 

Great work!

## References 
1. Rudrabhatla, C. K. (2020, October). Comparison of zero downtime based deployment techniques in public cloud infrastructure. In 2020 Fourth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud)(I-SMAC) (pp. 1082-1086). IEEE.
