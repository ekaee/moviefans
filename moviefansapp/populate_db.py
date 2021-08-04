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
        {"name": "Action"},
        {"name": "Horror"},
        {"name": "Comedy"},
    ]
