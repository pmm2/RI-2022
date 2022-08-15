from __future__ import division
from bs4 import BeautifulSoup
import re
import requests
url = "https://www.futuristicgames.com.br/grand-theft-auto-v-standard-edition-rockstar-games-ps3-fisico/p/MLB6084030?pdp_filters=category:MLB1144%7Cseller_id:161960254#position=3&search_layout=grid&type=item&tracking_id=c273642d-2098-4267-aea6-d94dea69e692"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
price = soup.find("span",  {"class": "andes-money-amount__fraction"})
print(price.text.strip())
title = soup.h1
print(title.text)
pattern = re.compile(r'^Gênero:')
genero = soup.find("li", string=pattern).text.split("Gênero: ")
print(genero[1])
plataforma = soup.find("span",  {"id": "picker-label-VIDEO_GAME_PLATFORM"})
print(plataforma.text)
pattern = re.compile(r'^Desenvolvido por')
desenvolvedora = soup.find("li", string=pattern).text.split("Desenvolvido por ")
print(desenvolvedora[1])