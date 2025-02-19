from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from typing import Optional

app = FastAPI()

receipts = []

class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    id: Optional[str] = None
    retailer: str
    purchaseDate: str
    purchaseTime: str
    total: str
    items: list[Item]

@app.post("/receipts/process")
def create_receipt_id(receipt: Receipt):
    #print(receipt)
    id_generator = uuid.uuid4()
    receipt.id = id_generator
    receipts.append(receipt)
    print(receipts)
    return {"id": receipts[-1].id}

@app.get("/receipts/{id}/points")
def get_receipt_points(id: str):
    return {"points": 32}