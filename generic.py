from __future__ import division
from operator import truediv
from bs4 import BeautifulSoup
import re
import requests

with open("./nba.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# url = "https://www.bigboygames.com.br/naruto-to-boruto-shinobi-striker-ps4-7014-p997519"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
def generic(html):
    plataforma =''
    dev =''
    tagspattern = re.compile('<.*?>')
    cleanedhtml = re.sub('\s', '', html.body.text)
    testehtml = re.sub(tagspattern,' ',str(html))
    testehtml = re.sub("\s",' ',testehtml)
    cleanedhtml2 = re.sub('\s', ' ', html.body.text)
    pattern = re.compile(r'R\$\d+[,|.]?\d*')
    search = re.findall(pattern,cleanedhtml)
    price = 0
    for s in search:
        aux_price = float(s.replace("R$",'').replace(',','.').strip())
        if aux_price > price:
            price = aux_price

    print("price : R$",price)

    # pattern = re.compile(r'[g|G]ênero:?\s*\w*')
    pattern = re.compile(r'[g|G]ênero:?')
    search = re.search(pattern,html.body.text)
    r =re.compile(r"\w*")
    cleanedhtml2 = list(filter(r.match,testehtml.split()))
    # print(cleanedhtml2)
    tb = False
    print("title:",html.h1.text.strip())
    for t in range(len(cleanedhtml2)):
        z = re.match(pattern,cleanedhtml2[t])
        if z:
            print("Genre:",cleanedhtml2[t+1])
            break
    pattern = re.compile(r'Plataforma|Modelo')
    for t in range(len(cleanedhtml2)):
        z = re.match(pattern,cleanedhtml2[t])
        if z:
            plataforma =cleanedhtml2[t+1]
            break
    print("Plataforma:",plataforma)
    pattern = re.compile(r'Desenvolvedor|Marca')
    for t in range(len(cleanedhtml2)):
        z = re.match(pattern,cleanedhtml2[t])
        if z:
            dev =cleanedhtml2[t+1]
            break
    print("Dev:",dev)
