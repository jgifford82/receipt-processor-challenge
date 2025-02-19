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
def create_receipt_id(receipt: Receipt):
    print(receipt)
    id_generator = uuid.uuid4()
    return {"id": id_generator}

@app.get("/receipts/{id}/points")
def get_receipt_points(id: str):
    return {"points": 32}