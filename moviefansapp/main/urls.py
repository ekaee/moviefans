from django.conf.urls import include, url
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("private/", views.private, name="private"),
    path("about/", views.about, name="about"),
    path("movie/<slug:movie_slug>", views.movie, name="movie"),
    path("movie_list/", views.movie_list, name="movie_list"),
    path("genre/<slug:genre_slug>", views.genre, name="genre"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register, name="register"),
    path("add_movie/", views.add_movie, name="add_movie"),
    path("like_movie/", views.likeMovie, name="like_movie"),
    path("search/", views.search, name="search"),
    path("add_comment/", views.add_comment, name="add_comment"),
    path("upvote_comment/", views.upvote_comment, name="upvote_comment"),
    path("add_view/", views.add_view, name="add_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
