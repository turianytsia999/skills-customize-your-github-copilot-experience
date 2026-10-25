import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


DATABASE_PATH = "books.db"
app = FastAPI(title="Persistent Book Library API")


class Book(BaseModel):
    title: str
    author: str
    year: int


def get_connection():
    """Open a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Create the books table and add starter records if needed."""
    pass


@app.on_event("startup")
def startup():
    initialize_database()


@app.get("/books")
def list_books():
    """Return every book in the database."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID."""
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    """Save a new book in the database."""
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    """Update an existing book."""
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete one book by ID."""
    pass