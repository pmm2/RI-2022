from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
# url = "https://www.ibyte.com.br/game-fifa-18-xbox-one/p"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
#downloaded so the site is fully loaded
with open("./eldenringextra.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
price = soup.find("span",  id="product-price")
print(price.text)
title = soup.h1
print(title.text)
pattern = re.compile(r'^(Gênero)')
genero = soup.find("span",string=pattern).findNext('span')
print(genero.text)
pattern = re.compile(r'^Desenvolvedor|Developer|Marca')
desenvolvedor = soup.find("b",string=pattern).parent.findNext('td')
print(re.sub('<[^<]+?>', '',str(desenvolvedor) ))
pattern = re.compile(r'^Plataforma')
plataforma = soup.find("b",string=pattern).parent.findNext('td')
print(re.sub('<[^<]+?>', '',str(plataforma) ))