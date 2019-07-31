from selenium import webdriver

browser = webdriver.Firefox() #Inicia o navegador
browser.get('http://localhost:8000/') #Entra no endereço

assert 'Django' in browser.title #Verifica se o title da página é Django