from django.conf.urls import include, url
from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("movie/<slug:movie_slug>", views.movie, name="movie"),
    path("genre/<slug:genre_slug>", views.genre, name="genre"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("add_movie/", views.add_movie, name="add_movie"),
    path("like_movie/", views.likeMovie, name="likemovie"),
    path("search/", views.search, name="search"),
    path("add_comment/", views.add_comment, name="add_comment"),
    path("upvote_comment/", views.upvote_comment, name="upvote_comment"),
]
