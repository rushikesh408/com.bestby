from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db.database import Base


class Product_Details(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    expiry_date = Column(Date)
    remainder = Column(Boolean, default=True)
    remindBefore = Column(Integer)
    merchant = Column(String)
    price = Column(Integer)
    product_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    useremail = Column(String(100), unique=True, nullable=False)

    # this is a product_Details model and models are just a table structure
