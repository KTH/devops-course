import csv

CREATE_PERSON = """CREATE TABLE Person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);
"""
CREATE_MOVIE = """CREATE TABLE Movie (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL
);
"""
CREATE_DIRECTED = """CREATE TABLE DirectedBy (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL REFERENCES Person(id),
    movie_id INT NOT NULL REFERENCES Movie(id)
);
"""
CREATE_ACTED_IN = """CREATE TABLE ActedIn (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL REFERENCES Person(id),
    movie_id INT NOT NULL REFERENCES Movie(id),
    played_role VARCHAR(128) NOT NULL
);
"""


def main():
    output = [CREATE_PERSON, CREATE_MOVIE, CREATE_DIRECTED, CREATE_ACTED_IN]

    person_id = lambda name: f"SELECT id FROM Person WHERE name='{name}'"
    movie_id = lambda title: f"SELECT id FROM Movie WHERE title='{title}'"

    with open("movies.csv", "r") as f:
        movie_values = ",\n".join([f"    ('{line.strip()}')" for line in f.readlines()])
        output.append(f"INSERT INTO Movie(title) VALUES \n{movie_values};")

    with open("people.csv", "r") as f:
        person_values = ",\n".join([f"   ('{line.strip()}')" for line in f.readlines()])
        output.append(f"INSERT INTO Person(name) VALUES \n{person_values};")

    with open("acted_in.csv", "r") as f:
        acted_in_values = []
        for row in csv.reader(f):
            actor, played_role, movie = row
            acted_in_values.append(
                f"    (({person_id(actor)}), ({movie_id(movie)}), '{played_role}')"
            )

        acted_in_values = ",\n".join(acted_in_values)
        output.append(
            f"INSERT INTO ActedIn(person_id, movie_id, played_role) VALUES \n{acted_in_values};"
        )

    with open("directed.csv", "r") as f:
        directed_by_values = []
        for row in csv.reader(f):
            director, movie = row
            directed_by_values.append(
                f"    (({person_id(director)}), ({movie_id(movie)}))"
            )

        directed_by_values = ",\n".join(directed_by_values)
        output.append(
            f"INSERT INTO DirectedBy(person_id, movie_id) VALUES \n{directed_by_values};"
        )

    print("\n".join(output))


if __name__ == "__main__":
    main()
