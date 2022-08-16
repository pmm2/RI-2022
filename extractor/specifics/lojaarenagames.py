from bs4 import BeautifulSoup
import re
# import requests
# url = "https://lojaarenagames.com.br/far-cry-4-ps4-playstation-hits/"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
def arenaextractor(html):
    price = html.find_all("span",{'class':'woocommerce-Price-amount amount'})[2].text
    price = re.search(r'\d+,\d+',price)[0]
    title = html.h1
    if hasattr(title,"text"):
        title = title.text.replace('\n','')

    genre = html.find("span",string="\nGênero ")
    if hasattr(genre,"parent"):
        genre = genre.parent.findNext('td').text.strip()
    plataforma = html.find("span",string="\nCategoria ")
    if hasattr(plataforma,"parent"):
        plataforma = plataforma.parent.findNext('td').text.strip()
    dev = html.find("span",string="\nMarca ")
    if hasattr(dev,"parent"):
        dev = dev.parent.findNext('td').text.strip()
    return [float(price.replace(',','.')),title,genre,plataforma,dev]