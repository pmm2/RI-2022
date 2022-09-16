from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.mercadolivre.com.br/the-last-of-us-part-ii-standard-edition-sony-ps4-fisico/p/MLB15350833#reco_item_pos=0&reco_backend=best-seller&reco_backend_type=low_level&reco_client=highlights-rankings&reco_id=7c9a9847-c0de-44c1-bb49-183165fdffcc#trends_tracking_id=2ed4576c-3f9b-4a37-b094-17e8f7a3f6d5&component_id=BEST_SELLER'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
# with open("./fifa.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# driver.get(url)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# soup = BeautifulSoup(driver.page_source, 'html.parser')
def walkonsamelevel (sibling):
    if 'Gênero' in sibling.text:
        return sibling
    else:
        print(sibling.text)
        walkonsamelevel(sibling.findNext())
def mercadolivreextractor (html):
    html = html.find('main')
    price = ''
    title =''
    genre = ''
    plataforma = ''
    dev = ''
    title = html.find('h1').text
    price = html.find('meta',itemprop = 'price').attrs['content']
    genero = html.find("h2",string='O que você precisa saber sobre este produto').findNext('ul').findNext('li')
    genre = walkonsamelevel(genero)
    # price = htmlaftertitle.findAll('div')
    return [price,title,genre,plataforma,dev]

print(mercadolivreextractor(soup))

