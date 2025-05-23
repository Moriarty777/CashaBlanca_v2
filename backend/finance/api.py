# finance/api.py
from ninja import NinjaAPI
from .models import Transaction
from typing import List
from pydantic import BaseModel
from datetime import date

api = NinjaAPI()

# Response schema
class TransactionOut(BaseModel):
    id: int
    date: date
    type: str
    category: str
    title: str
    amount: float
    notes: str

    class Config:
        orm_mode = True

@api.get("/transactions", response=List[TransactionOut])
def list_transactions(request):
    return Transaction.objects.all()