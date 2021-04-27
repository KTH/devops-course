(Feedback comment available [here](https://github.com/KTH/devops-course/pull/1379#issuecomment-827968781))

WORD COUNT: 1178 words

READING TIME: ~5 minutes

Hello Kun Wu 👋🏼 

I have read through your essay and would like to share some feedback, both positive and constructive, regarding what I've read. I will share my immediate thoughts as I read through the writing section by section. I will then leave you with a short list of recommended changes that I think are most important in my feedback. I hope you find this beneficial in any light.

## Introduction
This set an amazing tone for the start of the essay. In contrary to people who undervalue citations, I think that the abundance of links in the first few statements led to a productive outlook. After checking out and skimming the links I can't say I had a concrete grasp of the topic, but I had a strong intrigue in seeing where it would go from here. It is a skilled writing to capture a reader's attention strongly, and it moves smoothly unto the Murphy's law text block as well. This all paints a clear picture of seeking scale, fault tolerance, and ultimately reliability. The main gripe with this section is how we exit it by looking to compare software architecture models. It would have been more intuitive to place the primary focus on the paper heading of the evolution of such software instead in my opinion. This is especially true given the tight word limit constraints. As a fellow essay writer who had to compare various software offerings, I can say that the easiest way to still generate meaningful content was to be upfront with the reader on what the focus will be, so that they better respond to the upcoming sections rather than expect the non-existent. 

##  The software architecture exploration
### Primaeval distributed systems
Good to include those citations for those interested in this distributed systems genesis. Earlier than I expected it to have started. This section does good in illustrating the challenges for the future architectures to tackle. In hindsight, if you needed to cut down some words to fit some more info elsewhere, this would be the prime place to cut down as the tech is hardly modern.

### Monolithic Application
This starts the fantastic trend of using pictures to relay the explanation of structures as opposed to mainly in text. Indeed the picture is worth 100 words here and does a great job. The text also does a good job of advertising the architecture by first stating the benefits and then moving on to some drawbacks. We can clearly see that scale and reliability is a concern and this makes way nicely for the next section. A concern is that the layered terminology might not be intuitive to all readers, so it doesn't hurt to use some more Layman's terms. 

### Service-Oriented Architecture
As a semi-veteran application developer, I was able to follow these architectures very well thanks to the diagrams again which save words. A big concern here is that there is less text than usual and there is a wonder if a typical MSc student with less application development experience can also benefit completely from this section, this can be solved with some nice citations. One drawback here is that it is not super clear how this benefits over monolith explicitly, as independence is not fully sorted and reliability can still be an issue. It would be good to reiterate the track of improvement as we evolve the techs just to keep the readers on track.

### Microservices
Now this is excellent in terms of focusing on a balance good citations and history information. The main problem here, is a popular one. It is not completely clear what microservices refers to given the idea of fine grained and loosely coupled. It is of course a large topic to tackle, but it would not hurt to encourage the reader on which reference to investigate to fully understand this. I love the UNIX philosophy, it is best to use idioms the reader is probably familiar with just like this. This section did a good job to highlight the power of scale with microservices.

### Cloud native
Exciting start to this section. Especially poetic is the challenge of if we really can do things differently. Here we can finally see some issues mentioned back in the first sections like load balancing and it is great to come back to them and see them satisfied with such an architecture. The biggest strength of this section is also a weakness. It does a good job of highlighting containerizations and clusters as an enabler for the cloud native architecture, but lack of further reading citations for either of these topics means that their merging in this architecture is slightly more difficult to appreciate. This is all of course dependent on the knowledge you expect the reader to have.

### Server less
The section is understandably brief. The main negative here is how you seem to summarize the architecture and sort of 'hype it up', which is excellent, but only to mainly mention where it doesn't help much 'online games'. I think adding a good use case for server less before mentioning where it doesn't help paints it in a better light.

## The conclusion
They say a conclusion is often no more than a reiteration of the introduction. This is mainly targeted towards scientific writing, where the problem statement is formulated at the beginning and reformulated near the end. In your case, you chose to give it a pedagogical view. Indeed, looking through evolution should give us insight into how to always wisely choose the right solution for a given situation. Personally, I think this is great. The only addition I would add to this is to reaffirm the other aspect gained which is the domain knowledge in modern tech such as the Kubernetes microservices and server less APIs in the aforementioned sections. Those sections did lose a bit of the overall gist of specifying the continual improvement in the evolution, so the conclusion could have been their saving grace.

#Suggested changes
- Better focus on evolution history in end of introduction
- Rather than expand on further topics in Cloud native (Service Mesh), maybe elaborate more on the core concept of clustered and distributed decoupled containers. Oftentimes, an example of use case is best for cementing the idea.
- Add a use case to server less to show how it can be useful, if word count is an issue consider replacing the case when it's not useful (online games).
- Give the conclusion its own section header, and add some more concluding statements (the modern tools mentioned like microservices and server less), and how they play into the speculative future.
- Your references are good, but in future consider using a particular citation style (APA, MLA, IEEE). This link-based approach can also work sort of like reading a blog post or an article on Medium. [Here is a source on citation styles](https://pitt.libguides.com/citationhelp) which you can use if you are interested in any of APA, MLA, IEEE. 
Thank you for reading my feedback! 🥣 
