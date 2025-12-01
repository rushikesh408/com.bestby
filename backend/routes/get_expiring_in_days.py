from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.product_details import Product_Details
from db.schemas import ProductDetailsCreate, ProductDetailsResponse
from typing import List
from datetime import date, timedelta


router = APIRouter()

@router.get("/days/{days}", response_model=List[ProductDetailsResponse])
def products_expiringin(days:int,  db: Session = Depends(get_db)):
    expiring_in = date.today() + timedelta(days=days)
    print(expiring_in)
    expiring_in_days_records = db.query(Product_Details).filter(Product_Details.expiry_date>=date.today()).filter(Product_Details.expiry_date<=expiring_in).all()
    return expiring_in_days_records