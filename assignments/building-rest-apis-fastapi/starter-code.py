from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Book Library API")


class Book(BaseModel):
    """A book stored by the API."""

    pass


books = []


@app.get("/books")
def list_books():
    """Return every book in the library."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID."""
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    """Add a book to the library."""
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete one book by ID."""
    pass