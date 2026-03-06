from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

# --- Internal Data Structure ---
class Book:
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# --- Request Validator ---
class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author One', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author Two', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author Three', 'Book Description', 1, 2026)
]

# --- GET: Status 200 OK ---
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

# --- GET by ID: Status 200 or 404 ---
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    # If the loop finishes without returning, raise 404
    raise HTTPException(status_code=404, detail='Item not found')

# --- GET by Rating: Status 200 ---
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    return [book for book in BOOKS if book.rating == book_rating]

# --- GET by Date: Status 200 ---
@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    return [book for book in BOOKS if book.published_date == published_date]

# --- POST: Status 201 Created ---
@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    # No return statement needed for 201 in this specific course example, 
    # or you can return the object if you prefer. 

# --- PUT: Status 204 No Content ---
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = Book(**book.model_dump())
            book_changed = True
            break
    
    # If we didn't find the book to update, raise 404
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

# --- DELETE: Status 204 No Content ---
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    
    # If we didn't find the book to delete, raise 404
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book