from main.models import Movie
from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.models import Genre, Movie
from main.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    movies_most_viewed = Movie.objects.order_by("-views")[:5]
    movies_top_rated = Movie.objects.order_by("-rating")[:5]
    genre_list = Genre.objects.all().order_by("word")

    context = {}
    context["movies_most_viewed"] = movies_most_viewed
    context["movies_top_rated"] = movies_top_rated
    context["genre_list"] = genre_list

    return render(request, "main/index.html", context=context)


def about(request):
    return HttpResponse("About")


def movie(request, movie_slug):
    context = {}

    try:
        movie = Movie.objects.get(slug=movie_slug)
        context["movie"] = movie
    except:
        context["movie"] = None

    return render(
        request, "main/movie.html", context=context
    )  # TODO: check template name


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

    return render(
        request, "main/genre.html", context=context
    )  # TODO: check template name


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES["picture"]

            profile.save()
            registered = True
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
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("main:index"))
            else:
                return HttpResponse("Your main account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "main/login.html")


@login_required
def logout(request):
    logout(request)
    return redirect(reverse("main:index"))


# TODO: add movie page
@login_required
def add_movie(request):
    return


def search(request):
    return HttpResponse("Search")
