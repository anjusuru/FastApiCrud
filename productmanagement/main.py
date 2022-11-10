from fastapi import FastAPI, status, Depends
import models
from db import SessionLocal, engine
from sqlalchemy.orm import Session
import crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.get("/list_products")
def list_products(db: Session = Depends(get_db)):
    product_list = crud.list_products(db=db)
    return product_list


@app.post("/create_product", status_code=status.HTTP_201_CREATED)
def create_product(name: str, brand: str, price: float, quantity: int, db: Session = Depends(get_db)):
    product = crud.create_product(db=db, name=name, brand=brand, price=price, quantity=quantity)

    return {"product": product}


@app.get("/get_product/{id}/")  # id is a path parameter
def get_product(id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db=db, id=id)
    return product


@app.put("/update_product/{id}/")  # id is a path parameter
def update_product(id: int, name: str, brand: str, price: float, quantity: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, id=id)

    if db_product:
        updated_product = crud.update_product(db=db, id=id, name=name, brand=brand, price=price, quantity=quantity)
        return updated_product
    else:
        return {"error": "Product with id {id} does not exist"}


@app.delete("/delete_product/{id}/")  # id is a path parameter
def delete_friend(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, id=id)
    # check if friend object exists
    if db_product:
        return crud.delete_product(db=db, id=id)
    else:
        return {"error": f"Product with id {id} does not exist"}
