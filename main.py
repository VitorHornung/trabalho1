from random import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/devops")
def read_root():
    return {"Olá, Mundo da Programação!"}

@app.get("/formativa")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}