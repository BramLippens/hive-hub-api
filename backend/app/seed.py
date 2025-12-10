"""
Seed script to populate the database with sample data.
Run with: python -m app.seed
"""

from app.database import SessionLocal
from app.models import CollectionItem, MediaType


def seed_data():
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_count = db.query(CollectionItem).count()
        if existing_count > 0:
            print(f"Database already has {existing_count} items. Skipping seed.")
            return
        
        # Sample DVD data
        sample_items = [
            CollectionItem(
                title="The Matrix",
                media_type=MediaType.DVD,
                genre="Sci-Fi",
                year=1999,
                director="The Wachowskis",
                notes="Classic cyberpunk film"
            ),
            CollectionItem(
                title="Inception",
                media_type=MediaType.BLURAY,
                genre="Thriller",
                year=2010,
                director="Christopher Nolan",
                notes="Mind-bending heist movie"
            ),
            CollectionItem(
                title="The Dark Knight",
                media_type=MediaType.DVD,
                genre="Action",
                year=2008,
                director="Christopher Nolan",
                notes="Best Batman film"
            ),
            CollectionItem(
                title="Abbey Road",
                media_type=MediaType.CD,
                genre="Rock",
                year=1969,
                artist="The Beatles",
                notes="Iconic album with Come Together"
            ),
            CollectionItem(
                title="Thriller",
                media_type=MediaType.CD,
                genre="Pop",
                year=1982,
                artist="Michael Jackson",
                notes="Best-selling album of all time"
            ),
            CollectionItem(
                title="The Shawshank Redemption",
                media_type=MediaType.BLURAY,
                genre="Drama",
                year=1994,
                director="Frank Darabont",
                notes="Highly rated prison drama"
            ),
            CollectionItem(
                title="Pulp Fiction",
                media_type=MediaType.DVD,
                genre="Crime",
                year=1994,
                director="Quentin Tarantino",
                notes="Non-linear storytelling masterpiece"
            ),
            CollectionItem(
                title="Dark Side of the Moon",
                media_type=MediaType.CD,
                genre="Progressive Rock",
                year=1973,
                artist="Pink Floyd",
                notes="Legendary concept album"
            ),
        ]
        
        # Add all items to database
        db.add_all(sample_items)
        db.commit()
        
        print(f"Successfully seeded {len(sample_items)} items into the database!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
