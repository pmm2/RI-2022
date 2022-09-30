from ast import If
import json
import requests
from bs4 import BeautifulSoup
from .specifics.bigboygames import bigboyextractor
from .specifics.vnsgames import vnsextractor
from .specifics.futuristicGames import futuristicextractor
from .specifics.lojaarenagames import arenaextractor
from .specifics.shockgames import shockextractor
from .specifics.ibyte import ibyteextractor
from .specifics.shopb import shopbextractor
from .generic import generic


def extractor(url, html):
    soup = BeautifulSoup(html, 'html.parser')
    if "bigboy" in url:
        return bigboyextractor(soup)
    if "ibyte" in url:
        # ibyteextractor
        return ibyteextractor(soup)
        # continue
    # if "mercadolivre" in url:
    #     return mercadolivreextractor(url)
    if "shockgames" in url:
        # vnsextractor
        return shockextractor(soup)
    if "shopb" in url:
        # vnsextractor
        return shopbextractor(soup)
    if "vnsgames" in url:
        # vnsextractor
        return vnsextractor(soup)
