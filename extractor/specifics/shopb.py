from bs4 import BeautifulSoup
import re
import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = 'https://www.shopb.com.br/jogo-monster-energy-supercross-the-official-videogame-5-ps4'
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# with open("./fifa.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# driver.get(url)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)
# soup = BeautifulSoup(driver.page_source, 'html.parser')


def shopbextractor(html):
    price = ''
    title = ''
    dev = ''
    genre = ''
    plataforma = ''
    table = html.find('h2', string='ESPECIFICAÇÕES').findNext('ul')
    table = table.findAll('li')
    for d in table:
        if 'Desenvolvedora:' in d.text:
            dev = d.text.split("Desenvolvedora:")[1]
    plataforma = html.find(
        'h2', string='REQUISITOS').findNext('li').text.strip()
    title = html.find('h1').text.strip()
    price = html.find(
        'strong', {'class': 'preco-promocional cor-principal'}).text.strip()
    # price = htmlaftertitle.findAll('div')
    return [price, title, genre, plataforma, dev]

# print(shopbextractor(soup))
