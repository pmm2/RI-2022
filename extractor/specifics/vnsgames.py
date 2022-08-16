from bs4 import BeautifulSoup
import re
# import requests
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# with open("./farcry.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
def vnsextractor(html):
    genre =''
    dev = ''
    price = html.find("span",{'data-app':"product.price"})
    price =re.sub('\s', '', price.text)
    title = html.h1.text
    plataforma = title.split("-")[1].strip()

    # finds description
    description = html.find("div",{"class":"board_htm description"}).text
    # jumps to important part of description
    descriptionHandler = description.split("Idiomas:")[1].split("\n")
    # searchs for genero and desenvolvedor in description
    for d in descriptionHandler:
        if d.__contains__('Gênero:'):
            genre =d.split("Gênero: ")[1]
        if d.__contains__('Desenvolvedor:'):
            dev = d.split("Desenvolvedor: ")[1]
    return [float(price.replace(',','.')),title,genre,plataforma,dev]
