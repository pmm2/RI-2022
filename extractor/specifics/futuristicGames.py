from bs4 import BeautifulSoup
import re
# import requests
# url = "https://www.futuristicgames.com.br/grand-theft-auto-v-standard-edition-rockstar-games-ps3-fisico/p/MLB6084030?pdp_filters=category:MLB1144%7Cseller_id:161960254#position=3&search_layout=grid&type=item&tracking_id=c273642d-2098-4267-aea6-d94dea69e692"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
def futuristicextractor(html):
    price = html.find("span",  {"class": "andes-money-amount__fraction"})
    if hasattr(price,"text"):
        price = price.text.strip()
    title = html.h1.text
    pattern = re.compile(r'^Gênero:',flags=re.IGNORECASE)
    genre = html.find("li", string=pattern)
    if hasattr(genre,"text"):
        genre = genre.text.split("Gênero: ")[1]
    plataforma = html.find("span",  {"id": "picker-label-VIDEO_GAME_PLATFORM"})
    if hasattr(plataforma,"text"):
        plataforma = plataforma.text
    pattern = re.compile(r'^Desenvolvido por',flags=re.IGNORECASE)
    dev = html.find("li", string=pattern)
    if hasattr(dev,"text"):
        dev = dev.text.split("Desenvolvido por ")[1]
    return [float(price.replace(',','.')),title,genre,plataforma,dev]