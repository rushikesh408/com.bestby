from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.product_details import Product_Details
from db.schemas import ProductDetailsCreate, ProductDetailsResponse
from typing import List

router = APIRouter()


@router.get("/allproducts",response_model= List[ProductDetailsResponse])
def get_all_products(db: Session = Depends(get_db)):
    all_products = db.query(Product_Details).all()
    return all_products
