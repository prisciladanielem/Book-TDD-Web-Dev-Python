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
        self.assertTrue(response.content.startswith(b'<html>')) #Verifica se a resposta recebida inicia com '<html>'
        self.assertIn(b'<title> To-Do lists </title>', response.content) #Verifica se existe o código na resposta
        self.assertTrue(response.content.endswith(b'</html>')) #Verifica se a resposta termina com o texto