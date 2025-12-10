# Migration & Seeding Guide

## Initial Setup

After setting up your project for the first time:

1. **Install dependencies** (including alembic):
   ```bash
   pip install -r requirements.txt
   ```

2. **Start PostgreSQL**:
   ```bash
   docker-compose up -d
   ```

3. **Create initial migration**:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```
   This will create a migration file in `alembic/versions/` with all your models.

4. **Apply the migration**:
   ```bash
   alembic upgrade head
   ```

5. **Seed the database** (optional):
   ```bash
   python -m app.seed
   ```

## Common Migration Tasks

### Adding a new field to a model

1. Add the field to your model in `app/models.py`:
   ```python
   location = Column(String, nullable=True)  # e.g., shelf location
   ```

2. Create a migration:
   ```bash
   alembic revision --autogenerate -m "Add location field"
   ```

3. Apply the migration:
   ```bash
   alembic upgrade head
   ```

### Viewing migration history

```bash
alembic history
```

### Checking current migration version

```bash
alembic current
```

### Rolling back migrations

Rollback one migration:
```bash
alembic downgrade -1
```

Rollback to a specific revision:
```bash
alembic downgrade <revision_id>
```

Rollback all migrations:
```bash
alembic downgrade base
```

### Resetting the database

If you want to start fresh:

```bash
# Rollback all migrations
alembic downgrade base

# Reapply all migrations
alembic upgrade head

# Reseed the database
python -m app.seed
```

## Seeding

The seed script (`app/seed.py`) includes sample data for development. You can modify it to add your own test data.

To run seeding:
```bash
python -m app.seed
```

The script checks if data already exists before seeding to avoid duplicates.

## Tips

- Always create a migration after changing models
- Review the generated migration file before applying it
- Alembic autogenerate is smart but not perfect - always check the generated SQL
- Keep migrations small and focused on one change
- Commit migration files to version control
