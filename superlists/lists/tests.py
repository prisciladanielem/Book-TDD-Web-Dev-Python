from django.test import TestCase
# from django.template.loader import render_to_string
from django.urls import resolve
from django.http import HttpRequest

from superlists.lists.views import home_page

from superlists.lists.models import Item

class HomePageTest(TestCase):

    #Teste para verificar se é possível resolver a url da página inicial
    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/') #Procura a view associada a essa url
        self.assertEqual(found.func, home_page)

    #Teste para verificar se a página inicial está retornando o html corretamente
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #Cria uma request http
        response = self.client.get('/') #Passa a request para a home_page e captura a resposta
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item-text'] = 'A new list item'

        response = self.client.post('/', data={'item_text':'A new list item'})

        self.assertIn('A new list item', response.content.decode())

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')