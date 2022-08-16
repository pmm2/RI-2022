
from ast import If
from bs4 import BeautifulSoup
import re
# import requests
# url = "https://www.kabum.com.br/produto/298373/jogo-elden-ring-xbox"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
#downloaded so the site is fully loaded
with open("/home/pmilet/RI-2022/extractor/specifics/deathloop.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
def fastextractor(html):
    price = html.find("span",  {"class": "value"})
    if hasattr(price,"text"):
        price = price.text.replace(u'\xa0', u'')
    title = html.h1.text
    genre =''
    plataforma =''
    dev=''
    pattern = re.compile(r'^Características',flags=re.IGNORECASE)
    description = html.find("b",string=pattern).parent

    # searchs for genero and desenvolvedor in description
    for d in description:
        if d.__contains__('Gênero:'):
            genre=d.split("Gênero: ")[1]
        if d.__contains__('Plataforma:'):
            plataforma=d.split("Plataforma: ")[1]
        if d.__contains__('Desenvolvedor:'):
            dev=d.split("Desenvolvedor: ")[1]
    return [float(price),title,genre,plataforma,dev]
