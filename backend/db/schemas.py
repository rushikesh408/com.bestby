from pydantic import BaseModel
from datetime import date, datetime
import uuid



class ProductDetailsCreate(BaseModel):
    name: str
    expiry_date : date
    remainder: bool
    remindBefore: int
    merchant: str
    price: float
    useremail: str


class ProductDetailsResponse(BaseModel):
    id: int
    name: str
    updated_at : datetime
    expiry_date : date
    remainder: int
    remindBefore: int
    merchant: str
    price: float
    # product_uuid :uuid
    useremail: str

    class Config:
        orm_mode = True


# this is a schema
#  schemas are needed for apivalidation, what data we accept from the user, what data we return
# this is used for request and response and not for the database


#  why dont we use models directly? models doest support validation, as in models just describe a table
