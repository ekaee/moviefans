from main.models import Comments, Movie, UserProfile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.models import Genre, Movie
from main.forms import AddMovieForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


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
    return HttpResponse("About")


# Single Movie Detail
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


def movie_list(request):
    return render(request, "main/movielist.html")


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


def search(request):
    query = request.GET.get("q", "")
    if query:
        queryset = Q(name__icontains=query)
        results = Movie.objects.filter(queryset).distinct()
    else:
        results = []
    return render(request, "search.html", {"results": results, "query": query})


@login_required
def likeMovie(request):
    if request.method == "GET":
        movie_slug = request.GET["movie_slug"]
        likedMovie = Movie.objects.get(slug=movie_slug)
        likedMovie.rating += 1
        likedMovie.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


@login_required
def add_comment(request):
    if request.user.is_authenticated():
        user = request.user
        profile = UserProfile.objects.get(user=user)

        if request.method == "POST":
            movie_id = request.POST.get("movie_id")
            movie = Movie.objects.get(movie_id=movie_id)
            content = request.POST.get("content")

            comment = Comments()
            comment.user_id = profile
            comment.movie_id = movie
            comment.content = content
            comment.save()

            return HttpResponse("Success!")

    return HttpResponse("Add comment request failed.")


@login_required
def upvote_comment(request):
    if request.user.is_authenticated():
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
