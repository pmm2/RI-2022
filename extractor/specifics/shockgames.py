from bs4 import BeautifulSoup
import re
# import requests
# url = "https://www.shockgames.com.br/demons-souls-ps5"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
def shockextractor(html):
    price = html.find("s",  {"class": "preco-venda"}).text.strip()
    if hasattr(price,"text"):
        price = price.text.strip()
    title = html.h1.text
    genre = html.find("span",string="Gênero")
    if hasattr(genre,"parent"):
        genre = genre.parent.parent.text.strip().replace('Gênero','').replace('\n','')
    plataforma = title.split("-")[1].strip()
    dev = html.find("a", itemprop="url").text.strip()
    return [float(price.replace(',','.').replace("R$",'')),title,genre,plataforma,dev]