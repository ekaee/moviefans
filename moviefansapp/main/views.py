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
