def main():
    person_tag = lambda fullname: fullname.split()[0]
    movie_tag = lambda title: title.replace(" ", "")

    output = []
    with open("movies", "r") as f:
        for line in f.readlines():
            title = line.strip()
            output.append(f'CREATE ({movie_tag(title)}:Movie {{title: "{title}"}})')

    with open("people", "r") as f:
        for line in f.readlines():
            fullname = line.strip()
            output.append(
                f'CREATE ({person_tag(fullname)}:Person {{name: "{fullname}"}})'
            )

    with open("acted_in", "r") as f:
        for line in f.readlines():
            actor, character, movie = line.strip().split(",")
            output.append(
                f'CREATE ({person_tag(actor)})-[:ACTED_IN {{played: "{character}"}}]->({movie_tag(movie)})'
            )

    with open("directed", "r") as f:
        for line in f.readlines():
            director, movie = line.strip().split(",")
            output.append(
                f"CREATE ({movie_tag(movie)})-[:DIRECTED_BY]->({person_tag(director)})"
            )

    print("\n".join(output))


if __name__ == "__main__":
    main()
