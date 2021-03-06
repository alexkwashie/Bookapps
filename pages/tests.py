from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

#Test the Templates
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

#Testing the HTML
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'HOME PAGE')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'This text shouldnt be be on this page')

    def test_homepage_url_resolves_homepagesview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
