import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviefansapp.settings")

import django

django.setup()
from main.models import Movie, Genre, Comments


def populate():
    action_movies = [
        {
            "name": "Action Movie 1",
            "description": "Action Movie 1 description",
        },
        {
            "name": "Action Movie 2",
            "description": "Action Movie 2 description",
        },
    ]

    horror_movies = [
        {
            "name": "Horror Movie 1",
            "description": "Horror Movie 1 description",
        },
        {
            "name": "Horror Movie 2",
            "description": "Horror Movie 2 description",
        },
    ]

    comedy_movies = [
        {
            "name": "Comedy Movie 1",
            "description": "Comedy Movie 1 description",
        },
        {
            "name": "Comedy Movie 2",
            "description": "Comedy Movie 2 description",
        },
    ]

    genres = [
        {"name": "Action", "pages": action_movies},
        {"name": "Horror", "pages": horror_movies},
        {"name": "Comedy", "pages": comedy_movies},
    ]

    for gx in genres:
        g = add_genre(gx['name'])
        for mx in gx['pages']:
            add_movie(g, mx['name'], mx['description'])



def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

def add_movie(genre, name, description):
    m = Movie.objects.get_or_create(genre_id=genre, name=name, description=description)[0]
    m.save()
    return m

if __name__ == '__main__':
    populate()