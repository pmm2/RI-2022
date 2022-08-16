from bs4 import BeautifulSoup
import re

# with open("./fifaIbyte.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

# url = "https://www.futuristicgames.com.br/grand-theft-auto-v-standard-edition-rockstar-games-ps3-fisico/p/MLB6084030?pdp_filters=category:MLB1144%7Cseller_id:161960254#position=3&search_layout=grid&type=item&tracking_id=c273642d-2098-4267-aea6-d94dea69e692"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
def generic(html):
    title =''
    plataforma =''
    dev =''
    genre=''
    price=0
    tagspattern = re.compile('<.*?>',flags=re.IGNORECASE)
    htmlaftertitle = html.body.text.split(html.h1.text,1)[1]
    cleanedhtml = re.sub('\s', '', htmlaftertitle)
    testehtml = re.sub(tagspattern,' ',str(html))
    testehtml = re.sub("\s",' ',testehtml)
    title = html.h1.text.strip()
    # print("title:",title)
    # Search for price, if price doesnt contain comma its missing it so divides it by 100
    pattern = re.compile(r'R\$\d+[,|.]?\d*',flags=re.IGNORECASE)
    search = re.findall(pattern,cleanedhtml)
    for s in search:
        # divisor =1
        # # if ',' not in s and '.' not in s:
        # #     divisor =100
        aux_price = float(s.replace("R$",'').replace(',','.').strip())
        if aux_price > price and price ==0:
            price = aux_price
            # print("price : R$",price)
    # Search for genre, its always string right after pattern
    pattern =re.compile(r'[g|G]ênero:?\s*\w*',flags=re.IGNORECASE)
    search = re.search(pattern,html.body.text)
    r =re.compile(r"\w*",flags=re.IGNORECASE)
    cleanedhtml2 = list(filter(r.match,testehtml.split()))
    searchgenre = re.findall(pattern,testehtml)
    pattern = re.compile(r'[g|G]ênero:?\s*',flags=re.IGNORECASE)
    if len(searchgenre)>0 and searchgenre != None :
        genre= re.sub(pattern,'',searchgenre[0].replace(' ',''))

    # Search for plataforma, its always string right after pattern
    pattern = re.compile(r'Plataforma:?',flags=re.IGNORECASE)
    for t in range(len(cleanedhtml2)):
        z = re.match(pattern,cleanedhtml2[t])
        if z:
            plataforma =cleanedhtml2[t+1]
            break
    # print("Plataforma:",plataforma)

    # Search for developer, its always string right after pattern
    pattern = re.compile(r'Desenvolvedor|Marca',flags=re.IGNORECASE)
    for t in range(len(cleanedhtml2)):
        z = re.match(pattern,cleanedhtml2[t])
        if z:
            dev =cleanedhtml2[t+1]
            break
    # print("Dev:",dev)

    return [price,title,genre,plataforma,dev]

# print(generic(soup))