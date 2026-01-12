import requests
import models
from sqlalchemy import or_  


class LocalRepository:
    

    def __init__(self):
        models.init_db()

    def list_movies(self, search_query=None):  
        session = models.SessionLocal()
        query = session.query(models.Film)

        if search_query:
            search_pattern = f"%{search_query}%"
            query = query.join(models.Director).filter(
                or_(
                    models.Film.title.ilike(search_pattern),
                    models.Director.surname.ilike(search_pattern),
                )
            )

        movies = query.all()
        data = []
        for m in movies:
            data.append(
                {
                    "id": m.id,
                    "title": m.title,
                    "year": m.year,
                    "director": m.director.surname,
                    "operator": m.operator.surname,
                    "producers": [p.name for p in m.producers],
                }
            )
        session.close()
        return data

    def add_movie(self, title, year, director, operator, producers):
        session = models.SessionLocal()
        try:
            models.create_film_in_db(
                session, title, year, director, operator, producers
            )
            print("Film added locally.")
        finally:
            session.close()

    def delete_movie(self, film_id):
        session = models.SessionLocal()
        film = session.query(models.Film).filter(models.Film.id == film_id).first()
        if film:
            session.delete(film)
            session.commit()
            print(f"Film ID {film_id} deleted locally.")
        else:
            print("Film not found.")
        session.close()

    def update_movie(
        self,
        film_id,
        title=None,
        year=None,
        director=None,
        operator=None,
        producers=None,
    ):
        session = models.SessionLocal()
        film = session.query(models.Film).filter(models.Film.id == film_id).first()
        if film:
            if title:
                film.title = title
            if year:
                film.year = year

            if director:
                d_obj = models.get_or_create(session, models.Director, surname=director)
                film.director = d_obj

            if operator:
                o_obj = models.get_or_create(session, models.Operator, surname=operator)
                film.operator = o_obj

            if producers is not None:
                new_producers = []
                for p_name in producers:
                    p_obj = models.get_or_create(
                        session, models.Producer, name=p_name.strip()
                    )
                    new_producers.append(p_obj)
                film.producers = new_producers

            session.commit()
            print(f"Film ID {film_id} updated locally.")
        else:
            print("Film not found.")
        session.close()


class RemoteRepository:
    

    def __init__(self, url="http://127.0.0.1:8000"):
        self.url = url

    def list_movies(self, search_query=None):  
        try:
            params = {}
            if search_query:
                params["search"] = search_query

            response = requests.get(f"{self.url}/films", params=params)

            if response.status_code == 200:
                return response.json()
            else:
                print("API Error:", response.text)
                return []
        except requests.exceptions.ConnectionError:
            print("Could not connect to server.")
            return []

    def add_movie(self, title, year, director, operator, producers):
        payload = {
            "title": title,
            "year": year,
            "director": director,
            "operator": operator,
            "producers": producers,
        }
        try:
            response = requests.post(f"{self.url}/films", json=payload)
            if response.status_code == 200:
                print("Film added via API.")
            else:
                print("API Error:", response.text)
        except requests.exceptions.ConnectionError:
            print("Could not connect to server.")

    def delete_movie(self, film_id):
        try:
            response = requests.delete(f"{self.url}/films/{film_id}")
            if response.status_code == 200:
                print(f"Film ID {film_id} deleted via API.")
            else:
                print("API Error:", response.text)
        except requests.exceptions.ConnectionError:
            print("Could not connect to server.")

    def update_movie(
        self,
        film_id,
        title=None,
        year=None,
        director=None,
        operator=None,
        producers=None,
    ):
        payload = {}
        if title:
            payload["title"] = title
        if year:
            payload["year"] = year
        if director:
            payload["director"] = director
        if operator:
            payload["operator"] = operator
        if producers is not None:
            payload["producers"] = producers

        try:
            response = requests.put(f"{self.url}/films/{film_id}", json=payload)
            if response.status_code == 200:
                print(f"Film ID {film_id} updated via API.")
            else:
                print("API Error:", response.text)
        except requests.exceptions.ConnectionError:
            print("Could not connect to server.")
