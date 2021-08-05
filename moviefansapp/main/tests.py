from django.test import TestCase, Client
from .models import Movie
import os
import re
# Create your tests here.


class PagesTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.failUnlessEqual(response.status_code, 200)
        
    def test_register(self):
        response = self.client.get('/register/')
        self.failUnlessEqual(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get('/about/')
        self.failUnlessEqual(response.status_code, 200)
        
    def test_movie(self):
        response = self.client.get('/movie/action-movie-1')
        self.failUnlessEqual(response.status_code, 200)
    

class viewTest(TestCase):
    
    def test_search(self):
        response = self.client.post('/search/', {'q': 'action'})
        self.failUnlessEqual(response.status_code, 200)
    
class TemplatesTest(TestCase):
    
    def test_templates_exist(self):
        index_path = os.path.join(self.rango_templates_dir, 'index.html')
        about_path = os.path.join(self.rango_templates_dir, 'about.html')