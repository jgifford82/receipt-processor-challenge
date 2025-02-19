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

    points = 0

    for receipt in receipts:
        if receipt.id == id:
            name = []
            for char in receipt.retailer:
                if char.isalnum():
                    name.append(char)

            points += len(name)

            total = float(receipt.total)
            if total.is_integer():
                points += 50

            if total % 0.25 == 0:
                points += 25

            return {"points": points}
    return {"error": "receipt not found"}