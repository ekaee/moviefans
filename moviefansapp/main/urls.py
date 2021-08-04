from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('movie/', views.movie, name='movie'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('action/', views.action, name='action'),
    path('animated/', views.animated, name='animated'),
    path('comedy/', views.comedy, name='comedy'),
    path('drama/', views.drama, name='drama'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('horror/', views.horror, name='horror'),
    path('scifi/', views.scifi, name='scifi'),
    
]