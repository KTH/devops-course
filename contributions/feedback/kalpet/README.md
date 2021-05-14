# Feedback on essay 
* Submitted essay [#1355](https://github.com/KTH/devops-course/pull/1355)
* Essay proposal [#1079](https://github.com/KTH/devops-course/pull/1079)
* Feedback proposal [#1087](https://github.com/KTH/devops-course/pull/1087)


## Members:

Name: Kalle Pettersson (kalpet@kth.se)  
GitHub: [kallepettersson](https://github.com/kallepettersson)


# Feedback on "Comparison of DevOps Pipeline Setup in Public Cloud(Azure, AWS, and GCP)"

## General impression 
Overall a very well written and technical report I think you guys can be proud of. You manage to provide a good overview of how setting up pipelines on the three public Cloud platforms can be done. Your use of images help a lot with this since there are a lot of "buzzwords" that need to be thrown around when writing about these things.

---
The structure of you report is also very clear and reasonable.

## 1: Introduction 
Interesting and well written introduction! I really like how you guys motivated your decision to focus on Azure, AWS, and GCP, not only did you cite the source but summarized the reasons which makes it even more convincing.

## 2: Comparison of DevOps Pipeline setup

### 2.1...
When you use acronyms such as "PaaS" and "IaaS" it would be nice if you could use their full names the first time you introduce them. For instance writing "Platform as a service (PaaS)" when introducing Paas.

---
Maybe having sections explaining what PaaS and IaaS means would be nice to have as well. Since they are frequent terms used throughout your essay it's important that the reader understands them.

---
Sections 2.1.1 to 2.1.3 which describe the different ways of setting up the pipelines on the different Cloud platforms are very good. Showing the images that you do makes it a lot easier to grasp what you are writing.

### 2.2...
I like your table which clearly defines what the different types of VM's are. One improvement you could make here is to separate out the information about which type of VM's each Cloud provider offers into new columns. For instance something like this:
| Type of VM        |  Description| GCP           | AZURE  |  AWS  |  
| ------------- |:-------------:| -----:| -----:| -----:|
|General purpose| General-purpose VMs are suitable for normal ... |Provided by GCP| Provided by AZURE| Provided by AWS|
|...|...| ...| ...| ...| 

Or maybe separate this information into another paragraph of text. This would make it easier for the reader to see what the different Cloud providers actually provide.

---

An interesting thing to add while you’re on the subject of geographical reach would be to include information about the market share of these providers. Not completely relevant and necessary considering your topic but as a reader it would be interesting to know. This [link](https://www.parkmycloud.com/blog/aws-vs-azure-vs-google-cloud-market-share/) might be useful.

## 3: Conclusion
The conclusion is well written and connects well to what you brought up in the previous sections.

---
Your final "In conclusion..." sentence, while being 

## General improvements and notes 

### Image referencing
I love your extensive use of images, they work very well in aiding the reader in understanding what you are writing about! I noticed that you don't explicitly reference figure 3 and 4, this is something you could easily fix which would make the text more consistent. You should also consider to create a reference list to all the images you use. 

### Suggested changes to sentences
#### Introduction
I only really found one sentence that I thought could use some changes, which says a lot about the overall quality of the text.
```
... to deliver faster, better, and cheaper. -> ... to deliver said services and products faster, better, and cheaper.
```

### Nitpicky stuff
* Image number 4 has quite a low resolution, maybe upload a new version of it.
* Put the references on a new page
