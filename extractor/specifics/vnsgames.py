from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import requests
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.vnsgames.com.br/ps4/acao/horizon-forbidden-west-ps4"
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
with open("./farcry.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
price = soup.find("span",{'class':"preco-avista precoAvista"})

print(re.sub('\s', '', price.text))
title = soup.h1
print(title.text)
plataforma = title.text.split("-")[1].strip()
print(plataforma)
# finds description
description = soup.find("p",{"class":"MsoNormal"}).text
# jumps to important part of description
descriptionHandler = description.split("Idiomas:")[1].split("\n")
# searchs for genero and desenvolvedor in description
for d in descriptionHandler:
    if d.__contains__('Gênero:'):
        print(d.split("Gênero: ")[1])
    if d.__contains__('Desenvolvedor:'):
        print(d.split("Desenvolvedor: ")[1])
