# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend a FastAPI book service so that its data is stored in a SQLite database instead of only in memory. Practice creating database tables, executing parameterized SQL queries, and connecting persistent data to REST endpoints.

## 📝 Tasks

### 🛠️ Initialize the SQLite Database

#### Description

Complete the database setup in the starter code. Create a SQLite database file, define the books table, and seed it with sample records when the table is empty.

#### Requirements

Completed program should:

- Create or open a database file named `books.db`.
- Create a `books` table with columns for an integer ID, title, author, and publication year.
- Use a primary key for the book ID.
- Insert at least two sample books only when the table has no records.
- Keep the database connection logic in a reusable function.

### 🛠️ Connect REST Routes to SQLite

#### Description

Replace the in-memory book operations with SQL queries so that the existing API reads and writes persistent data.

#### Requirements

Completed program should:

- Return all database records from `GET /books` with HTTP status `200`.
- Return one matching record from `GET /books/{book_id}` with HTTP status `200`.
- Return HTTP status `404` when a requested book does not exist.
- Insert a new book with `POST /books` and return the created record with HTTP status `201`.
- Delete a book with `DELETE /books/{book_id}` and return a confirmation response.
- Use parameterized SQL values instead of building queries with string concatenation.

### 🛠️ Add Updates and Persistence Checks

#### Description

Add an update route and verify that changes remain available after the API restarts. Test the completed service through FastAPI’s interactive documentation.

#### Requirements

Completed program should:

- Update an existing book with `PUT /books/{book_id}`.
- Return HTTP status `404` when an update targets a missing book.
- Return HTTP status `422` for requests with missing or invalid book fields.
- Preserve newly created and updated books after stopping and restarting the API.
- Make every route testable from `http://127.0.0.1:8000/docs`.
- Demonstrate one successful request and one missing-book error response.