import os
from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

# Test: user creation
def create_user():
        user = User.objects.get_or_create(username='testuser',email='test@test.com')[0]
        user.set_password('testabc123')
        user.save()
        return user

# Test: url redirects  
class PagesResponseTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertTrue(response.status_code, 200)
        
    def test_register(self):
        response = self.client.get('/register/')
        self.assertTrue(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get('/about/')
        self.assertTrue(response.status_code, 200)
        
    def test_movie(self):
        response = self.client.get('/movie_listxx/')
        self.assertTrue(response.status_code, 200)
    
# Test: search helper func test
class searchTest(TestCase):
    
    def test_search(self):
        response = self.client.post('/search/', {'q': 'action'})
        self.assertTrue(response.status_code, 200)

# Test: checking if necessary files exist
class TemplatesTest(TestCase):
    
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.app_templates_dir = os.path.join(self.templates_dir, 'main')
    
    def test_templates_exist(self):
        index_path = os.path.join(self.app_templates_dir, 'index.html')
        about_path = os.path.join(self.app_templates_dir, 'about.html')
        movie_path = os.path.join(self.app_templates_dir, 'movie.html')
        movielist_path = os.path.join(self.app_templates_dir, 'movielist.html')
        search_path = os.path.join(self.app_templates_dir, 'search.html')
        login_path = os.path.join(self.app_templates_dir, 'login.html')
        register_path = os.path.join(self.app_templates_dir, 'register.html')
        genre_path = os.path.join(self.app_templates_dir, 'genre.html')
        base_path = os.path.join(self.app_templates_dir, 'base.html')
              
        self.assertTrue(os.path.isfile(index_path), f"Your index.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(about_path), f"Your about.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(movie_path), f"Your movie.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(movielist_path), f"Your movielist.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(search_path), f"Your search.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(login_path), f"Your login.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(register_path), f"Your register.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(genre_path), f"Your genre.html template does not exist, or is in the wrong location.")
        self.assertTrue(os.path.isfile(base_path), f"Your base.html template does not exist, or is in the wrong location.")

# Test: basic authentication check
class AuthenticateTest(TestCase):
    
    def test_addmovie(self): 
        user = create_user()    
        self.client.login(username=user.username, password=user.password)  
        
        response = self.client.get(reverse('main:add_movie_page'))
        self.assertTrue(response.status_code, 200)
        
    def test_addcomment(self): 
        user = create_user()    
        self.client.login(username=user.username, password=user.password)  
        
        response = self.client.get(reverse('main:add_comment'))
        self.assertTrue(response.status_code, 200)
    
    def test_Resrict_addcomment(self):
        response = self.client.get(reverse('main:add_comment'))
        self.assertEqual(response.status_code, 302, "failed to be restricted")
        
#Test: check the response Topviewed and Topupvotes function
class TestTopViewed(TestCase):
    
    # check top Viewed movies
    def test_top_viewed(self):
        response = self.client.get(reverse('main:index'))
        expected_movies_most_viewed = list(Movie.objects.order_by("-views")[:5])
        self.assertTrue('movies_most_viewed' in response.context, "Couldn't find 'movies_most_viewed' variable in the index() view's context dictionary. Check index.html")
        self.assertEqual(type(response.context['movies_most_viewed']), QuerySet, "movies_most_viewed' variable in the index() view's context dictionary doesn't return a QuerySet as expected.")
        self.assertEqual(expected_movies_most_viewed, list(response.context['movies_most_viewed']), 
                         f"The 'pages' context dictionary variable for the index() view didn't return the QuerySet we were expectecting: got {list(response.context['movies_most_viewed'])}, expected {expected_movies_most_viewed}. Did you apply the correct ordering to the filtered results?")
        
    # check top Upvoted movies
    def test_topUpvoted(self):
        response = self.client.get(reverse('main:index'))
        expected_movies_top_rated = list(Movie.objects.order_by("-rating")[:5])
        self.assertTrue('movies_top_rated' in response.context, "Couldn't find 'movies_top_rated' variable in the index() view's context dictionary. Check index.html")
        self.assertEqual(type(response.context['movies_top_rated']), QuerySet, "movies_top_rated' variable in the index() view's context dictionary doesn't return a QuerySet as expected.")
        self.assertEqual(expected_movies_top_rated, list(response.context['movies_most_viewed']), 
                         f"The 'pages' context dictionary variable for the index() view didn't return the QuerySet we were expectecting: got {list(response.context['movies_top_rated'])}, expected {expected_movies_top_rated}. Did you apply the correct ordering to the filtered results?")
        