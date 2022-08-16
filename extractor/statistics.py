from ast import If
import json
import requests
from bs4 import BeautifulSoup
from  specifics.bigboygames import bigboyextractor
from  specifics.vnsgames import vnsextractor
from  specifics.fastshop import fastextractor
from  specifics.futuristicGames import futuristicextractor
from  specifics.lojaarenagames import arenaextractor
from  specifics.shockgames import shockextractor
from  specifics.ibyte import ibyteextractor
from  generic import generic
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.magazineluiza.com.br/fifa-21-para-xbox-one-ea/p/227122100/ga/otga/"
#
def extrair(url,func):
    # req = requests.get(url)
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    specific_ = func(soup)
    generic_ = generic(soup)
    matches =[]
    for s, g in zip(specific_, generic_):
        if type(s) !=float and type(g) !=float:
            if s in g or g in s:
                if s =='' or g =='':
                    if s =='' and g =='':
                        matches.append(True)
                        continue
                    else:
                        matches.append(False)
                        continue
                else:
                    matches.append(True)
            else:
                matches.append(False)
                continue
        elif (s ==g):
            matches.append(True)
            continue
        else:
            matches.append(False)
    with open('/home/pmilet/RI-2022/extractor/statistics.txt', 'w') as txt:
        # txt.write("specific_")
        # txt.write(str(specific_))
        # txt.write("generic_")
        # txt.write(str(generic_))
        # txt.write(str(matches))
        print("specific_")
        print(specific_)
        print("generic")
        print(generic_)
        print(matches)
        print()

with open('/home/pmilet/RI-2022/extractor/data.json') as data_file:
    data = json.load(data_file)
    for v in data.values():
        for url in v:
            if "lojaarenagames" in url:
                extrair(url,arenaextractor)
                # continue
            if "bigboy" in url:
                extrair(url,bigboyextractor)
                # continue
            if "fastshop" in url:
                # extrair(url,fastextractor)
                continue
            if "futuristic" in url:
                # futuristicextractor
                extrair(url,futuristicextractor)
            if "ibyte" in url:
                # ibyteextractor
                extrair(url,ibyteextractor)
                # continue
            if "shockgames" in url:
                # shockextractor
                extrair(url,shockextractor)
            if "vnsgames" in url:
                # vnsextractor
                extrair(url,vnsextractor)


