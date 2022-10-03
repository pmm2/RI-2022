from ast import operator
from asyncore import file_dispatcher
from email.encoders import encode_noop
import json
from nis import match
from pydoc import doc
from bs4 import BeautifulSoup
from typing_extensions import IntVar
from nltk.corpus import stopwords
from operator import ge
from math import log
import unidecode
import os
import re


def execute_query(query_string, title, gen, dev, plat, price, num_docs, docs_lenght, tfidf=True, n=5):

    games_list = []
    if query_string != '':

        games = run_query(query_string, tfidf, num_docs, docs_lenght, n)
        games_list.append(games)

    if title != '':

        games = run_query(title, tfidf, num_docs,
                          docs_lenght, n, field='title')
        games_list.append(games)

    if gen != '':

        games = run_query(
            gen, tfidf, num_docs, docs_lenght, n, field='gen')
        games_list.append(games)

    if dev != '':

        games = run_query(
            dev, tfidf, num_docs, docs_lenght, n, field='dev')
        games_list.append(games)

    if plat != '':

        games = run_query(
            plat, tfidf, num_docs, docs_lenght, n, field='plat')
        games_list.append(games)

    if price != '':

        games = run_query(
            price, tfidf, num_docs, docs_lenght, n, field='price')
        games_list.append(games)

    all_games = {}

    for ranks_list in games_list:
        for game in ranks_list:
            if not str(game[0]) in all_games:
                all_games[str(game[0])] = float(game[1])
            else:
                all_games[str(game[0])] += float(game[1])
    for doc in all_games:
        all_games[doc] /= 6

    return sorted(all_games.items(), key=operator.itemgetter(1), reverse=True)


# calcular no começo de tudo
def get_docs_len(docs_path_map='./data/data_map.json'):
    lengths = {}
    with open(docs_path_map, 'r') as map:
        map_docs = map.read()
        map_docs = json.loads(map_docs)
    for id in map_docs:
        with open(f"./data/htmls/{map_docs[id]['arquivo']}.html") as html:
            lengths[id] = len(BeautifulSoup(
                html.read(), 'html.parser').text.split(' '))
    return lengths


def cosine_Score(terms, tfidf, invlist, num_docs, doc_lengths, n):
    scores = {i: 0 for i in range(1, num_docs + 1)}
    for term in terms:

        w_term_query = term.count(term)
        if (tfidf):
            w_term_query = 0.5 + 0.5 * \
                (w_term_query /
                 max([i for i, val in enumerate(terms) if val == term])+1)
            w_term_query *= get_idf(invlist[term], num_docs)
        for post in term:
            w_doc_term = post[1]  # tf
            if tfidf:
                w_doc_term *= get_idf(invlist[term], num_docs)
            scores[post[0]] += w_term_query * w_doc_term
    for d in range(1, num_docs + 1):
        scores[d] /= doc_lengths[d]
    scores = sorted(scores.items, key=lambda x: x[1], reverse=True)
    return scores[:n]


def clear_query_input(query, field=None, usestopwords=False):

    if type(query) == str:
        substr = re.findall(r'"(.*?)"', query)
        words = re.sub(r'"(.*?)"', '', query)
        words = words.lower().strip().split(' ')
        words = words + substr

    toRemove = r'[.*,;\(\)\'\"\?\!%\$]'

    for i in range(len(words)):
        words[i] = re.sub(toRemove, '', words[i])
        words[i] = unidecode.unidecode(words[i])

    if usestopwords:
        set_sw = set(stopwords.words('english'))
        newWords = []
        for word in words:
            if not word in set_sw:
                if (field):
                    newWords.append(word + '.' + field)
                else:
                    newWords.append(word)
        return list(set(newWords))
    if (field):
        for i in range(len(words)):
            words[i] = words[i] + '-' + field
    return list(set(words))


def get_idf(posting, num_docs):

    idf = log(num_docs/len(posting))
    return idf


def get_invindex(path='./inverted_index/invIndex.json'):
    with open(path, 'r') as file:
        text = file.read()
        invindex = json.loads(text)
    return invindex


def run_query(query, tfidf, num_docs, docs_lenght, n, field=None, invlist_path='./inverted_index/invIndex.json'):
    terms = clear_query_input(query, field)
    invindex = get_invindex(invlist_path)
    return cosine_Score(terms, tfidf, invindex, num_docs, docs_lenght, n)
