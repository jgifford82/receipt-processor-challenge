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
    id_generator = uuid.uuid4()
    receipt.id = str(id_generator)
    receipts.append(receipt)
    return {"id": receipts[-1].id}

@app.get("/receipts/{id}/points")
def get_receipt_points(id: str):
   return {"points": 32}