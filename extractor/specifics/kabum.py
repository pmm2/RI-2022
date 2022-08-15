from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
# url = "https://www.kabum.com.br/produto/298373/jogo-elden-ring-xbox"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
#downloaded so the site is fully loaded
with open("./eldenring.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
price = soup.find("h4",  {"itemprop": "price"})
print(price.text)
title = soup.h1
print(title.text)
pattern = re.compile(r'^- Gênero')
genero = soup.find("p",string=pattern)
print(genero.text.replace('- Gênero:',''))
pattern = re.compile(r'^- Marca')
desenvolvedora = soup.find("p",string=pattern)
print(desenvolvedora.text.replace("- Marca: ",''))
pattern = re.compile(r'^- Modelo')
desenvolvedora = soup.find("p",string=pattern)
print(desenvolvedora.text.replace("- Modelo: ",''))
# print(re.sub('<[^<]+?>', '',str(genero) ))
# pattern = re.compile(r'^Desenvolvedor|Developer|Marca')
# desenvolvedor = soup.find("b",string=pattern).parent.findNext('td')
# print(re.sub('<[^<]+?>', '',str(desenvolvedor) ))
# pattern = re.compile(r'^Plataforma')
# plataforma = soup.find("b",string=pattern).parent.findNext('td')
# print(re.sub('<[^<]+?>', '',str(plataforma) ))
