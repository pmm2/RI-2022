from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
# url = "https://www.ibyte.com.br/game-fifa-18-xbox-one/p"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
#downloaded so the site is fully loaded
with open("./fifaIbyte.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
price = soup.find("span",  {"class": "js-buy-box-best-price"})
print(price.text)
title = soup.find("div",{"class":"productName"})
print(title.text)
pattern = re.compile(r'^(Gênero|Categoria do Jogo)')
genero = soup.find("b",string=pattern).parent.findNext('td')
print(re.sub('<[^<]+?>', '',str(genero) ))
pattern = re.compile(r'^Desenvolvedor|Developer|Marca')
desenvolvedor = soup.find("b",string=pattern).parent.findNext('td')
print(re.sub('<[^<]+?>', '',str(desenvolvedor) ))
pattern = re.compile(r'^Plataforma')
plataforma = soup.find("b",string=pattern).parent.findNext('td')
print(re.sub('<[^<]+?>', '',str(plataforma) ))
