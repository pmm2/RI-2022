from bs4 import BeautifulSoup
import re
# import requests
# url = "https://www.ibyte.com.br/returnal-ps5/p"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
#downloaded so the site is fully loaded
# with open("./fifaIbyte.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
def ibyteextractor (html):
    price = html.find("strong",  {"class": "skuBestPrice"})
    if hasattr(price,"text"):
        price = price.text
    title= html.find("div",{"class":"productName"})
    if hasattr(title,"text"):
        title = title.text

    pattern = re.compile(r'^(Gênero|Categoria do Jogo)',flags=re.IGNORECASE)
    genero = html.find("b",string=pattern)
    if hasattr(genero,"parent"):
        genero = genero.parent.findNext('td')
    genre =re.sub('<[^<]+?>', '',str(genero) )

    pattern = re.compile(r'^Desenvolvedor|Developer|Marca',flags=re.IGNORECASE)
    desenvolvedor = html.find("b",string=pattern)
    if hasattr(desenvolvedor,"parent"):
        desenvolvedor = desenvolvedor.parent.findNext('td')
    dev = re.sub('<[^<]+?>', '',str(desenvolvedor) )

    pattern = re.compile(r'^Plataforma',flags=re.IGNORECASE)
    plataforma = html.find("b",string=pattern)
    if hasattr(plataforma,"parent"):
        plataforma = plataforma.parent.findNext('td')
    plataforma= re.sub('<[^<]+?>', '',str(plataforma) )
    return [float(price.replace(',','.').replace("R$",'')),title,genre,plataforma,dev]
# print(ibyteextractor(soup))