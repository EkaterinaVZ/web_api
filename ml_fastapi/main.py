from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


unmarked = pipeline("fill-mask", model="albert-base-v2")


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "All right, there is a connection."}


@app.post("/predict/")
def predict(item: Item):
    """Предварительно подготовленная модель на английском языке.
    Вместо [MASK] моделирует(подбирает) слово.
    Источник - https://huggingface.co/albert-base-
    Примеры фраз:  I study economics at [MASK]., I like apples and  pears., My friend often tr>
    I always get up at 8 o’clock in the morning., We have a flat in London., He plays football>
    She sometimes listens to the radio"""
    
    return unmarked(item.text)[0]["sequence"]
