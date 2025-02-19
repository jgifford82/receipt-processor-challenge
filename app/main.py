from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()


class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    total: str
    items: list[Item]

@app.post("/receipts/process")
def root(receipt: Receipt):
    print(receipt)
    id_generator = uuid.uuid4()
    return {"id": id_generator}