# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI starter/learning project demonstrating multiple database integration patterns. The codebase contains multiple example implementations showcasing different approaches:

- **main.py** - Current MongoDB implementation (uses pymongo)
- **main_sqllite.py** - SQLite implementation (uses SQLAlchemy ORM)
- **main_o.py** - Original example with custom exception handlers
- **router_example.py** - Demonstrates APIRouter usage for modular route organization

## Architecture

### Database Patterns

The project demonstrates two database approaches in separate modules:

1. **NoSQL (MongoDB)** - `nosql_example/database.py`
   - Uses `pymongo` for direct MongoDB access
   - Connection string with authentication
   - Collection-based operations (insert_one, find)

2. **SQL (SQLite)** - `sql_example/database.py`
   - Uses SQLAlchemy ORM with declarative base
   - Session-based pattern with dependency injection
   - Uses `DeclarativeBase`, `Mapped`, and `mapped_column` for modern SQLAlchemy

### File Organization

```
nosql_example/     # MongoDB database module
sql_example/       # SQLite/SQLAlchemy database module
models.py          # Pydantic models for validation
main*.py           # Various example implementations
router_example.py  # APIRouter example
```

## Common Commands

### Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run with uvicorn (standard)
uvicorn main:app --reload

# Run SQLite version
uvicorn main_sqllite:app --reload

# Run original example
uvicorn main_o:app --reload
```

### Database Files

- SQLite database: `test.db` (created automatically, gitignored)
- MongoDB connection configured in `nosql_example/database.py`

## Code Patterns

### Dependency Injection for Database Sessions

The SQLite example uses FastAPI's dependency injection:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Usage in endpoints
db: Session = Depends(get_db)
```

### Pydantic Model Inheritance

Used for response models with additional fields (like auto-generated IDs):

```python
class User(BaseModel):
    name: str
    email: str

class UserResponse(User):
    id: str  # Added for response
```

### Exception Handling

The original example (`main_o.py`) demonstrates custom exception handlers for `HTTPException` and `RequestValidationError`. Use these patterns for consistent error responses.

## Important Notes

- When unpacking dictionaries for Pydantic models, use `**model_dump()` not `*model_dump()`
- MongoDB ObjectId must be converted to string for JSON responses: `str(result.inserted_id)`
- SQLite requires `connect_args={"check_same_thread": False}` for FastAPI
- Database credentials are currently hardcoded in `nosql_example/database.py` - should be moved to environment variables for production
