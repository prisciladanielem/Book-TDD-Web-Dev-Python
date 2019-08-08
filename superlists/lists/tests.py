from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from superlists.lists.views import home_page

class HomePageTest(TestCase):

    #Teste para verificar se é possível resolver a url da página inicial
    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/') #Procura a view associada a essa url
        self.assertEqual(found.func, home_page)

    #Teste para verificar se a página inicial está retornando o html corretamente
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #Cria uma request http
        response = home_page(request) #Passa a request para a home_page e captura a resposta
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html) # Compara se o template é o mesmo que veio na resposta http