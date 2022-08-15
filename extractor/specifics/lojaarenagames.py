from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
url = "https://lojaarenagames.com.br/far-cry-4-ps4-playstation-hits/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

price = soup.find("ins")
print(price.text)
title = soup.h5
print(title.text)
genero = soup.find("span",string="\nGênero ").parent.findNext('td')
print(genero.text.strip())
plataforma = soup.find("span",string="\nCategoria ").parent.findNext('td')
print(plataforma.text.strip())
desenvolvedora = soup.find("span",string="\nMarca ").parent.findNext('td')
print(desenvolvedora.text.strip())