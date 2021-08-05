from django.test import TestCase, Client
from .models import Movie

# Create your tests here.


class CinemaPagesTestCase(TestCase):
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
    
    def test_search(self):
        response = self.client.post('/search/', {'q': 'action'})
        self.failUnlessEqual(response.status_code, 200)

# something wrong with this test
    def test_genre(self):
        response = self.client.get('/genre/comedy')
        self.assertIn(response.status_code, (301, 302))

