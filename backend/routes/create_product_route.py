from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from db.database import get_db
from db.product_details import Product_Details
from db.schemas import ProductDetailsCreate, ProductDetailsResponse


router = APIRouter()


@router.post("/new_product", response_model=ProductDetailsResponse)
def create_new_product(
    product_data: ProductDetailsCreate, db: Session = Depends(get_db)
):
    new_product = Product_Details(
        name=product_data.name,
        remainder=product_data.remainder,
        remindBefore=product_data.remindBefore,
        merchant=product_data.merchant,
        price=product_data.price,
        useremail=product_data.useremail,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
