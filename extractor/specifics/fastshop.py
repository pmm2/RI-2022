from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
# url = "https://www.kabum.com.br/produto/298373/jogo-elden-ring-xbox"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
#downloaded so the site is fully loaded
with open("./gt71.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
price = soup.find("div",  {"class": "price-current"})
print(price.text)
title = soup.h1
print(title.text)
pattern = re.compile(r'^Características')
description = soup.find("b",string=pattern).parent

# searchs for genero and desenvolvedor in description
for d in description:
    if d.__contains__('Gênero:'):
        print(d.split("Gênero: ")[1])
    if d.__contains__('Plataforma:'):
        print(d.split("Plataforma: ")[1])
    if d.__contains__('Desenvolvedor:'):
        print(d.split("Desenvolvedor: ")[1])
