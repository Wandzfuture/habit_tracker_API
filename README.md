# Bookmark Organizer API

A simple web API for managing bookmarks, allowing users to add, view, and delete saved links. Built with Flask and SQLite, this project demonstrates fundamental CRUD (Create, Read, Update, Delete) operations in a REST API format.

## Features

- **Add Bookmarks**: Save a new bookmark with a title, URL, and category.
- **View All Bookmarks**: Retrieve a list of all saved bookmarks.
- **Delete Bookmarks**: Remove a bookmark by its unique ID.

## Project Structure

- **app.py**: Main application file containing the API routes and database connection.
- **bookmarks.db**: SQLite database file storing the bookmarks data.

## Endpoints

### 1. Add a Bookmark

- **Endpoint**: `/bookmarks`
- **Method**: `POST`
- **Request Body** (JSON):
  ```json
  {
    "title": "Example Site",
    "url": "https://example.com",
    "category": "Resources"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Bookmark added!"
  }
  ```

### 2. Retrieve All Bookmarks

- **Endpoint**: `/bookmarks`
- **Method**: `GET`
- **Response** (JSON):
  ```json
  [
    {
      "id": 1,
      "title": "Example Site",
      "url": "https://example.com",
      "category": "Resources"
    },
    ...
  ]
  ```

### 3. Delete a Bookmark

- **Endpoint**: `/bookmarks/<id>`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Bookmark deleted!"
  }
  ```

## Getting Started

### Prerequisites

- **Python 3**: Make sure Python 3 is installed on your system.
- **Flask**: Install Flask by running:
  ```bash
  pip install flask
  ```

### Installation

1. **Clone the repository** (or download the project files).
2. **Navigate to the project directory**:
   ```bash
   cd BookmarkOrganizer
   ```

### Running the Application

1. Start the Flask server:
   ```bash
   python3 app.py
   ```
2. The server will start on `http://127.0.0.1:5000`.

### Testing the API

You can test the API endpoints using `curl` commands or with tools like **Postman** or **Insomnia**.

#### Example `curl` Commands

- **Add a Bookmark**:
  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"title": "Example Site", "url": "https://example.com", "category": "Resources"}' \
  http://127.0.0.1:5000/bookmarks
  ```

- **Retrieve All Bookmarks**:
  ```bash
  curl http://127.0.0.1:5000/bookmarks
  ```

- **Delete a Bookmark**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/bookmarks/1
  ```

## Additional Notes

- The database (`bookmarks.db`) will be created automatically the first time you run the app.
- Ensure the server is running before making any requests to the API.

---

This `README.md` provides a detailed overview and instructions on using and testing your Bookmark Organizer API. Let me know if there’s anything else you’d like to add!
