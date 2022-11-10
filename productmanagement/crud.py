from sqlalchemy.orm import Session
from models import Product


def create_product(db: Session, name, brand, price, quantity):
    new_product = Product(name=name, brand=brand, price=price, quantity=quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_product(db: Session, id: int):
    db_product = db.query(Product).filter(Product.id == id).first()
    return db_product


def list_products(db: Session):
    all_products = db.query(Product).all()
    return all_products


def update_product(db: Session, id: int, name: str, brand: str, price: float, quantity: int):
    db_product = get_product(db=db, id=id)
    db_product.name = name
    db_product.brand = brand
    db_product.price = price
    db_product.quantity = quantity
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, id: int):
    db_product = get_product(db=db, id=id)
    db.delete(db_product)
    db.commit()
