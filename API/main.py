from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Consulta(BaseModel):
    title: str
    genre: str
    plataforma: str
    dev: str

@app.post('/')
async def consulta(consulta:Consulta):
    print(consulta)
    #retornar json dos resultados
    return {"status":200}