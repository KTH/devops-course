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
database systems, collectively known as NoSQL [@vicknair2010comparison].
It is important to note that NoSQL is not _one_ technology, but
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
this article exhaustively covers graph databases. Rather, I will introduce the
_property graph_ database, and show by practical example how such using such a
database compares to the use of a traditional SQL database. For completeness, I
will also present the concepts of a different kind of graph database based
on the RDF-standard, as such databases frequently appeared during my background
research of the subject [@hartig2014reconciliation;@angles2018g]. The rest of
the article is structured as follows. [Section @sec:rdf] presents the concepts
behind RDF databases, while and [Sec. @sec:pg] does the same for property graph
databases. [Section @sec:usage] compares creation and subsequent querying
of a movie database using the relational PostgreSQL system, and the property
graph Neo4j system. Finally, [Section @sec:discussion] presents a discussion of
the potential pros and cons of using a graph database over a relational
database.

## Resource Description Framework (RDF) Databases {#sec:rdf}
The _Resource Description Framework_ is a language for expressing metadata for
websites, and is a key part of the WWW Consortium's (W3C) effort to standardize
a Semantic Web that a machine can not only navigate, but also understand
[@rdf;@semanticweb]. Lately, it has also seen use as general purpose data
storage in several products, including
AllegroGraph^[https://franz.com/agraph/allegrograph/](https://franz.com/agraph/allegrograph/),
GraphDB^[http://graphdb.ontotext.com/](http://graphdb.ontotext.com/) and
BlazeGraph^[https://www.blazegraph.com/](https://www.blazegraph.com/).
An RDF graph is a set of triples of _subject_, _predicate_ and _object_. The
subject is that which we want to say something about, the predicate is what
kind of statement we are making, and the object the value of that statement.
For example, the triples in [Table @tbl:rdf-example] is an RDF encoding of the
data "The Town is a movie", "Ben is a person", "Ben acted in The Town", and
"The Town was directed by Ben" .

Table: RDF triples example. {#tbl:rdf-example}

| Subject  | Predicate  | Object   |
| ------   | --------   | -----    |
| The Town | type       | Movie    |
| Ben      | type       | Person   |
| Ben      | actedIn    | The Town |
| The Town | directedBy | Ben      |

There is an interesting observation to be made regarding the triples presented
in [Table @tbl:rdf-example]: it is not immediately apparent that they
constitute a graph. In fact, it is possible to have for example the object of
one triple be the predicate of another, so the triples do not by themselves 
represent a graph in the traditional sense [@hayes2004bipartite]. In the
case of [Table @tbl:rdf-example] however, viewing the set union of subjects
and objects as nodes, and the set of predicates as labeled edges, it is clear
that the triples of [Table @tbl:rdf-example] induce the graph in [Fig. @fig:rdf-example].

![Visualisation of [Table @tbl:rdf-example]](images/rdf-example.png){#fig:rdf-example width=60%}

Another interesting observation is that [Table @tbl:rdf-example] looks
similar to a traditional relational database table, and indeed, there are ways
to implement RDF stores on top of a relational database system
[@bornea2013building].


## Property graphs {#sec:pg}
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
node. [Figure @fig:pg] shows a PG graph example of the same data as was
presented in [Fig. @fig:rdf-example]. Another important difference between
RDF graphs and PG is that the latter has no standardized query language,
although it should be noted that efforts are underway to standardize a Graph
Query Language (GQL) [@gqlstandard;@gqlmanifesto;@w3c2019workshop;@angles2018g].
Examples of current PG databases are Neo4j^[https://neo4j.com](https://neo4j.com),
which uses the Cypher query
language^[https://neo4j.com/developer/cypher/](https://neo4j.com/developer/cypher/)
(open-sourced as openCypher^[http://www.opencypher.org/](http://www.opencypher.org/)), and
JanusGraph^[https://janusgraph.org/](https://janusgraph.org/), which uses the Gremlin query
language^[https://docs.janusgraph.org/latest/gremlin.html](https://docs.janusgraph.org/latest/gremlin.html).

![Visualisation of a property graph. Labels are in bold and properties are written `key: value`](images/pg.png){width=60% #fig:pg}

# Usage examples (same DB, same operation, relational vs graph) {#sec:usage}
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

## SQL database definition {#sec:sql-def}
This is the part of this article that assumes some prior knowledge of relational
databases, as concepts such as tables and foreign keys will not be explained in
detail. To model the data [Sec. @sec:usage], a typical SQL database will need
four tables: two tables to represent the base entities _Person_ and _Movie_, as
well as two association tables to model the _ActedIn_ and _DirectedBy_
relationships between these. The reason that the two association tables are
required is that both _ActedIn_ and _DirectedBy_ are many-to-many relationships,
which cannot be expressed in a relational database with only the concrete entity
tables. For example, an actor typically has acted in more than one movie, and
most movies are acted in by more than one actor. As an example, the Person table
could be created as shown in [Listing @lst:create-person-table], with the Movie
table being almost identical. The ActedIn table could then be defined as shown in
[Listing @lst:create-actedin-table], with the DirectedBy table being almost
identical to that.

```{#lst:create-person-table .sql caption="DDL for the Person table"}
CREATE TABLE Person (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL
);
```

```{#lst:create-actedin-table .sql caption="DDL for the ActedIn association table"}
CREATE TABLE ActedIn (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    person_id INT UNSIGNED NOT NULL,
    movie_id INT UNSIGNED NOT NULL,
    played_role VARCHAR(128) NOT NULL,
    FOREIGN KEY(person_id) REFERENCES Person(id),
    FOREIGN KEY(movie_id) REFERENCES Movie(id)
);
```

The whole database schema is
presented schematically in [Fig. @fig:sql-schema]. Note the multiplicities on
the relations between the tables. For example, each `ActedIn` row is associated
with precisely one `Person` row, while each `Person` row is associated with zero
(because not every person is an actor) or more `ActedIn` rows.

![SQL schema for the movie database](images/sql-schema.png){width=90% #fig:sql-schema}

With the schema defined, the database can be filled with data using queries
like those shown in [Listing @lst:insert-sql]. Note how the insertions into
the association tables have nested SELECT queries to find the correct primary
keys of the related tables. The full definition of the database, including data
insertions, can be found in [Sec. @sec:appendix-a]. It has been tested to work
with PostreSQL 9.6.

```{#lst:insert-sql .sql caption="Sample of value insertions into the SQL database"}
INSERT INTO Movie(title) VALUES
    ('The Town');
INSERT INTO Person(name) VALUES
   ('Ben Affleck');
INSERT INTO ActedIn(person_id, movie_id, played_role) VALUES
    ((SELECT id FROM Person WHERE name='Ben Affleck'),
     (SELECT id FROM Movie WHERE title='The Town'),
     'Doug MacRay');
INSERT INTO DirectedBy(person_id, movie_id) VALUES
    ((SELECT id FROM Person WHERE name='Ben Affleck'),
     (SELECT id FROM Movie WHERE title='The Town'));
```

## Property graph database definition {#sec:neo4j-def}

![Graph visualisation of the example database. Orange nodes represent people, and blue nodes represent movies.](images/neo4j-db.png){width=60% #fig:neo4j-visualisation}


Let us now try to model the data as a property graph instead. I will use Neo4j
and its query language Cypher because it is easy to get started with, and Cypher
is easy to briefly explain. Do however keep in mind that there is no one query
language for property graphs, as described in [Sec. @sec:pg], so this section
is not representative of property graphs as a whole. I do however think that it
illustrates the idea of graph-based queries well.

As Neo4j is a schemaless database system, there is no need to first _define_ the
database, as was the case for the SQL database in [Sec. @sec:sql-def]. It is
simply a matter of entering values into the database. Cypher is concise, so
entering the same data about Ben Affleck that was entered in [Sec. @sec:sql-def]
is a matter of the four statements shown in [Listing @lst:create-neo4j-values].

```{#lst:create-neo4j-values .sql caption="Sample CREATE statements for the Neo4j database"}
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
curly braces are simply properties on the form `key: value`. Neo4j has an
excellent visualisation tool built-in to its web interface, and the
visualisation of this particular database can be found in
[Fig.  @fig:neo4j-visualisation]. The definition of a relationship is similarly
straightforward, and generally looks like `CREATE
(<NODE>)-[<EDGE_DEFINITION>]->[<NODE>]`. The `<EDGE_DEFINITION>` is written
precisely the same as `<NODE_DEFINITION>`, including property declarations.
Looking more closely at the last `CREATE` statement, it is plain to see how the
variables `TheTown` and `Ben` are reused to denote the nodes which the edge
connects. Also note how no variable name is declared for the edge. There is no
need for it, as it is not reused. The full database declaration can be found in
[Sec. @sec:appendix-b].

## Querying the databases
In this section, I present a series of increasingly complex queries. Keep in
mind that these queries play to the strengths of a graph database, and as such
are not meant to show that graph databases are always better than.

### Query \#1: Find all actors and the roles they have played {#sec:query1}
For the first query, we want to list all actors and they roles they have played,
as well as in which movies. This is a straightforward three-way join with SQL,
as shown in [Listing @lst:sql-query-1].

```{#lst:sql-query-1 .sql caption="SQL query #1"}
SELECT Person.name, Movie.title, ActedIn.played_role
FROM Person, Movie, ActedIn
WHERE
  Person.id = ActedIn.person_id AND
  Movie.id = ActedIn.movie_id;
```

With Cypher, it gets slightly simpler, using the `MATCH` statement shown
in [Listing @lst:cypher-query-1]. A `MATCH` statement looks much like a `CREATE`
statement, but instead of declaring a structure to create, it declares a
structure to search for. Note the use of variables to enable accessing specific properties in the return
statement. The results of these queries would be identical, apart from
potentially different ordering of the results.

```{#lst:cypher-query-1 .sql caption="Cypher query #1"}
MATCH (actor:Person)-[acted:ACTED_IN]->(movie:Movie)
RETURN actor.name, movie.title, acted.played_role
```

### Query \#2: Find all self-directed actors
This query is meant to find all actors that have acted in a movie that they have
also directed. For SQL, this results in a slight extension of the three-way
join in [Sec. @sec:query1], making it the four-way join shown in
[Listing @lst:sql-query-2].

```{#lst:sql-query-2 .sql caption="SQL query #2"}
SELECT Person.name, Movie.title, ActedIn.played_role
FROM Person, Movie, ActedIn, DirectedBy
WHERE
  Person.id = ActedIn.person_id AND
  Person.id = DirectedBy.person_id AND
  Movie.id = ActedIn.movie_id AND
  Movie.id = DirectedBy.movie_id;
```

The Cypher query also needs an extension, but it is done in a fairly different
way by simply adding another structure to match against, as shown in
[Listing @lst:cypher-query-2].

```{#lst:cypher-query-2 .sql caption="Cypher query #2"}
MATCH (actor:Person)-[acted:ACTED_IN]->(movie:Movie),
      (movie)-[directed:DIRECTED_BY]->(actor)
RETURN actor.name, acted.played_role, movie.title
```

Again, both queries will yield identical results.

### Query \#3: Rumors about Ben
This is the final query, which is meant to clearly demonstrate the benefit of
reasoning about data as a graph. The idea is to find any actor that may have
heard a rumor about what it is like acting together with Ben Affleck. This
includes any actor A who has acted in the same movie as Ben, or any actor B
who has acted with actor A, or any actor C who has acted with actor B, and so
on. The astute reader may have noticed that this is a slightly more complicated
version of traversing a social graph to find a person's friends, friends of
friends, and so on^[This is closely related to the transitive closure
of a binary relation R on some set S. Wikipedia has a nice page on the subject:
[https://en.wikipedia.org/wiki/Transitive_closure](https://en.wikipedia.org/wiki/Transitive_closure)].
The problem can however
be somewhat simplified if by considering the `DIRECTED_BY` and `ACTED_IN` edges
visualised in [Fig. @fig:neo4j-visualisation] as bi-directional. Then, it is
simply a matter of finding every actor that can be reached from Ben's node by
traversing `ACTED_IN` edges. While it does not make much sense for a movie to
have acted in an actor, it makes the problem easier to visualise. It is
important not to get stuck on trying to understand the query, the point of
showing it is mostly to exemplify that it is complicated. To solve such a
problem in SQL, we need to issue a so called _hierarchical
query_^[Again, Wikipedia has a nice page on the subject:
[https://en.wikipedia.org/wiki/Hierarchical_and_recursive_queries_in_SQL](https://en.wikipedia.org/wiki/Hierarchical_and_recursive_queries_in_SQL)],
shown in [Listing @lst:sql-query-3].

```{#lst:sql-query-3 .sql caption="SQL query #3"}
WITH RECURSIVE acted_in(person_id, movie_id) AS (
  /* Initial start query */
  SELECT person_id, movie_id
  FROM ActedIn, Person
  WHERE Person.id = ActedIn.person_id AND 
        Person.name = 'Ben Affleck'
UNION
  /* The recursive query */
  SELECT ActedIn.person_id, ActedIn.movie_id
  FROM acted_in, ActedIn
  WHERE acted_in.movie_id = ActedIn.movie_id OR
        acted_in.person_id = ActedIn.person_id
)
/* selecting from the result */
SELECT DISTINCT Person.name
FROM acted_in, Person
WHERE acted_in.person_id = Person.id
AND Person.name != 'Ben Affleck'
```

I will only briefly explain what is actually happening in the query. On the
first line, the `acted_in` pseudo-entity is defined. Then, an initial "start"
query is issued to find all of Ben's `(person_id, movie_id)` tuples. What
happens next is fairly unintuitive. The results of the "recursive" query is
unioned with the initial query, the result of which is then unioned with the
recursive query again, and again, until the result set is no longer expanding.
It is essentially a breadth first search over the `ActedIn` relations, where
the movies are discarded in the final result. The Cypher equivalent of this SQL
query shown in [Listing @lst:cypher-query-3] is a good example of why
representing data as graphs can be advantageous.

```{#lst:cypher-query-3 .sql caption="Cypher query #3"}
MATCH (Ben:Person {name: "Ben Affleck"}),
      (Ben)-[:ACTED_IN*]-(movie:Movie),
      (actor:Person)-[:ACTED_IN]->(movie)
RETURN actor
```

Fetching the Ben Affleck node and storing it in the `Ben` variable is not
strictly necessary, and could be done inline on the second line, but I found
this more readable. [Listing @lst:cypher-query-3] can be broken down as
follows.

1. `MATCH (Ben:Person {name: "Ben affleck"})`
   - Find the Ben Affleck node and store it in `Ben`
2. `(Ben)-[:ACTED_IN*]-(movie:Movie)`
   - Find all `Movie` nodes reachable by traversing any amount of `ACTED_IN`
     edges, starting from `Ben`
   - Note the `*` for "any amount"
   - Note the lack of an arrowhead on the edge, which instructs Neo4j to consider
     all edges bi-directional
3. `(actor:Person)-[:ACTED_IN]->(movie)`
   - Find every actor who acted in any of the found `movie` nodes
4. `RETURN actor`
   - Return every actor that matched the constraints

# Discussion {#sec:discussion}
PG databases show some clear advantages over traditional relational databases.
The queries in Cypher are shorter throughout, yet remain readable. The final
query exemplified how a non-trivial but still realistic search query required
use of advanced SQL constructs, with quite a lot of boilerplate, while the
Cypher equivalent only made use of some of the most rudimentary features of the
language and remained concise. While shorter is not always better, shorter _and_
more readable surely has to count as better from a maintainability point of
view. Another stark contrast between SQL and Cypher is the former's reliance on
a pre-defined schema, and the latter's lack of such. A schemaless approach is a
great boon to quick iteration development practices, as many minor alterations
to the abstract schema of a schemaless database may not require any production
database maintenance. On the other hand, _any_ alteration in a SQL schema
requires a database migration in production environments, which from personal
experience can be a hassle even for relatively simple databases.

There are some major caveats to these comparisons, however. First, I
specifically modeled the database and queries to play to the strengths of a
graph representation. In other words, these are by no means general conclusions
about graph databases being superior to relational databases, but rather that
they can be given the right circumstances. Furthermore, Cypher is not _the_
graph database language, so results are not even generalizable over graph
database query languages as a whole. Time will tell if GQL ends up becoming a
widely adopted standard, but as it stands, there is nothing resembling a
standard for property graph databases. Adopting a database such as Neo4j may
therefore lead to more lock-in than risk averse managers may be willing to
accept.

\clearpage

# References

<div id="refs"></div>

\clearpage

# Appendix

## Appendix A {#sec:appendix-a}

```sql
CREATE TABLE Person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE Movie (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL
);

CREATE TABLE DirectedBy (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL REFERENCES Person(id),
    movie_id INT NOT NULL REFERENCES Movie(id)
);

CREATE TABLE ActedIn (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL REFERENCES Person(id),
    movie_id INT NOT NULL REFERENCES Movie(id),
    played_role VARCHAR(128) NOT NULL
);

INSERT INTO Movie(title) VALUES 
    ('The Avengers'),
    ('The Town'),
    ('Justice League'),
    ('The Prestige'),
    ('The Dark Knight');

INSERT INTO Person(name) VALUES 
   ('Amy Adams'),
   ('Ben Affleck'),
   ('Chris Hemsworth'),
   ('Scarlett Johansson'),
   ('Rebecca Hall'),
   ('Christian Bale'),
   ('Christopher Nolan'),
   ('Zack Snyder'),
   ('Joss Whedon');

INSERT INTO ActedIn(person_id, movie_id, played_role) VALUES 
    ((SELECT id FROM Person WHERE name='Amy Adams'),
     (SELECT id FROM Movie WHERE title='Justice League'),
     'Lois Lane'),
    ((SELECT id FROM Person WHERE name='Ben Affleck'),
     (SELECT id FROM Movie WHERE title='The Town'),
     'Doug MacRay'),
    ((SELECT id FROM Person WHERE name='Ben Affleck'),
     (SELECT id FROM Movie WHERE title='Justice League'),
     'Batman'),
    ((SELECT id FROM Person WHERE name='Chris Hemsworth'),
     (SELECT id FROM Movie WHERE title='The Avengers'),
     'Thor'),
    ((SELECT id FROM Person WHERE name='Christian Bale'),
     (SELECT id FROM Movie WHERE title='The Prestige'),
     'Alfred Borden'),
    ((SELECT id FROM Person WHERE name='Christian Bale'),
     (SELECT id FROM Movie WHERE title='The Dark Knight'),
     'Batman'),
    ((SELECT id FROM Person WHERE name='Rebecca Hall'),
     (SELECT id FROM Movie WHERE title='The Prestige'),
     'Sarah'),
    ((SELECT id FROM Person WHERE name='Rebecca Hall'),
     (SELECT id FROM Movie WHERE title='The Town'),
     'Claire Keesey'),
    ((SELECT id FROM Person WHERE name='Scarlett Johansson'),
     (SELECT id FROM Movie WHERE title='The Avengers'),
     'Black Widow');

INSERT INTO DirectedBy(person_id, movie_id) VALUES 
    ((SELECT id FROM Person WHERE name='Ben Affleck'),
     (SELECT id FROM Movie WHERE title='The Town')),
    ((SELECT id FROM Person WHERE name='Christopher Nolan'),
     (SELECT id FROM Movie WHERE title='The Prestige')),
    ((SELECT id FROM Person WHERE name='Christopher Nolan'),
     (SELECT id FROM Movie WHERE title='The Dark Knight')),
    ((SELECT id FROM Person WHERE name='Zack Snyder'),
     (SELECT id FROM Movie WHERE title='Justice League')),
    ((SELECT id FROM Person WHERE name='Joss Whedon'),
     (SELECT id FROM Movie WHERE title='The Avengers'));
```

## Appendix B {#sec:appendix-b}

```sql
CREATE (TheAvengers:Movie {title: "The Avengers"})
CREATE (TheTown:Movie {title: "The Town"})
CREATE (JusticeLeague:Movie {title: "Justice League"})
CREATE (ThePrestige:Movie {title: "The Prestige"})
CREATE (TheDarkKnight:Movie {title: "The Dark Knight"})
CREATE (Amy:Person {name: "Amy Adams"})
CREATE (Ben:Person {name: "Ben Affleck"})
CREATE (Chris:Person {name: "Chris Hemsworth"})
CREATE (Scarlett:Person {name: "Scarlett Johansson"})
CREATE (Rebecca:Person {name: "Rebecca Hall"})
CREATE (Christian:Person {name: "Christian Bale"})
CREATE (Christopher:Person {name: "Christopher Nolan"})
CREATE (Zack:Person {name: "Zack Snyder"})
CREATE (Joss:Person {name: "Joss Whedon"})
CREATE (Amy)-[:ACTED_IN {played_role: "Lois Lane"}]->(JusticeLeague)
CREATE (Ben)-[:ACTED_IN {played_role: "Doug MacRay"}]->(TheTown)
CREATE (Ben)-[:ACTED_IN {played_role: "Batman"}]->(JusticeLeague)
CREATE (Chris)-[:ACTED_IN {played_role: "Thor"}]->(TheAvengers)
CREATE (Christian)-[:ACTED_IN {played_role: "Alfred Borden"}]->(ThePrestige)
CREATE (Christian)-[:ACTED_IN {played_role: "Batman"}]->(TheDarkKnight)
CREATE (Rebecca)-[:ACTED_IN {played_role: "Sarah"}]->(ThePrestige)
CREATE (Rebecca)-[:ACTED_IN {played_role: "Claire Keesey"}]->(TheTown)
CREATE (Scarlett)-[:ACTED_IN {played_role: "Black Widow"}]->(TheAvengers)
CREATE (TheTown)-[:DIRECTED_BY]->(Ben)
CREATE (ThePrestige)-[:DIRECTED_BY]->(Christopher)
CREATE (TheDarkKnight)-[:DIRECTED_BY]->(Christopher)
CREATE (JusticeLeague)-[:DIRECTED_BY]->(Zack)
CREATE (TheAvengers)-[:DIRECTED_BY]->(Joss)
```
