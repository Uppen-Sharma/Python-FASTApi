from fastapi import FastAPI, Body

app = FastAPI()

'''in memory book list'''
BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]

@app.get("/books")
async def read_all_books():
    '''return all books'''
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    '''return book by title'''
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    '''filter by category'''
    return [
        book for book in BOOKS
        if book["category"].casefold() == category.casefold()
    ]

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    '''filter by author and category'''
    return [
        book for book in BOOKS
        if book["author"].casefold() == book_author.casefold()
        and book["category"].casefold() == category.casefold()
    ]

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    '''create new book'''
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    '''update book by title'''
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book
            return updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    '''delete book by title'''
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            BOOKS.pop(i)
            break