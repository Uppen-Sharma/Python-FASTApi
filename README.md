<div align="center">
  <h1>📚 FastAPI Books API Project</h1>
  <p>A comprehensive Python <b>FastAPI</b> application demonstrating robust API design, data validation, and CRUD operations.</p>
</div>

---

## 📖 Overview

This repository contains a RESTful **FastAPI** project that manages a collection of books. It is divided into two parts to demonstrate progression from basic to advanced API structure:

1. **`books1.py`**: A foundation application that uses Python dictionaries for in-memory data storage, showcasing simple path parameters and query parameters.
2. **`books2.py`**: An advanced application utilizing **Pydantic** models, data validation, specific HTTP status codes, structured response models, and exception handling (like 404 Not Found).

---

## ✨ Features

- **CRUD Operations**: Complete Create, Read, Update, and Delete capabilities.
- **Data Validation**: Strict request object validation using Pydantic `BaseModel` and `Field`.
- **Path & Query Parameters**: Advanced routing and filtering logic.
- **Status Codes**: Precise HTTP status codes mapping (e.g., `201 Created`, `204 No Content`, `200 OK`).
- **Interactive Documentation**: Out-of-the-box Swagger UI for endpoint testing.
- **Error Handling**: Graceful error handling using standard FastAPI HTTP exceptions.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Uppen-Sharma/Python-FASTApi.git
   cd Python-FASTApi/FastAPI_Books_Project
   ```

2. **Create a virtual environment (Recommended):**
   - Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

---

## 💻 Running the Application

You can run either the basic version or the advanced version of the application.

### Running the Basic API (`books1.py`)

```bash
uvicorn books1:app --reload
```

### Running the Advanced API (`books2.py`)

```bash
uvicorn books2:app --reload
```

> **Note:** The `--reload` flag enables auto-reloading whenever you make changes to your code, which is ideal during development.

---

## 🌐 API Endpoints (Advanced Version - `books2.py`)

Here is an overview of the endpoints available when running `books2.py`.

| Method     | Endpoint                                | Description                         | Status Code                         |
| :--------- | :-------------------------------------- | :---------------------------------- | :---------------------------------- |
| **GET**    | `/books`                                | Retrieve all books.                 | `200 OK`                            |
| **GET**    | `/books/{book_id}`                      | Retrieve a specific book by ID.     | `200 OK` or `404 Not Found`         |
| **GET**    | `/books/?book_rating={rating}`          | Filter books by their rating score. | `200 OK`                            |
| **GET**    | `/books/publish/?published_date={year}` | Filter books by published date.     | `200 OK`                            |
| **POST**   | `/create-book`                          | Create a new book entry.            | `201 Created`                       |
| **PUT**    | `/books/update_book`                    | Update an existing book entry.      | `204 No Content` or `404 Not Found` |
| **DELETE** | `/books/{book_id}`                      | Delete a book by its precise ID.    | `204 No Content` or `404 Not Found` |

### 🧪 API Documentation (Swagger UI)

FastAPI automatically generates interactive API documentation. Once your server is running, navigate to:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

From there, you can view request schemas, required fields, and even submit API requests directly from your browser!

---

## 🛠️ Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used.
- [Uvicorn](https://www.uvicorn.org/) - ASGI web server implementation.
- [Pydantic](https://docs.pydantic.dev/) - Data validation and settings management.

---

<div align="center">
  <i>Happy Coding! 🚀</i>
</div>
