Feedback for essay: "5G technology: An investigation in cloud architecture and "Blue/Green" strategy for software upgrades" #1777
---

First of all, thank you for this valuable contribution to DevOps. The essay is highly theoretical and was an wonderful read. With that being said, I do however have a few pointers that might make it an even more exceptional essay.

high-level strengths
---

- The title stays true to its content and conveys an interesting topic
- The essay is well structured with a clear problem statement connected to the background and deals with the problem in a very meticulous way
- The problem statement is expressive and contains enough information to understand its purpose and influence.

high-level weaknesses
---

- The essay has in some segments a lack of background, meaning that it states something as being obvious or without an associative source to its claims. It could be helpful to back the statements with external information or explanations that further discloses the underlying reasoning. 
  - Section IV is an example of where this presence inhere. 
  - A technique I like to use is to refer to other studies by their author(s). i.e "Author A, suggests that Subject A works better for Subject B..."
- The connection between sections could had been more apparent
- The discussion feels a bit ubiquitous as it brings up new points that have no transparent connection to previous mentioned material in the essay. Thus making the discussion hard to follow.

Overall feedback
---

5G is a eminent business area for DevOps. Especially as you wrote that it wants to challenge the cloud infrastructure. I really think this essay conveys a clear message about what 5G technology requires in order to stand a chance against its competition and how it can re-use concepts inherited from cloud architecture. However, I would love to see the essay focus more on the software architecture (Kubernetes for example), as it better relates to DevOps rather than what 5G operators should do to adapt to its competition from a business strategy approach. With that being said, it is also imperative to understand the issue from a business intelligence perspective, which this study has fully illustrated.

The author undoubtedly has a talent of remitting technical knowledge into a more digestible subject matter by disecting the subject into bite-size pieces and problematizing it accordingly.

A question that came to mind during the examination was why the essay didn't make a comparison between Blue/Green strategy and the mentioned active-standby node scheme, as it on a high-level gives the impression to be very similar, as both strategies are using redundant nodes in order to maximize the system uptime reliability.

## 1. Introduction

The introduction is very enticingly written and hooks the reader immediately. It reveals the problems that 5G has to take care of and propose a possible solution that could work for its design. However, I would had appreciated some claims to be backed by previous literature. Such as the claim that its expected that 5G networks are expected to be highly software centric.

It might be obvious for us as DevOps students to understand that virtualization is key for scalability, but how does that look for an infrastructure such as mobile networks? I think the essay could had gathered more debate if this was more clearer.

## 2. Background and related work

This section provides the reader with information about ***the why***. Namely that the mobile network are monoliths, that are dependent of proprietary hardware systems and that it comes with difficult challenges. Howbeit, the content in this section was a bit confusing and didn't add much to the overall essay. I would recommend to weave in the abridged background information into the problem statement section, such that the essay could fill in more information regarding the software side of the problem.

## 3. Problem statement

This section is excellently written and conveys the problem in an intuitively manner. It does also narrow down the problem statement in a natural way by expressing its target points.

## 4. A Comparison between containers and VM for deploying apps in 5G

The message is there, but the execution is somewhat confusing. It would had been helpful if the comparison was in regards to the blue/Green deployment strategy instead of a stark comparison between the two technologies. Also, it would had made more sense to have the database synchronization challenge here instead of having it as its own section as it is heavily dependent on the virtualization strategy.

## 5. Blue-Green deployment strategy

This chapter is very well written. But it could be improved, as the concept is very complex. A informative figure could had been helpful here in order to visualize how everything is connected. But as previously said, the author has made an excellent work of making the complex subject digestable.

The arguments for why Blue/Green deployment is suitable for 5G networks are well put and neatly explained and conveys the overall message that the essay tells.

## 7. Discussion and conclusions

This section brings up a lot of though-proviking debate. Especially around 5G specific operations. It does however not resolve the stated problem directly. It rather expands the proposition with further obstacles, than attempting to solve the already existing ones.

On the other hand, it does answer the question about the implications of what Blue/Green deployment does to new services in a 5G network. Notably enabling faster and reliable continuous deployment of software.

# Pointers to additional material

- [Edge computing - a must for 5G success](https://www.ericsson.com/en/edge-computing)
  
  Edge computing is a new concept that will be heavily enabled by 5G and is a cornerstone of Telecommunications attempt to compete with cloud.
- [5G and edge computing: why does 5G need edge?](https://stlpartners.com/articles/edge-computing/5g-edge-computing/)

  Goes into detail why 5G is dependent on edge computing in order to compete
- [Why 5G Needs Kubernetes](https://containerjournal.com/topics/why-5g-needs-kubernetes/)

  Kubernetes is a popular orchestrator of containers, that can be applicable for 5G applications 
- [Containers and Virtual Machines – Essential to 5G](https://www.hcltech.com/blogs/containers-and-virtual-machines-essential-5g)

  Further material that might explain the differences between containerization and virtualization in the 5G network domain.
- [Containers vs Virtual Machines: Choosing the Right Virtualization Technology for Mobile Edge Cloud](https://ieeexplore.ieee.org/document/8911715)

  An academic study that explains the challenges that comes with containerizing the Mobile Edge Cloud.
- [The impact of 5G on the evolution of intelligent automation and industry digitization (Industry 4.0)](https://link.springer.com/article/10.1007/s12652-020-02521-x)

  A literature review that explores how 5G enables intelligent automation, as well as its key enabling technlogies
- [Flexible Migration in Blue-Green Deployments within a Fixed Cost](https://dl.acm.org/doi/abs/10.1145/3429885.3429963)
  
  This paper discusses the importance that a orchestrator such as kubernetes has towards a blue-green deployment strategy.
