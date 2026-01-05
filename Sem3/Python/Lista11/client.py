import argparse
from ops import LocalRepository, RemoteRepository


def print_movies(movies):
    for m in movies:
        producers = ", ".join(m["producers"])
        print(f"ID: {m['id']} | {m['title']} ({m['year']})")
        print(f"  Director: {m['director']} | Operator: {m['operator']}")
        print(f"  Producers: {producers}")
        print("-" * 30)


def main():
    parser = argparse.ArgumentParser(description="Movie Client")
    parser.add_argument(
        "--api", action="store_true", help="Use API instead of direct DB connection"
    )

    subparsers = parser.add_subparsers(dest="command")

    # List
    parser_list = subparsers.add_parser("list", help="List movies")
    parser_list.add_argument(
        "--search", help="Filter by title or director surname"
    )  # Nowy argument

    # Add
    parser_add = subparsers.add_parser("add", help="Add movie")
    parser_add.add_argument("--title", required=True)
    parser_add.add_argument("--year", type=int, required=True)
    parser_add.add_argument("--director", required=True)
    parser_add.add_argument("--operator", required=True)
    parser_add.add_argument("--producers", help="Comma separated")

    # --- NOWE KOMENDY ---

    # Delete
    parser_del = subparsers.add_parser("delete", help="Delete movie by ID")
    parser_del.add_argument(
        "--id", type=int, required=True, help="ID of the movie to delete"
    )

    # Update
    parser_upd = subparsers.add_parser("update", help="Update movie by ID")
    parser_upd.add_argument(
        "--id", type=int, required=True, help="ID of the movie to update"
    )
    parser_upd.add_argument("--title", help="New title")
    parser_upd.add_argument("--year", type=int, help="New year")
    parser_upd.add_argument("--director", help="New director surname")
    parser_upd.add_argument("--operator", help="New operator surname")
    parser_upd.add_argument("--producers", help="New producers (comma separated)")

    args = parser.parse_args()

    # Wybór źródła danych
    if args.api:
        repo = RemoteRepository()
        print("--- MODE: API ---")
    else:
        repo = LocalRepository()
        print("--- MODE: DIRECT DB ---")

    # Obsługa komend
    if args.command == "list":
        movies = repo.list_movies(search_query=args.search)  # Przekazanie argumentu
        print_movies(movies)

    elif args.command == "add":
        producers_list = args.producers.split(",") if args.producers else []
        repo.add_movie(
            args.title, args.year, args.director, args.operator, producers_list
        )

    elif args.command == "delete":
        repo.delete_movie(args.id)

    elif args.command == "update":
        producers_list = args.producers.split(",") if args.producers else None
        repo.update_movie(
            args.id,
            title=args.title,
            year=args.year,
            director=args.director,
            operator=args.operator,
            producers=producers_list,
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
