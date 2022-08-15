from __future__ import division
from operator import truediv
from bs4 import BeautifulSoup
import re
import requests

# with open("./nba.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

url = "https://www.futuristicgames.com.br/grand-theft-auto-v-standard-edition-rockstar-games-ps3-fisico/p/MLB6084030?pdp_filters=category:MLB1144%7Cseller_id:161960254#position=3&search_layout=grid&type=item&tracking_id=c273642d-2098-4267-aea6-d94dea69e692"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
def generic(html):
    cleanedhtml = re.sub('\s', '', html.text)
    cleanedhtml2 = re.sub('\s', ' ', html.text)
    pattern = re.compile(r'R\$\d+[,|.]?\d*')
    search = re.findall(pattern,cleanedhtml)
    price = 0
    for s in search:

        aux_price = float(s.replace("R$",'').replace(',','.').strip())
        if aux_price > price:
            price = aux_price

    print("price : R$",price)
    pattern = re.compile(r'[g|G]ênero:?\s*\w*')
    search = re.search(pattern,str(html))
    if search != None:
        print(re.sub(r'[g|G]ênero:?\s*','',search[0]))


# generic(soup)
# print(repr(cleanedhtml.strip()))
# title = soup.h1
#
# pattern = re.compile(r'^Características')
# description = soup.find("b",string=pattern).parent

# # searchs for genero and desenvolvedor in description
# for d in description:
#     if d.__contains__('Gênero:'):
#         print(d.split("Gênero: ")[1])
#     if d.__contains__('Plataforma:'):
#         print(d.split("Plataforma: ")[1])
#     if d.__contains__('Desenvolvedor:'):
#         print(d.split("Desenvolvedor: ")[1])
