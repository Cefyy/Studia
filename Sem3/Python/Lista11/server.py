from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import or_  # Dodaj ten import na górze jeśli go nie ma
import models

app = FastAPI()

models.init_db()


class FilmCreate(BaseModel):
    title: str
    year: int
    director: str
    operator: str
    producers: List[str]


class FilmResponse(BaseModel):
    id: int
    title: str
    year: Optional[int]
    director: str
    operator: str
    producers: List[str]


# --- READ ---
@app.get("/films", response_model=List[FilmResponse])
def get_films(search: Optional[str] = None):  # Dodano parametr search
    session = models.SessionLocal()
    query = session.query(models.Film)

    if search:
        # Filtrowanie: Tytuł LUB Reżyser (nazwisko) zawiera frazę
        # ilike jest case-insensitive (w SQLite like też zazwyczaj jest)
        search_pattern = f"%{search}%"
        query = query.join(models.Director).filter(
            or_(
                models.Film.title.ilike(search_pattern),
                models.Director.surname.ilike(search_pattern),
            )
        )

    films = query.all()
    results = []
    for f in films:
        results.append(
            {
                "id": f.id,
                "title": f.title,
                "year": f.year,
                "director": f.director.surname,
                "operator": f.operator.surname,
                "producers": [p.name for p in f.producers],
            }
        )
    session.close()
    return results


# --- CREATE ---
@app.post("/films")
def create_film(film: FilmCreate):
    session = models.SessionLocal()
    try:
        models.create_film_in_db(
            session, film.title, film.year, film.director, film.operator, film.producers
        )
        return {"message": "Film added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()


# --- DELETE (Dodane dla wymogu CRUD) ---
@app.delete("/films/{film_id}")
def delete_film(film_id: int):
    session = models.SessionLocal()
    film = session.query(models.Film).filter(models.Film.id == film_id).first()
    if not film:
        session.close()
        raise HTTPException(status_code=404, detail="Film not found")

    session.delete(film)
    session.commit()
    session.close()
    return {"message": "Film deleted"}


# --- UPDATE (Dodane dla wymogu CRUD) ---
class FilmUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    director: Optional[str] = None
    operator: Optional[str] = None
    producers: Optional[List[str]] = None


@app.put("/films/{film_id}")
def update_film(film_id: int, film_update: FilmUpdate):
    session = models.SessionLocal()
    film = session.query(models.Film).filter(models.Film.id == film_id).first()
    if not film:
        session.close()
        raise HTTPException(status_code=404, detail="Film not found")

    # Aktualizacja prostych pól
    if film_update.title:
        film.title = film_update.title
    if film_update.year:
        film.year = film_update.year

    # Aktualizacja relacji (Reżyser)
    if film_update.director:
        director = models.get_or_create(
            session, models.Director, surname=film_update.director
        )
        film.director = director

    # Aktualizacja relacji (Operator)
    if film_update.operator:
        operator = models.get_or_create(
            session, models.Operator, surname=film_update.operator
        )
        film.operator = operator

    # Aktualizacja relacji (Producenci)
    if film_update.producers is not None:
        new_producers = []
        for p_name in film_update.producers:
            prod = models.get_or_create(session, models.Producer, name=p_name.strip())
            new_producers.append(prod)
        film.producers = new_producers

    session.commit()
    session.close()
    return {"message": "Film updated"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
