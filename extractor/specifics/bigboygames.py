
from bs4 import BeautifulSoup
import re
# import requests
# url = "https://www.bigboygames.com.br/naruto-to-boruto-shinobi-striker-ps4-7014-p997519"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
def bigboyextractor(html):
    preco =html.find("div",attrs={'class': 'precode'})
    if hasattr(preco,"text"):
        preco=preco.text.strip()
        price = re.search(r'\d+,\d+',preco)[0].replace(',','.')
    else:
        price =html.find("span",attrs={'data-app': 'product-price'})
        if price != None:
            price = price.replace(',','.')
    title = html.h1.text
    genre = html.find("td",string="Categoria")
    if hasattr(genre,"text"):
        genre=genre.findNext("td").text
    plataforma = html.find("td",string="Modelo")
    if hasattr(plataforma,"text"):
        plataforma=plataforma.findNext("td").text
    dev = html.find("td",string="Marca")
    if hasattr(dev,"text"):
        dev=dev.findNext("td").text
    if price !=None:
        price = float(price)
    return [price,title,genre,plataforma,dev]