from asyncore import read
from re import L, sub
import re
import pprint
import json
import numpy
pp = pprint.PrettyPrinter(indent=4)


def clean(doc):
    doc = re.sub(r'[\W_]+', '', doc)
    doc = doc.strip().lower()
    return doc

def pick_quartis(price_list):
    q1 = numpy.quantile(price_list, q=0.25)
    q2 = numpy.quantile(price_list, q=0.5)
    q3 = numpy.quantile(price_list, q=0.75)

# print(clean("I-like-bananas - "))

class invertedIndex:

    def __init__(self, documents):
        self.vocabulary = dict()
        self.frequency = []
        self.documents = documents
        return

    def countWords(self, docIndex, word, occurences):

        if word not in self.vocabulary:
            self.vocabulary.update({word: []})
            self.vocabulary[word].append([docIndex, occurences])


        else:
            self.vocabulary[word].append([docIndex, occurences])


    def indexCompression(self):

        for entry in self.vocabulary.keys():
            # x[0] pois é o index x[1] é as ocorrencias
            j = [x[0] for x in self.vocabulary[entry]]
            # primeiro indice + restante dos indices aplicados a compressao onde indice = indice - soma dos indices passados
            l = j[:1]+list(map(lambda x: x-j[j.index(x)-1], j[1:]))
            # substitui
            for index in range(len(self.vocabulary[entry])):
                self.vocabulary[entry][index][0] = l[index]

    def createInvertedIndex(self):

        docIndex = 1
        for document in self.documents:

            for word in set(document):
                self.countWords(docIndex=docIndex, word=word,
                                occurences=document.count(word))

            docIndex += 1

        self.frequency = [(v, len(self.vocabulary[v]))
                          for v in self.vocabulary.keys()]


# teste = []
# p = 'I like Bananas120102'
# teste.append(len(p.lower().strip().split(' ')))

# pag1 = 'To pedro to Rato To'.split()
# pag2 = 'to pedro Rato rato To TO'.split()
# pag3 = 'I  rato think therefore I am Do be do be do'.split()
# pag4 = 'Do pedro rato rato rato do do da da da Let it be let it be'.split()
# ii = invertedIndex([pag1, pag2, pag3, pag4])
# ii.createInvertedIndex()
# pp.pprint(ii.vocabulary)
# pp.pprint(ii.frequency)
# ii.indexCompression()

# pp.pprint(ii.vocabulary)
f = open('./data/data_map.json')
data = json.load(f)
documentos = []
def tag (s,tag):
    cleaned = [ f"{clean(i)}" for i in s if i != 'None']
    tagged = [ f"{i}.{tag}" for i in cleaned if len(i)>0]
    return tagged
for i in data:
    doc = []
    titleList = tag(data[i]['title'].split(),'title')
    genreList = tag(data[i]['genre'].split(),'genre')
    plataformaList = tag(data[i]['plataforma'].split(),'plataforma')
    devList = tag(data[i]['dev'].split(),'dev')
    docList =titleList+genreList+plataformaList+devList
    documentos.append(docList)
f.close()

ii = invertedIndex(documentos)
ii.createInvertedIndex()
pp.pprint(ii.vocabulary)