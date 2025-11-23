from pydantic import BaseModel


class ProductDetailsCreate(BaseModel):
    name: str
    # expiry_date : date
    remainder: bool
    remindBefore: int
    merchant: str
    price: int
    useremail: str


class ProductDetailsResponse(BaseModel):
    id: int
    name: str
    # updated_at : Date
    # expiry_date = Column(Date)
    remainder: int
    remindBefore: int
    merchant: str
    price: bool
    # product_uuid :
    useremail: str

    class Config:
        orm_mode = True


# this is a schema
#  schemas are needed for apivalidation, what data we accept from the user, what data we return
# this is used for request and response and not for the database


#  why dont we use models directly? models doest support validation, as in models just describe a table
