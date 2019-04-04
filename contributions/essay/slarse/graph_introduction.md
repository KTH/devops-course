\pagenumbering{gobble}
\clearpage

\pagenumbering{roman}
\tableofcontents

\clearpage
\pagenumbering{arabic}
# Foreword
This article presents an introduction to graph databases, intended to be read by
those already somewhat familiar with relational databases. Readers are also
expected to have some rudimentary knowledge of graph theory, at least to the
extent that they feel comfortable with the concepts of nodes and edges (both
directed and undirected), as well as basic graph traversal. After having read
this article, readers should be left with a good idea of what graph databases
are, how they compare to relational databases, and when and why one might want
to use one. In terms of formality, this article sits somewhere in between a
scientific paper and an article one would come across on a software engineering
web site. Formalities are readily sacrificed in favor of making for a more
enjoyable read, but facts are not pulled out of thin air; I have made an effort
to back up non-obvious statements with sources.

# Background
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
rather denotes a collection of storage technologies that are not based on
the relational database model. Graph databases is one such technology
[@buerli2012current]. The concept of graph databases has been around since the
1980s, but was more or less forgotten about in the mid 1990s due to the
emergence of other technologies such as XML. It is not until recently that
graph databases have seen a resurgence in popularity, and much due to this fact,
there are a whole lot of different types of graph database models
around. Angles et al. provides a fairly comprehensive but slightly dated
overview of several different models and their origins [@angles2008survey].
As there is such a large amount of different models, I will make no claim that
this article exhaustively covers graph databases. Rather, I will introduce two
models that are common in production use today: RDF-based models and property
graph models [@hartig2014reconciliation;@angles2018g]. The following two
sections outline the principles behind these models.

## Resource Description Framework (RDF) Databases
The _Resource Description Framework_ is a language for expressing metadata for
websites, and is a key part of the WWW Consortium's (W3C) effort to standardize
a Semantic Web that a machine can not only navigate, but also understand
[@rdf;@semanticweb]. Lately, it has also seen use as general purpose data
storage in several products, including
AllegroGraph\footnote{\url{https://franz.com/agraph/allegrograph/}},
GraphDB\footnote{\url{http://graphdb.ontotext.com/}} and
BlazeGraph\footnote{\url{https://www.blazegraph.com/}}. Such databases are
often called RDF triplestores or semantic databases [SOURCE NEEDED]. An RDF
graph is a set of triples of _subject_, _predicate_ and _object_. The subject
is that which we want to say something about, the predicate is what kind of
statement we are making, and the object the value of that statement.  For
example, the triples in Table\ref{tab:rdf-example} is an RDF encoding of the
data "The Mule is a movie", "Clint is a person", "Clint acted in The Mule", and
"The Mule was directed by Clint" .

Table: RDF triples example \label{tab:rdf-example}

| Subject  | Predicate  | Object   |
| ------   | --------   | -----    |
| The Mule | type       | Movie    |
| Clint    | type       | Human    |
| Clint    | actedIn    | The Mule |
| The Mule | directedBy | Clint    |

There is an interesting observation to be made regarding the triples presented
in Table \ref{tab:rdf-example}: it is not immediately apparent that they
constitute a graph, and there are those who consider RDF triple stores not to be
graphs in the traditional sense [@hayes2004bipartite]. However, viewing the set
union of subjects and objects as nodes, and the set of predicates as labeled
edges, it is clear that the triples of Table \ref{tab:rdf-example} induce the
graph in Fig. \ref{fig:rdf-example}. 

\begin{figure}[ht]
    \centering
    \includegraphics[width=.7\columnwidth]{images/rdf-example.pdf}
    \caption{Visualisation of Table \ref{tab:rdf-example}}\label{fig:rdf-example}
\end{figure}

Another interesting observation is that Table \ref{tab:rdf-example} looks
similar to a traditional relational database table, and indeed, there are ways
to implement RDF stores on top of a relational database system
[@bornea2013building].

## Property graphs
Unlike RDF graphs, Property Graphs (PG) are not formally defined
[@hartig2014reconciliation]. The term also seems to be fairly new; the earliest
mention that I can find is from 2010 [@rodriguez2010constructions], while
another contemporary author does not use the term to describe the same concept
[@srinivasa2012data]. There is however a general agreement about what a property
graph is: a graph in which nodes and edges are distinct, labeled entities that
can contain properties in the form of key-value pairs. Note that the edges of a
PG are often referred to as _relationships_, but I will always refer to them as
edges. Slightly adding to the confusion is that the term PG is often used
interchangeably with _Labeled Property Graph_ (LPG)
[@barrasa2017rdfvslpg;@hartig2014reconciliation;@wiki2018graphdatabases]. The L
in LPG simply emphasizes the fact that nodes and edges are labeled, which is
sensible considering the important role that labels play in a PG model. Labels
are used to categorize nodes and edges, and are roughly equivalent to type
assignments [@srinivasa2012data]. For example, a node representing a person
could have the label "Person", which makes it very easy to query for Person
node. Another important difference between RDF graphs and PG is that the latter
has no standardized query language, although it should be noted that efforts are
underway to standardize a Graph Query Language (GQL)
[@gqlstandard;@gqlmanifesto;@w3c2019workshop;@angles2018g]. Examples of current
PG databases are Neo4j\footnote{\url{https://neo4j.com}}, which uses the Cypher
query language\footnote{\url{https://neo4j.com/developer/cypher/}}, and
JanusGraph\footnote{\url{https://janusgraph.org/}}, which uses the Gremlin query
language\footnote{\url{https://docs.janusgraph.org/latest/gremlin.html}}.

# Usage examples (same DB, same operation, relational vs graph)
In this section, I present a simple movie database modeled with an RDF graph
database, a property graph database and a standard relational database.

# Other Types of NoSQL Databases (possibly!)

# Pros and cons

# Discussion

\clearpage

# References
