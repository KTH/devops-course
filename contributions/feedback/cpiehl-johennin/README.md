## Feedback for Essay: The inner workings of Git #1092

### Members
Name: Carl Piehl

Mail: cpiehl@kth.se

Github: [cpiehl1](https://github.com/cpiehl1)

Name: Johan Henning

Mail: johennin@kth.se

Github: [johennin](https://github.com/johenninn)

## Links to relevant PRs
The inner workings of Git [#1092](https://github.com/KTH/devops-course/pull/1092)

The inner workings of Git essay submission [#1303](https://github.com/KTH/devops-course/pull/1303)

Original Feedback proposal for the essay [#1095](https://github.com/KTH/devops-course/pull/1095)

## Feedback for Essay
### Overall comment 
Our overall opinion is that the essay is of very high quality. The topic is highly relevant, but often overlooked, making this essay a very useful read for anyone taking this course. We found a lot of new and interesting information in the essay. Describing such a complicated subject in 2000-words is no easy task but we believe that you have succeeded. We are especially impressed with how the different intricacies are explained in a very pedagogical manner. 2000 words exactly from the word count command, [impressive, very nice](https://i.pinimg.com/originals/73/f5/eb/73f5eb6af54f9c46e48966cf5c3ae243.gif).

Below are more detailed comments organised by grading criteria. 

### Title
Very good title, short and precise while still capturing the essence of the essay.

### Introduction 
It’s nice to get a general but brief overview of the contents of the essay.

It would perhaps be useful to have a small motivation in the introduction. You could, for instance, describe the relevance of git to the DevOps topic, maybe even mention [GitOps](https://www.gitops.tech/) briefly.  Additionally, you could argue why knowing the inner workings is useful for your prospective readers. 

### Well-structured
The essay has a good flow, with concepts being introduced in a natural order, making it quite easy for the reader to follow. For instance, the data-model section ends with defining the objects. Then, in the following object-model section, we see how git handles these objects. We also like the early mention of the DAG structure, since it is referenced to regularly in the following sections. 

The section about branching should maybe be a subsection instead of a subsubsection, since the overview in the introduction says “...describing its data-, object- and branching model” and you have subsections for the data-model and the object-model. On this note, we do not really understand why “Branches” is a subsubsection while “Git tags and remote references” is a subsection. The topic of branches seems much more important. This could also serve to improve the structure in the branches section, since you could have subsubsections about merging and detached heads. Currently these things are explained in the same paragraph which is a bit confusing. It might be enough to just split them into separate paragraphs. 

### Conclusion
The conclusion was short, but in a good way. It tied up the essay by mentioning key aspects from each section and also summarises the ideas mentioned in the discussion section.

### Self-contained
Since the targeted audience is master students in CS, everyone should be familiar with the basic functionality of git. With this in mind, we believe that the essay is almost entirely self-contained, with a couple very small exceptions mentioned below.

There are a couple terms that we feel require more explanation or should be excluded. One of these is the term “atomic object model” in the introduction. The word “atomic” is never explained so we believe that it should be expanded on or removed. The other term is the staging command, which is a central part of section 3.2, but is never explained. We believe that it should at least get a brief explanation.

### Innovative
Git is not a new concept both in this course and in general for DevOps. However, the report has an interesting, often overlooked, take on the subject and will most likely add new knowledge to the intended audience reader.

### Figures and Listings
On the one hand, the figures and listings are well made and help deliver the message in the essay. On the other hand the figure 2 seems redundant (and low resolution compared to figure 1) because the graph properties have already been visualized in figure 1 and the commit data structure has already been described several times and visualized in the first pseudo code. It might be a good idea to add listings for the pseudo code as well, making them easier to refer to (so we do not have to write “the first pseudo code”).

### Sound
The essay had the right scientific tone throughout the entire read. To our knowledge the content itself was perfect, in the sense that it is all factually correct.

### References
The referencing was done in a nice and consistent way. There were a total of 14 references which is above the minimum criteria and they all seemed like relevant, high quality references.

### Elegant
It is written in LaTeX which makes it nice looking by default. The authors have taken their time to customize the options in LaTeX to not make the essay look like the default template of overleaf/LaTeX.

The bullet list in section 3.2 is not so visually appealing and not very readable. 
Also, the sentence right above the list “..listed below with the argued violations by Rosso and Diago below” is not very elegant. An idea would be to change this into a table with the following headers: “Principle”, “Explanation”, “Violation”.

### Relevant
Highly relevant topic for DevOps.

### Additional comments 
The language is very good, and the essay seems proof-read. There are some grammatical errors that can be fixed for a better read, but they are quite rare. The sentence breaking errors have already been mentioned in other sections of the feedback.

We have addressed quite a few ways of changing parts of the essay, and we understand that it might be difficult to implement these changes due to the strict word count. One suggestion is to shorten section 3.2 a bit. The ideas mentioned there could probably be summarised in shorter fashion. This could open up for a more thorough coverage on the benefits of git, which should maybe be a subsection. This is another opportunity to bring up [GitOps](https://www.gitops.tech/), which we also mentioned under introduction. You already write about the importance of revision in git, you could further strengthen this argument with the mention of GitOps, since this is a central part of GitOps. 

In section 2.2.3 Branches you mentioned “personal user memory” which took both of us a second read to realise you meant “human memory”. So perhaps change this so it becomes more obvious for the reader.
