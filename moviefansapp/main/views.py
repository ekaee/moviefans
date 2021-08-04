from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html',)

def signup(request):
    return render(request, 'main/signup.html',)

def login(request):
    return render(request, 'main/login.html',)

def about(request):
    return render(request, 'main/about.html',)

def movie(request):
    return render(request, 'main/movie.html',)

def profile(request):
    return render(request, 'main/profile.html',)

def search(request):
    return render(request, 'main/search.html',)
    
#genres

def action(request):
    return render(request, 'main/genre_action.html',)
    
def animated(request):
    return render(request, 'main/genre_animated.html',)
    
def comedy(request):
    return render(request, 'main/genre_comedy.html',)
    
def drama(request):
    return render(request, 'main/genre_drama.html',)
    
def fantasy(request):
    return render(request, 'main/genre_fantasy.html',)
    
def horror(request):
    return render(request, 'main/genre_horror.html',)
    
def scifi(request):
    return render(request, 'main/genre_scifi.html',)
