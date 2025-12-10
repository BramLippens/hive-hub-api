# DVD Collection API

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

6. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Access the API documentation at: http://localhost:8000/docs

## Project Structure

```
dvd-collection-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application entry point
│   ├── database.py       # Database connection and session
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   └── crud.py           # Database operations
├── .env.example          # Environment variables template
├── .gitignore
├── docker-compose.yml    # PostgreSQL setup
├── requirements.txt
└── README.md
```

## API Endpoints

- `GET /items/` - List all items
- `GET /items/{item_id}` - Get specific item
- `POST /items/` - Add new item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item
