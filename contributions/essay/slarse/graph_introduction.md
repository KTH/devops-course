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

\label{sec:pg}

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

\label{sec:usage}

# Usage examples (same DB, same operation, relational vs graph)
In this section, I present a simple movie database modeled with an RDF graph
database, a property graph database and a standard relational database. The
database should model the following:

* People
* Movies
* Which movies any given person has acted in
    - And which role he or she performed as
* Which movies any given person has directed

Modeling this data represents a few, common tasks databases have to fulfill,
namely representing concrete entities (here, movies and people) and their
attributes (names and titles), as well as relationships between such entities
(acted in and directed by). The rest of this section is laid out in the
following way. TODO: explain rest of layout

Let us start out with the plain SQL database, as
that will probably be the most familiar to readers. 

\label{sec:sql-def}

## SQL database definition
This is the part of this article that assumes some prior knowledge of relational
databases, as concepts such as tables and foreign keys will not be explained in
detail. To model the data Sec. \ref{sec:usage}, a typical SQL database will need
four tables: two tables to represent the base entities _Person_ and _Movie_, as
well as two association tables to model the _ActedIn_ and _DirectedBy_
relationships between these. The reason that the two association tables are
required is that both _ActedIn_ and _DirectedBy_ are many-to-many relationships,
which cannot be expressed in a relational database with only the concrete entity
tables. For example, an actor typically has acted in more than one movie, and
most movies are acted in by more than one actor. As an example, the Person table
could be defined with the following statement:

```sql
CREATE TABLE Person (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL
);
```
The Movie table is almost identical. Then, the ActedIn table could be defined
with the following statement:

```sql
CREATE TABLE ActedIn (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    person_id INT UNSIGNED NOT NULL,
    movie_id INT UNSIGNED NOT NULL,
    played_role VARCHAR(128) NOT NULL,
    FOREIGN KEY(person_id) REFERENCES Person(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(movie_id) REFERENCES Movie(id) ON UPDATE CASCADE ON DELETE CASCADE
);
```

The DirectedBy table is, again, almost identical. The whole database schema is
presented schematically in Fig. \ref{fig:slq-schema}. For the sake of brevity, I
have omitted details such as `UNSIGNED` and `NOT NULL`. Note the multiplicities
on the relations between the tables. For example, each 

\begin{figure}[ht]
    \centering
    \includegraphics[width=\columnwidth]{images/sql_schema.pdf}
    \caption{SQL schema for the movie database}\label{fig:sql-schema}
\end{figure}

With the schema defined, the database can be filled with data using queries that
look something like the following:

```sql
INSERT INTO Movie(title) VALUES
    ('The Town');
INSERT INTO Person(name) VALUES
   ('Ben Affleck');
INSERT INTO ActedIn(person_id, movie_id, played_role) VALUES
    ((SELECT id FROM Person WHERE name='Ben Affleck'), (SELECT id FROM Movie WHERE title='The Town'), 'Doug MacRay');
INSERT INTO DirectedBy(person_id, movie_id) VALUES
    ((SELECT id FROM Person WHERE name='Ben Affleck'), (SELECT id FROM Movie WHERE title='The Town'));
```

Note how the insertions into the association tables have nested SELECT queries
to find the correct primary keys of the related tables. The full definition of
the database, including data insertions, can be found in appendix A. It has been
tested to work with MySQL 5.6.

\label{sec:neo4j-def}

## Property graph database definition
Let us now try to model the data as a property graph instead. I will use Neo4j
and its query language Cypher because it is easy to get started with, and Cypher
is easy to briefly explain. Do however keep in mind that there is no one query
language for property graphs, as described in Sec. \ref{sec:pg}, so this section
is not representative of property graphs as a whole. I do however think that it
illustrates the idea of graph-based queries well.

As Neo4j is a schemaless database system, there is no need to first _define_ the
database, as was the case for the SQL database in Sec. \ref{seq:sql-def}. It is
simply a matter of entering values into the database. Cypher is concise, so
entering the same data about Ben Affleck that was entered in Sec.
\ref{sec:sql-def} is a matter of four statements.

```sql
CREATE (TheTown:Movie {title: "The Town"})
CREATE (Ben:Person {name: "Ben Affleck"})
CREATE (Ben)-[:ACTED_IN {role: "Doug MacRay"}]->(TheTown)
CREATE (TheTown)-[:DIRECTED_BY]->(Ben)
```

The first two `CREATE` statements create Person and Movie nodes, while to two last
create `ACTED_IN` and `DIRECTED_BY` edges (or relations). The syntax for the
`CREATE` statement is rather straightforward. Creating a node is as simple as
`CREATE (<NODE_DEFINITION>)`. Looking specifically at the first statement,
`TheTown:Movie` denotes that the label on this node is `Movie`, and that the
node should be assigned to a variable called `TheTown`. The variable can be
used throughout the query to reference the node. Finally, everything within
curly braces are simply properties on the form `key: value`.

The definition of a relationship is similarly straightforward, and generally
looks like `CREATE (<NODE>)-[<EDGE_DEFINITION>]->[<NODE>]`. The
`<EDGE_DEFINITION>` is written precisely the same as `<NODE_DEFINITION>`,
including property declarations. Looking more closely at the last `CREATE`
statement, it is plain to see how the variables `TheTown` and `Ben` are reused
to denote the nodes which the edge connects. Also note how no variable name is
declared for the edge. There is no need for it, as it is not reused. The full
database declaration can be found in Appendix B.

## Querying the databases
In this section, I present a series of increasingly complex queries. Keep in
mind that these queries play to the strengths of a graph database, and as such
are not meant to show that graph databases are always better than.

\label{sec:query1}

### Query \#1: Find all actors and the roles they have played
For the first query, we want to list all actors and they roles they have played,
as well as in which movies. This is a straightforward three-way join with SQL.

```sql
SELECT Person.name, Movie.title, ActedIn.played_role
FROM Person, Movie, ActedIn
WHERE
  Person.id = ActedIn.person_id AND
  Movie.id = ActedIn.movie_id;
```

With Cypher, it gets slightly simpler, using the `MATCH` statement. A `MATCH`
statement looks much like a `CREATE` statement, but instead of declaring a
structure to create, it declares a structure to search for.

```sql
MATCH (actor:Person)-[acted:ACTED_IN]->(movie:Movie)
RETURN actor.name, movie.title, acted.played_role
```

Note the use of variables to enable accessing specific properties in the return
statement. The results of these queries would be identical, apart from
potentially different ordering of the results.

### Query \#2: Find all self-directed actors
This query is meant to find all actors that have acted in a movie that they have
also directed. For SQL, this results in a slight extension of the three-way
join in Sec. \ref{sec:query1}, making it a four-way join.

```sql
SELECT Person.name, Movie.title, ActedIn.played_role
FROM Person, Movie, ActedIn, DirectedBy
WHERE
  Person.id = ActedIn.person_id AND
  Person.id = DirectedBy.person_id AND
  Movie.id = ActedIn.movie_id AND
  Movie.id = DirectedBy.movie_id;
```

The Cypher query also needs an extension, but it is done in a fairly different
way.

```sql
MATCH (actor:Person)-[acted:ACTED_IN]->(movie:Movie),
      (movie)-[directed:DIRECTED_BY]->(actor)
RETURN actor.name, acted.played_role, movie.title
```

Again, both queries will yield identical results.

### Query \#3: Find all actors somehow related to Ben Affleck
This is the final query, and where it gets very interesting. I found it very
difficult to state the intention of this query entirely in natural language, so
I define this helper function.

```python
def related_actor(actor):
    if actor.visited:
        return False
    if actor.directedByBen or actor.actedWithBen:
        return True
    else:
        for related_actor in actor.actedWith:
            if related_actor(actor)
            


1. Acted beside Ben Affleck
2. Been directed by Ben Affleck
3. 

\label{sec:rdf-def}

## RDF database definition

# Other Types of NoSQL Databases (possibly!)

# Pros and cons

# Discussion

\clearpage

# References
