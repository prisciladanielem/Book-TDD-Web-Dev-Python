from django.urls import resolve
from django.test import TestCase
from superlists.lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/') #Procura a view associada a essa url
        self.assertEqual(found.func, home_page)