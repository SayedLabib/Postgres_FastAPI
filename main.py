from fastapi import FastAPI, Depends, HTTPException
from services import get_book, create_book
from schemas import BookCreate, BookBase, Book
from db import get_db
from sqlalchemy.orm import Session


app = FastAPI()

@app.post("/books/", response_model=BookBase)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)


@app.get("/books/", response_model=list[Book])
def get_all_books(db: Session = Depends(get_db)):
    return get_book(db)

