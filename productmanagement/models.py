from sqlalchemy import Column, Integer, String, Float
from db import Base


# model/table
class Product(Base):
    __tablename__ = "Product"

    # fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    brand = Column(String(20))
    price = Column(Float)
    quantity = Column(Integer)
