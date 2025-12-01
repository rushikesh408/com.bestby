from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.product_details import Product_Details
from db.schemas import ProductDetailsCreate, ProductDetailsResponse
from typing import List
from datetime import date


router = APIRouter()


@router.get("/dates/{datefrom}/{dateto}", response_model= List[ProductDetailsResponse])
def get_product_by_id(datefrom:date, dateto:date, db: Session = Depends(get_db)):
        print(datefrom)
        print(dateto)

        product_by_date = db.query(Product_Details).filter(Product_Details.expiry_date>=datefrom).filter(Product_Details.expiry_date<=dateto).all()


        return product_by_date
   
        
