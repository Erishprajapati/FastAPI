from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() #created instance

@app.get('/library')
def index(limit = 10, published:bool = True, sort:Optional[str] = None):
    if published:
        return {'data' : f'{limit} published books from database of Book lists'}
    else:
        return None

@app.get('/library/unreleased') 
def unreleased_books():
    return {'data' : 'List of unreleased books'}

@app.get('/library/{book_id}')
def specific_book(book_id:int):
    return {'data': 2}

@app.get('/library/{book_id}/reviews')
def book_reviews(book_id,limit = 10):
    return {'data' :{'first review', 'second review', 'third review'}}  

class Book(BaseModel):
    title : str
    description: str
    published: Optional[bool]
    author : str

@app.post('/library')
def add_book(book : Book):
    return {'data' : f'Book is added by {book.title}'}