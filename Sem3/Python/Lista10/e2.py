from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.orm import validates
from sqlalchemy import create_engine
from __future__ import annotations
from typing import List


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
    def validate_surname(self,key,surname):
        if len(surname)<3:
            raise ValueError("Surname is too short")
        return surname

class Producer(Base):
    __tablename__ = "Producers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    produced: Mapped[List[Film]] = relationship(
        secondary=production, back_populates="producers"
    )
    @validates("surname")
    def validate_surname(self,key,surname):
        if len(surname)<3:
            raise ValueError("Surname is too short")
        return surname


class Operator(Base):
    __tablename__ = "Operators"
    id = mapped_column(Integer, primary_key=True)
    surname = mapped_column(String)
    operated: Mapped[List[Film]] = relationship("Film", back_populates="operator")
    @validates("surname")
    def validate_surname(self,key,surname):
        if len(surname)<3:
            raise ValueError("Surname is too short")
        return surname