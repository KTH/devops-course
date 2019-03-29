\pagenumbering{gobble}
\clearpage

\pagenumbering{roman}
\tableofcontents

\clearpage
\pagenumbering{arabic}
# Foreword
This article presents an introduction to graph databases, intended to be read by
those already somewhat familiar with relational databases. After having read
this arcticle, readers should be left with a good idea of what graph databases
are, how they compare to relational databases, and when and why one might want
to use one. In terms of formality, this article sits somewhere in between a
scientific paper and an article one would come across on a software engineering
web site. Formalities are readily sacrificed in favor of making for a more
enjoyable read, but facts are not pulled out of thin air; I have made an effort
to back up non-obvious statements with sources.

# Introduction
It is very often the case that an application needs a persistent data store.
For a long time, the relational database model has been the go-to for most such
data stores [@vicknair2010comparison]. The 1970s saw the inception of the
Standard Query Language (SQL) as well as seminal work on performance
optimizations that paved the way for relational databases in the world outside
of academia [@selinger1979access]. Adoption rose sharply in the 1980s, and since
relational databases have been the de-facto standard [@vicknair2010comparison].
In the past few years, there has been an increase in interest for non-relational
database systems, collectively known as NoSQL [@vicknair2010comparison;TODO:
MORE SOURCES]. It is important to note that NoSQL is not _one_ technology, but
in rather denotes a collection of storage technologies that are not based on
the relational database model. Graph databases is one such technology
[@buerli2012current]. However, even graph databases is not one unified concept,
there are in fact several different types. This is not simply a matter of
implementation details either, as the type of graph database is highly relevant
to what the performance on different tasks.

# The Different Types of Graph Databases

## RDF

## Property-based

# Usage examples (same DB, same operation, relational vs graph)

# Other Types of NoSQL Databases (possibly!)

# Pros and cons

# Discussion
