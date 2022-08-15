from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
url = "https://www.shockgames.com.br/demons-souls-ps5"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
price = soup.find("strong",  {"class": "preco-promocional"})
print(price.text.strip())
title = soup.h1
print(title.text)
genero = soup.find("span",string="Gênero").parent.parent
print(genero.text.strip())
plataforma = title.text.split("-")
print(plataforma[1].strip())
desenvolvedora = soup.find("a", itemprop="url")
print(desenvolvedora.text.strip())