from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    brand: str
    price :float
    quantity: int