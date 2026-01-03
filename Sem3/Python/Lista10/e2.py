from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.orm import validates
from sqlalchemy import create_engine, or_, cast
from sqlalchemy.orm import sessionmaker, Session
from typing import List
import json
import os
import argparse
from sqlalchemy import select


class Base(DeclarativeBase):
    pass


# Tablica asocjacyjna Producenci - Filmy
production = Table(
    "producer_film",
    Base.metadata,
    Column("film_id", ForeignKey("Films.id")),
    Column("producer_id", ForeignKey("Producers.id")),
)


class Film(Base):
    __tablename__ = "Films"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    year = mapped_column(Integer)
    ##Zwiazek z reżyreserem (One-to-Many)
    director_id = mapped_column(Integer, ForeignKey("Directors.id"))
    director = relationship("Director", back_populates="directed")
    ##Zwiazek z producentem(Many-to-Many)
    producers: Mapped[List[Producer]] = relationship(
        secondary=production, back_populates="produced"
    )
    ##Zwiazek z operatorem (One-to-Many)
    operator_id = mapped_column(Integer, ForeignKey("Operators.id"))
    operator = relationship("Operator", back_populates="operated")


class Director(Base):
    __tablename__ = "Directors"
    id = mapped_column(Integer, primary_key=True)
    surname = mapped_column(String)
    directed: Mapped[List[Film]] = relationship("Film", back_populates="director")

    @validates("surname")
    def validate_surname(self, key, surname):
        if len(surname) < 3:
            raise ValueError("Surname is too short")
        return surname


class Producer(Base):
    __tablename__ = "Producers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    produced: Mapped[List[Film]] = relationship(
        secondary=production, back_populates="producers"
    )

    @validates("name")
    def validate_name(self, key, name):
        if len(name) < 2:
            raise ValueError("Name is too short")
        return name


class Operator(Base):
    __tablename__ = "Operators"
    id = mapped_column(Integer, primary_key=True)
    surname = mapped_column(String)
    operated: Mapped[List[Film]] = relationship("Film", back_populates="operator")

    @validates("surname")
    def validate_surname(self, key, surname):
        if len(surname) < 3:
            raise ValueError("Surname is too short")
        return surname


# Database setup
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "films.db")
engine = create_engine(f"sqlite:///{db_path}")
SessionLocal = sessionmaker(bind=engine)


def get_or_create(session: Session, model, **kwargs):
    instance = session.execute(select(model).filter_by(**kwargs)).scalar_one_or_none()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.flush()
        return instance


def load_initial_data(session: Session):
    """Loads data from data.json if database is empty."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "data.json")

    if os.path.exists(data_path):
        print(f"Loading initial data from {data_path}...")
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            # Get or create related people
            director = get_or_create(session, Director, surname=item["director"])
            operator = get_or_create(session, Operator, surname=item["operator"])

            producers = []
            for prod_name in item["producers"]:
                producer = get_or_create(session, Producer, name=prod_name)
                producers.append(producer)

            year_val = int(item["year"]) if "year" in item and item["year"] else None

            film = Film(
                title=item["title"],
                year=year_val,
                director=director,
                operator=operator,
                producers=producers,
            )
            session.add(film)

        session.commit()
        print("Data loaded successfully.")
    else:
        print("data.json not found, skipping initial data load.")


def add_movie(args):
    session = SessionLocal()
    try:
        director = get_or_create(session, Director, surname=args.director)
        operator = get_or_create(session, Operator, surname=args.operator)

        producers = []
        if args.producers:
            for prod_name in args.producers.split(","):
                producer = get_or_create(session, Producer, name=prod_name.strip())
                producers.append(producer)

        film = Film(
            title=args.title,
            year=args.year,
            director=director,
            operator=operator,
            producers=producers,
        )
        session.add(film)
        session.commit()
        print(f"Movie '{film.title}' added successfully.")
    except Exception as e:
        print(f"Error adding movie: {e}")
        session.rollback()
    finally:
        session.close()


def list_movies(args):
    session = SessionLocal()
    query = session.query(Film)

    if args.search:
        term = f"%{args.search}%"
        query = (
            query.outerjoin(Director)
            .outerjoin(Operator)
            .outerjoin(Film.producers)
            .filter(
                or_(
                    Film.title.ilike(term),
                    cast(Film.year, String).ilike(term),
                    Director.surname.ilike(term),
                    Operator.surname.ilike(term),
                    Producer.name.ilike(term),
                )
            )
            .distinct()
        )

    movies = query.all()
    for movie in movies:
        producers_names = ", ".join([p.name for p in movie.producers])
        year_str = f" ({movie.year})" if movie.year else ""
        print(f"ID: {movie.id} | Title: {movie.title}{year_str}")
        print(f"  Director: {movie.director.surname}")
        print(f"  Operator: {movie.operator.surname}")
        print(f"  Producers: {producers_names}")
        print("-" * 40)
    session.close()


def update_movie(args):
    session = SessionLocal()
    try:
        movie = session.get(Film, args.id)
        if not movie:
            print(f"Movie with ID {args.id} not found.")
            return

        if args.title:
            movie.title = args.title
        if args.year:
            movie.year = args.year

        if args.director:
            movie.director = get_or_create(session, Director, surname=args.director)

        if args.operator:
            movie.operator = get_or_create(session, Operator, surname=args.operator)

        if args.producers:
            producers = []
            for prod_name in args.producers.split(","):
                producer = get_or_create(session, Producer, name=prod_name.strip())
                producers.append(producer)
            movie.producers = producers

        session.commit()
        print(f"Movie ID {args.id} updated.")
    except Exception as e:
        print(f"Error updating movie: {e}")
        session.rollback()
    finally:
        session.close()


def main():
    parser = argparse.ArgumentParser(description="Movie Database Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List
    parser_list = subparsers.add_parser("list", help="List movies")
    parser_list.add_argument(
        "--search", help="Search by title, year, director, operator or producer"
    )

    # Add
    parser_add = subparsers.add_parser("add", help="Add a new movie")
    parser_add.add_argument("--title", required=True, help="Movie title")
    parser_add.add_argument("--year", type=int, help="Release year")
    parser_add.add_argument("--director", required=True, help="Director surname")
    parser_add.add_argument("--operator", required=True, help="Operator surname")
    parser_add.add_argument("--producers", help="Comma-separated producer names")

    # Update
    parser_update = subparsers.add_parser("update", help="Update a movie")
    parser_update.add_argument("--id", required=True, type=int, help="Movie ID")
    parser_update.add_argument("--title", help="New title")
    parser_update.add_argument("--year", type=int, help="New year")
    parser_update.add_argument("--director", help="New director surname")
    parser_update.add_argument("--operator", help="New operator surname")
    parser_update.add_argument("--producers", help="New comma-separated producer names")

    args = parser.parse_args()

    Base.metadata.create_all(engine)

    # Auto-load data if empty
    session = SessionLocal()
    if session.query(Film).count() == 0:
        load_initial_data(session)
    session.close()

    if args.command == "list":
        list_movies(args)
    elif args.command == "add":
        add_movie(args)
    elif args.command == "update":
        update_movie(args)
    elif args.command is None:
        parser.print_help()


if __name__ == "__main__":
    main()
