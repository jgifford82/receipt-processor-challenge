from fastapi import FastAPI
from pydantic import BaseModel

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


# @app.get("/")
# def root():
#     return {"message": "Hello World"}

@app.post("/receipts/process")
def root(receipt: Receipt):
    return {"message": "receipts/process"}