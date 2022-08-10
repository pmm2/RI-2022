from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
url = "https://www.bigboygames.com.br/naruto-to-boruto-shinobi-striker-ps4-7014-p997519"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
div_tabelas = soup.find_all("tr")
price = soup.find("span",attrs={'data-app': 'product.price'})
print(price.text)
title = soup.h1
print(title.text)
genero = soup.find("td",string="Categoria").findNext("td")
print(genero.text)
plataforma = soup.find("td",string="Modelo").findNext("td")
print(plataforma.text)
desenvolvedora = soup.find("strong",string="Marca").parent.parent.parent.findNext('td').findChildren("b",recursive=True)
print(desenvolvedora[0].text)