# https://testdriven.io/blog/fastapi-postgres-websockets/

from datetime import datetime, date

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import Base


class ProductBase(BaseModel):
    name: str
    remindBefore: int
    expiry_date: date


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    expiry_date: date


class ProductResponse(ProductBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True
