from typing import ContextManager
from main.models import Comments, Movie, UserProfile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.models import Genre, Movie
from main.forms import AddMovieForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


def index(request):
    movies_most_viewed = Movie.objects.order_by("-views")[:5]
    movies_top_rated = Movie.objects.order_by("-rating")[:5]
    genre_list = Genre.objects.all().order_by("name")

    context = {}
    context["movies_most_viewed"] = movies_most_viewed
    context["movies_top_rated"] = movies_top_rated
    context["genre_list"] = genre_list

    return render(request, "main/index.html", context=context)


def about(request):
    return render(request, "main/about.html")


# Single Movie Detail
def movie(request, movie_slug):
    context = {}

    try:
        movie = Movie.objects.get(slug=movie_slug)
        comments = Comments.objects.filter(movie_id=movie)
        context["movie"] = movie
        context["comments"] = comments
    except:
        context["movie"] = None
        context["comments"] = None

    return render(request, "main/movie.html", context=context)


def movie_list(request):
    context = {}

    try:
        movies = Movie.objects.all().order_by("name")
        context["movies"] = movies
    except:
        context["movies"] = None

    return render(request, "main/movielist.html", context=context)


def genre(request, genre_slug):  # genre detail page
    context = {}

    try:
        genre = Genre.objects.get(slug=genre_slug)
        genre_movies = Movie.objects.filter(genre_id=genre)
        context["genre"] = genre
        context["genre_movies"] = genre_movies
    except:
        context["genre"] = None
        context["genre_movies"] = None

    return render(request, "main/genre.html", context=context)


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            # user.save()
            login(request, user)
            messages.success(request, "Registration successful.")

            # profile = profile_form.save(commit=False)
            # profile.user = user

            # if "picture" in request.FILES:
            #     profile.picture = request.FILES["picture"]

            # profile.save()
            # registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(
        request,
        "main/register.html",
        context={
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )


# TODO: Check URLs
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(reverse("main:index"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "main/login.html", context={"login_form": form})


@login_required
def logout_page(request):
    logout(request)
    return redirect(reverse("main:index"))


def search(request):
    query = request.POST.get("query_name")
    if query:
        queryset = Q(name__icontains=query)
        results = Movie.objects.filter(queryset).distinct()
    else:
        results = []
    return render(request, "main/search.html", {"results": results, "query": query})


@login_required
def likeMovie(request):
    query = request.POST.get("query_name")
    if query:
        queryset = Q(slug__icontains=query)
        results = Movie.objects.filter(queryset).distinct()
        if results[0]:
            likedMovie = results[0]
            likedMovie.rating += 1
            likedMovie.save()
    else:
        results = []
    return redirect("/movie/" + query)


@login_required
def add_comment(request):
    if request.user.is_authenticated:
        user = request.user

        if user is None:
            return HttpResponse("Could not get user from request.")

        if hasattr(user, "_wrapped") and hasattr(user, "_setup"):
            if user._wrapped.__class__ == object:
                user._setup()
            user = user._wrapped

        if request.method == "POST":
            movie_slug = request.POST.get("movie_slug")
            movie = Movie.objects.get(slug=movie_slug)

            if movie is not None:
                content = request.POST.get("content")

                comment = Comments.objects.create(
                    movie_id=movie,
                    content=content,
                    username=user.username,
                    user_id=user,
                )

            return HttpResponse("Success!")

    return HttpResponse("Add comment request failed.")


@login_required
def upvote_comment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            comment_id = request.POST.get("comment_id")
            comment = Comments.objects.get(id=comment_id)
            comment.upvote += 1
            comment.save()
            return HttpResponse("Upvote Success!")

    return HttpResponse("Upvote comment request failed.")


@login_required
def add_movie(request):
    if request.method == "POST":
        movie_form = AddMovieForm(request.POST)

        if movie_form.is_valid():
            newMovie = movie_form.save(commit=False)

            newMovie.save()
        else:
            print(movie_form.errors)
    else:
        movie_form = AddMovieForm()

    # return render(
    #     request,
    #     "main/index.html",
    #     context={
    #         "movie_form": movie_form,
    #     },
    # )

    return redirect(reverse("main:index"))


def add_view(request):
    if request.method == "GET":
        movie_slug = request.GET["movie"]
        movie = Movie.objects.get(slug=movie_slug)
        movie.views += 1
        movie.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Invalid request")


@login_required
def private(request):
    return HttpResponse("Only seen when logged in.")
