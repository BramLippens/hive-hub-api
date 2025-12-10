from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional


def get_item(db: Session, item_id: int) -> Optional[models.CollectionItem]:
    return db.query(models.CollectionItem).filter(models.CollectionItem.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CollectionItem).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.CollectionItemCreate) -> models.CollectionItem:
    db_item = models.CollectionItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: schemas.CollectionItemUpdate) -> Optional[models.CollectionItem]:
    db_item = get_item(db, item_id)
    if db_item is None:
        return None
    
    update_data = item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> bool:
    db_item = get_item(db, item_id)
    if db_item is None:
        return False
    
    db.delete(db_item)
    db.commit()
    return True
