# Feedback for the essay “Docker containers: from 1979 till today”

## High level strengths and weaknesses of the work

### Strengths
- delightful and engaging to read with straight-to-the point sentences and great explanations
- great step-by-step history
- the essay is easy to follow without prior knowledge in the field of containers

### Weaknesses
- for each section, more concrete references for the mentioned points should be given, i.e. mention the original source of each piece of information
- also always good to not use Wikipedia as reference, but the references which those Wikipedia pages state at the bottom
- the essay doesn’t really contain a reflective and a concluding part
- the essay could include more scientific references, most of the references are from gray literature
- formality: use BibLaTeX for references, i.e.
  - `\printbibliography{}` at the bottom of your main LaTeX source file
  - a file called `bibliography.bib` with content like this, then use something like `\parencite{Example}` to reference that citation:
  
```
@online{Example,
    author = {{IANA}},
    title = {Example Domain},
    urldate = {2022-05-09},
    url = {https://example.com/}
}
```

## Further feedback and suggestions

- Introduction
  - A introduction is included in the essay, although it could be useful to actually name the section “Introduction” since it prepares the reader on what to expect in the section
  - The problem could be stated more clearly in the introduction, and the solution could be more clearly connected to the problem, ex:
  - Problem: There is a lack of deep knowledge concerning containers amongst software developers
  - Solution: Software developers' knowledge regarding containers could deepen by investigating their history and how they became what they are today.
  - In section 1.6 it is mentioned that the LXC is the first iteration of containers that resembles containers of today. It would be helpful for the reader during prior sections, especially 1.4 and 1.5 to get a description where these are put in relation to today's containers, and how the concepts differ.
  - The tense is changed in the middle of that section.
- section on Docker
  - suggestion: mention the concept of the Dockerfile, through which Docker configuration can be put easily into a source code version control system like git, as a Dockerfile has a purely text-based format
  - mention that Docker is not limited to Linux but also runs on Windows and Mac
  - explain the Docker ecosystem in a bit more detail (i.e. more than “management and integration with other software for CI/CD”), especially which specific extra tools other container platforms before Docker did not offer
  - could be interesting to mention microservice architecture as a partial explanation when describing the rise in popularity of containers
- idea: have a final “Conclusion” section in which a short recap is given on which important features were added to container technology over the decades and which features are state-of-the-art nowadays
- try to find some academic literature which, for example, compare different containerization technologies, so that you can map that to your timeline afterwards (see “Related work” below)
  - e.g. search for “containerization software history” and similar terms on Google Scholar
  - even complex citations become very easy with BibLaTeX because you can just paste the respective BibLaTeX definition from Google Scholar or somewhere els

## Related work

- parts from pages 6 and 7 of “The Docker Book”: https://lsi.vc.ehu.eus/pablogn/docencia/manuales/The%20Docker%20Book.pdf
- Bachelor’s thesis on “Software containerization with Docker”: https://www.theseus.fi/bitstream/handle/10024/123246/DockerThesis.pdf
