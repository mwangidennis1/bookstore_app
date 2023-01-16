from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from .views import HomePageView,AboutPageView

class HomePageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code ,200)
    
    def test_homepage_url(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

class AboutPageTests(SimpleTestCase):

    def test_about_status_code(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)
    def test_about_url(self):
        response=self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    