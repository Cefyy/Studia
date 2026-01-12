from __future__ import annotations
from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    mapped_column,
    Mapped,
    Session,
    sessionmaker,
    validates,
)
from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine, select
from typing import List
import os
import json  

# --- BAZA DANYCH I MODELE ---


class Base(DeclarativeBase):
    pass


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
    director_id = mapped_column(Integer, ForeignKey("Directors.id"))
    director = relationship("Director", back_populates="directed")
    producers: Mapped[List["Producer"]] = relationship(
        secondary=production, back_populates="produced"
    )
    operator_id = mapped_column(Integer, ForeignKey("Operators.id"))
    operator = relationship("Operator", back_populates="operated")


class Director(Base):
    __tablename__ = "Directors"
    id = mapped_column(Integer, primary_key=True)
    surname = mapped_column(String)
    directed: Mapped[List[Film]] = relationship("Film", back_populates="director")


class Producer(Base):
    __tablename__ = "Producers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    produced: Mapped[List[Film]] = relationship(
        secondary=production, back_populates="producers"
    )


class Operator(Base):
    __tablename__ = "Operators"
    id = mapped_column(Integer, primary_key=True)
    surname = mapped_column(String)
    operated: Mapped[List[Film]] = relationship("Film", back_populates="operator")


# --- KONFIGURACJA ---
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


def create_film_in_db(
    session: Session,
    title,
    year,
    director_surname,
    operator_surname,
    producer_names,
    commit=True,
):
    director = get_or_create(session, Director, surname=director_surname)
    operator = get_or_create(session, Operator, surname=operator_surname)

    producers = []
    if producer_names:
        for prod_name in producer_names:
            producer = get_or_create(session, Producer, name=prod_name.strip())
            producers.append(producer)

    film = Film(
        title=title,
        year=year,
        director=director,
        operator=operator,
        producers=producers,
    )
    session.add(film)

    
    if commit:
        session.commit()
    return film


# --- ŁADOWANIE DANYCH ---


def load_initial_data(session: Session):
    
    if session.query(Film).count() > 0:
        return

    data_path = os.path.join(script_dir, "data.json")
    if not os.path.exists(data_path):
        print(f"Warning: {data_path} not found.")
        return

    print("Loading initial data from data.json...")
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            
            year_val = item.get("year")
            if year_val:
                year_val = int(year_val)
            else:
                year_val = None

            create_film_in_db(
                session,
                title=item["title"],
                year=year_val,  
                director_surname=item["director"],
                operator_surname=item["operator"],
                producer_names=item.get("producers", []),
                commit=False,
            )

        
        session.commit()
        print(f"Loaded {len(data)} movies successfully.")

    except Exception as e:
        session.rollback()  # Cofnij zmiany jeśli wystąpił błąd
        print(f"Error loading data: {e}")


def init_db():
    Base.metadata.create_all(engine)
    # Po utworzeniu tabel, spróbuj załadować dane
    session = SessionLocal()
    load_initial_data(session)
    session.close()
