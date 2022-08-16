from __future__ import division
from operator import truediv
from bs4 import BeautifulSoup
import re
import requests
from  generic import generic
from  specifics.bigboygames import bigboyextractor
from  specifics.vnsgames import vnsextractor
from  specifics.fastshop import fastextractor
from  specifics.futuristicGames import futuristicextractor
from  specifics.lojaarenagames import arenaextractor
from  specifics.shockgames import shockextractor
from  specifics.ibyte import ibyteextractor
with open("./farcry.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print("far cry vns games ")
print(generic(soup))
print(vnsextractor(soup))
print()

with open("./fc6.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print("far cry fast shop")
print(generic(soup))
print(fastextractor(soup))
print()

url = "https://www.shockgames.com.br/demons-souls-ps5"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("demon souls shockgames ")
print(generic(soup))
print(shockextractor(soup))
print()

url = "https://lojaarenagames.com.br/far-cry-4-ps4-playstation-hits/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("far cry lojaarenagames")
print(generic(soup))
print(arenaextractor(soup))
print()

url = "https://www.futuristicgames.com.br/grand-theft-auto-v-standard-edition-rockstar-games-ps3-fisico/p/MLB6084030?pdp_filters=category:MLB1144%7Cseller_id:161960254#position=3&search_layout=grid&type=item&tracking_id=c273642d-2098-4267-aea6-d94dea69e692"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("gta futuristic")
print(generic(soup))
print(futuristicextractor(soup))
print()

url = "https://www.bigboygames.com.br/naruto-to-boruto-shinobi-striker-ps4-7014-p997519"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("naruto big boy")
print(generic(soup))
print(bigboyextractor(soup))
print()
with open("./fifaIbyte.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print("fifa ibyte")
print(generic(soup))
print(ibyteextractor(soup))