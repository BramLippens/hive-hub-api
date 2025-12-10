# Hive Hub API

A REST API for managing a DVD/CD collection built with FastAPI, SQLAlchemy, and PostgreSQL.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and configure your database settings

5. Start PostgreSQL (using Docker):
   ```bash
   docker-compose up -d
   ```

6. Run database migrations:
   ```bash
   # Create initial migration
   alembic revision --autogenerate -m "Initial migration"
   
   # Apply migrations
   alembic upgrade head
   ```

7. (Optional) Seed the database with sample data:
   ```bash
   python -m app.seed
   ```

8. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

9. Access the API documentation at: http://localhost:8000/docs

## Project Structure

```
hive-hub-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application entry point
│   ├── database.py       # Database connection and session
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   └── seed.py           # Database seeding script
├── alembic/
│   ├── versions/         # Migration files
│   ├── env.py           # Alembic environment config
│   └── script.py.mako   # Migration template
├── .env.example          # Environment variables template
├── .gitignore
├── alembic.ini          # Alembic configuration
├── docker-compose.yml    # PostgreSQL setup
├── requirements.txt
└── README.md
```

## Database Migrations

### Create a new migration
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback last migration
```bash
alembic downgrade -1
```

### View migration history
```bash
alembic history
```

### Reset database (drop all tables and rerun migrations)
```bash
alembic downgrade base
alembic upgrade head
python -m app.seed
```

## API Endpoints

- `GET /items/` - List all items
- `GET /items/{item_id}` - Get specific item
- `POST /items/` - Add new item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item

## Development

The API runs with auto-reload enabled, so code changes will automatically restart the server.

To stop the PostgreSQL container:
```bash
docker-compose down
```

To view PostgreSQL logs:
```bash
docker-compose logs postgres
```
