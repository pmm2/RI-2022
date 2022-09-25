from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
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
    genre: Optional[str] = None
    plataforma: Optional[str] = None
    dev: Optional[str] = None

@app.post('/')
async def consulta(consulta:Consulta):
    print(consulta)
    #retornar json dos resultados
    return {"status":200}