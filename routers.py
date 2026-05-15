from fastapi import  APIRouter,FastAPI, Depends, HTTPException
from services import get_book, create_book, get_book_by_id, update_book, delete_book
from schemas import BookCreate, BookBase, Book as BookSchema
from models import Book as BookModel
from db import get_db
from sqlalchemy.orm import Session

router = APIRouter(
  prefix="/api",
  tags=["books"]

)

@router.post("/books/", response_model=BookBase)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/books/", response_model=list[BookSchema])
def get_all_books(db: Session = Depends(get_db)):
    return get_book(db)


@router.get("/books/{book_id}", response_model=BookSchema)

def search_book_by_id(book_id: int, db: Session = Depends(get_db)):
    
    book = get_book_by_id(db, book_id)  
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
    


@router.put("/books/{book_id}", response_model=BookSchema)

def updated_book(book_id: int, book_data: BookCreate, db: Session = Depends(get_db)):
    
    book_updated = update_book(db, book_id, book_data)
    if not book_updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_updated

@router.delete("/books/{book_id}", response_model=BookSchema)

def deleted_book(book_id: int, db: Session = Depends(get_db)):
    
    book_delete = delete_book(db, book_id)
    if not book_delete:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_delete