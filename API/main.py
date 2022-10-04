from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json
from search import get_docs_len,execute_query

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Consulta(BaseModel):
    simple: Optional[str] = None
    title: Optional[str] = None
    price: Optional[int] = None
    genre: Optional[str] = None
    plataforma: Optional[str] = None
    dev: Optional[str] = None

@app.post('/')
async def consulta(consulta:Consulta):
    data_map = {}
    with open('../data/data_map.json') as infile:
        text = infile.read()
        data_map = json.loads(text)

    qt_docs = len(data_map)
    docs_len = get_docs_len(data_map)
    idsConsulta = execute_query(consulta.simple,consulta.title,consulta.genre,consulta.dev,consulta.plataforma,consulta.price,qt_docs,docs_len)
    retorno = []
    for i in idsConsulta:
       retorno.append(data_map[i]['url'])
    json_string = json.dumps(retorno)
    #retornar json dos resultados
    return json_string