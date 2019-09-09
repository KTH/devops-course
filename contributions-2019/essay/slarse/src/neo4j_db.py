import csv

person_tag = lambda fullname: fullname.split()[0].lower()
movie_tag = lambda title: "".join(title.split()).lower()


def movie_formatter(row):
    title = row[0]
    return f'CREATE ({movie_tag(title)}:Movie {{title: "{title}"}})'


def person_formatter(row):
    fullname = row[0]
    return f'CREATE ({person_tag(fullname)}:Person {{name: "{fullname}"}})'


def acted_in_formatter(row):
    actor, played_role, movie = row
    return f'CREATE ({person_tag(actor)})-[:ACTED_IN {{played_role: "{played_role}"}}]->({movie_tag(movie)})'


def directed_by_formatter(row):
    director, movie = row
    return f"CREATE ({movie_tag(movie)})-[:DIRECTED_BY]->({person_tag(director)})"


def convert(filepath, formatter):
    """Convert CSV file to a list of strings by applying the provided formatter
    to each line.
    """
    output = []
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            output.append(formatter(row))
    return output


def main():
    output = (
        convert("movies.csv", movie_formatter)
        + convert("people.csv", person_formatter)
        + convert("acted_in.csv", acted_in_formatter)
        + convert("directed.csv", directed_by_formatter)
    )
    print("\n".join(output))


if __name__ == "__main__":
    main()
