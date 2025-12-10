from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DVD Collection API",
    description="A REST API for managing a DVD/CD collection",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "DVD Collection API - visit /docs for API documentation"}


@app.get("/items/", response_model=List[schemas.CollectionItem])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all items in the collection"""
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}", response_model=schemas.CollectionItem)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID"""
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.post("/items/", response_model=schemas.CollectionItem, status_code=201)
def create_item(item: schemas.CollectionItemCreate, db: Session = Depends(get_db)):
    """Add a new item to the collection"""
    return crud.create_item(db=db, item=item)


@app.put("/items/{item_id}", response_model=schemas.CollectionItem)
def update_item(item_id: int, item: schemas.CollectionItemUpdate, db: Session = Depends(get_db)):
    """Update an existing item"""
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item from the collection"""
    success = crud.delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
