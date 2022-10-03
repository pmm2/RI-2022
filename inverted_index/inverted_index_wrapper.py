import json
import numpy

from .inverted_index import invertedIndex, clean

def pick_quartis(price_list):
    q1 = numpy.quantile(price_list, q=0.25)
    q2 = numpy.quantile(price_list, q=0.5)
    q3 = numpy.quantile(price_list, q=0.75)
    q4 = numpy.quantile(price_list, q=1)
    return [q1, q2, q3, q4]

def p_quatis(quatis, val):
    if val < float(quatis[0]):
        return float(quatis[0])
    if val < float(quatis[1]):
        return float(quatis[1])
    if val < float(quatis[2]):
        return float(quatis[2])
    else:
        return float(quatis[3])

def convert_to_float(val):
    price = val.split()
    price = price[1].replace(',', '.')
    return float(price)

def get_prices_lists(data):
    prices = []
    for i in data:
        if data[i]['price'] != "None":
            if type(data[i]['price']) == str:
                prices.append(convert_to_float(data[i]['price']))

            else:
                prices.append(data[i]['price'])

    prices = sorted(prices)
    return prices

def tag(s, tag):
    cleaned = [f"{clean(i)}" for i in s if i != 'None']
    tagged = [f"{i}-{tag}" for i in cleaned if len(i) > 0]
    return tagged

def create_field_invindex():
    f = open('./data/data_map.json')
    data = json.load(f)
    documentos = []
    quatis = pick_quartis(get_prices_lists(data))

    for i in data:
        titleList = tag(data[i]['title'].split(), 'title')
        genreList = tag(data[i]['genre'].split(), 'genre')
        plataformaList = tag(data[i]['plataforma'].split(), 'plataforma')
        devList = tag(data[i]['dev'].split(), 'dev')
        price = data[i]['price']
        priceList = []
        if price != 'None':
            if type(price) == str:
                price = convert_to_float(price)
            priceList = tag(str(p_quatis(quatis, price)), 'price')
        docList = titleList+genreList+plataformaList+devList+priceList
        documentos.append(docList)
    f.close()

    ii = invertedIndex(documentos)
    ii.createInvertedIndex()
    inv_list = json.dumps(ii.vocabulary)
    with open('./inverted_index/fields_invindex.json', 'w') as outfile:
        outfile.write(inv_list)

def create_general_invidex():
    f = open('./data/data_map.json')
    data = json.load(f)
    documentos = []
    quatis = pick_quartis(get_prices_lists(data))

    for i in data:
        titleList = [clean(i) for i in data[i]['title'].split() if i != 'None']
        genreList = [clean(i) for i in data[i]['genre'].split() if i != 'None']
        plataformaList = [clean(i) for i in data[i]
                          ['plataforma'].split() if i != 'None']
        devList = [clean(i) for i in data[i]['dev'].split() if i != 'None']
        price = data[i]['price']
        priceList = []
        if price != 'None':
            if type(price) == str:
                price = convert_to_float(price)
            priceList = [str(p_quatis(quatis, price))]
        docList = titleList+genreList+plataformaList+devList+priceList
        documentos.append(docList)
    f.close()

    ii = invertedIndex(documentos)
    ii.createInvertedIndex()
    inv_list = json.dumps(ii.vocabulary)
    with open('./inverted_index/geral_invindex.json', 'w') as outfile:
        outfile.write(inv_list)

create_field_invindex()
create_general_invidex()