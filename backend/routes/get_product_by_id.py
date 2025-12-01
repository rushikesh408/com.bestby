from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.product_details import Product_Details
from db.schemas import ProductDetailsCreate, ProductDetailsResponse
from typing import List


router = APIRouter()



@router.get("/{id}", response_model=ProductDetailsResponse)
def get_product_by_id(id:int,  db: Session = Depends(get_db)):
   
     product_by_id = db.query(Product_Details).filter_by(id=id).first()
     if(product_by_id == None):
        print(product_by_id)
        raise HTTPException(status_code=400,detail='bad request')
     return product_by_id
