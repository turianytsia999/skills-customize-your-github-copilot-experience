# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI for managing a collection of books. Practice defining API routes, accepting JSON request data, returning structured responses, and handling common HTTP errors.

## 📝 Tasks

### 🛠️ Define the Book Data Model

#### Description

Complete the starter code by defining the data structure used for books and creating an in-memory collection of sample books. Use a Pydantic model so FastAPI can validate incoming JSON data.

#### Requirements

Completed program should:

- Define a `Book` model with an integer `id`, a string `title`, a string `author`, and an integer `year`.
- Create an in-memory list containing at least two sample books.
- Start successfully with `uvicorn starter-code:app --reload` after FastAPI and Uvicorn are installed.

### 🛠️ Add Book API Routes

#### Description

Implement REST endpoints that allow a client to list all books, retrieve one book by ID, create a book, and delete a book.

#### Requirements

Completed program should:

- Return all books from `GET /books` with HTTP status `200`.
- Return one matching book from `GET /books/{book_id}` with HTTP status `200`.
- Return HTTP status `404` from `GET /books/{book_id}` when the ID does not exist.
- Add a new book from `POST /books` and return the created book with HTTP status `201`.
- Delete a matching book from `DELETE /books/{book_id}` and return a confirmation response.
- Return HTTP status `404` when a delete request targets a missing book.

### 🛠️ Validate Requests and Test the API

#### Description

Improve the API’s reliability by validating book data and testing each route with the automatically generated FastAPI documentation.

#### Requirements

Completed program should:

- Reject requests with a missing or invalid `title`, `author`, or `year` value.
- Require `year` to be a positive integer.
- Return JSON responses with clear messages for missing books and invalid requests.
- Make every route testable from `http://127.0.0.1:8000/docs`.
- Demonstrate at least one successful request and one error response in the student’s submission notes or terminal output.