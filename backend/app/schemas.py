from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from .models import MediaType


class CollectionItemBase(BaseModel):
    title: str
    media_type: MediaType
    genre: Optional[str] = None
    year: Optional[int] = None
    director: Optional[str] = None
    artist: Optional[str] = None
    notes: Optional[str] = None


class CollectionItemCreate(CollectionItemBase):
    pass


class CollectionItemUpdate(BaseModel):
    title: Optional[str] = None
    media_type: Optional[MediaType] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    director: Optional[str] = None
    artist: Optional[str] = None
    notes: Optional[str] = None


class CollectionItemResponse(CollectionItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
