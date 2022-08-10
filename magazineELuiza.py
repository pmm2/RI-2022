from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import requests
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.magazineluiza.com.br/fifa-21-para-xbox-one-ea/p/227122100/ga/otga/"
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
with open("./gow.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

Titulo = soup.h1
print(Titulo.text)
Preco = soup.find("p" ,attrs={'data-testid': 'price-value'})
print(Preco.text)
generoHandler = soup.find("td",string="Gênero")
Genero = generoHandler.findNext("td").findChildren("td",recursive=True)
print(Genero[0].text)
plataformaHandler = soup.find("td",string="Plataforma")
plataforma = plataformaHandler.findNext("td").findChildren("td",recursive=True)
print(plataforma[0].text)
desenvolvedorHandler = soup.find("td",string="Desenvolvedor")
desenvolvedor = desenvolvedorHandler.findNext("td").findChildren("td",recursive=True)
print(desenvolvedor[0].text)