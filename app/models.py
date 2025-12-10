from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func
import enum
from .database import Base


class MediaType(str, enum.Enum):
    DVD = "DVD"
    CD = "CD"
    BLURAY = "Blu-ray"


class CollectionItem(Base):
    __tablename__ = "collection_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    media_type = Column(Enum(MediaType), nullable=False)
    genre = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    director = Column(String, nullable=True)  # For movies
    artist = Column(String, nullable=True)    # For music
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
