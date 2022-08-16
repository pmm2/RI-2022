from __future__ import division
from operator import truediv
from bs4 import BeautifulSoup
import re
import requests
from generic import generic

with open("./farcry.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print("far cry vns games ")
generic(soup)
with open("./fc6.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print("far cry fast shop")
generic(soup)
# with open("./fifaIbyte.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# print("fifa ibyte")
# generic(soup)
# with open("./nba.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# print("nba ibyte")
generic(soup)
url = "https://www.shockgames.com.br/demons-souls-ps5"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("demon souls shockgames ")
generic(soup)

url = "https://lojaarenagames.com.br/far-cry-4-ps4-playstation-hits/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("far cry lojaarenagames")
generic(soup)

url = "https://www.futuristicgames.com.br/grand-theft-auto-v-standard-edition-rockstar-games-ps3-fisico/p/MLB6084030?pdp_filters=category:MLB1144%7Cseller_id:161960254#position=3&search_layout=grid&type=item&tracking_id=c273642d-2098-4267-aea6-d94dea69e692"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("gta futuristic")
generic(soup)

url = "https://www.bigboygames.com.br/naruto-to-boruto-shinobi-striker-ps4-7014-p997519"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("naruto big boy")
generic(soup)