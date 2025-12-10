# Example API Usage

## Using curl

### Add a DVD
```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Matrix",
    "media_type": "DVD",
    "genre": "Sci-Fi",
    "year": 1999,
    "director": "The Wachowskis"
  }'
```

### Get all items
```bash
curl "http://localhost:8000/items/"
```

### Get specific item
```bash
curl "http://localhost:8000/items/1"
```

### Update an item
```bash
curl -X PUT "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{
    "notes": "Great movie, watched multiple times"
  }'
```

### Delete an item
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

## Using the interactive docs

Visit http://localhost:8000/docs to use the Swagger UI interface where you can test all endpoints directly in your browser.
