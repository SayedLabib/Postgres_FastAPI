from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate


def create_book(db:Session, book: BookCreate):
    book_instance = Book(**book.model_dump())

    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)

    return book_instance

def get_book(db: Session):
    return db.query(Book).all()        

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data: BookCreate):
    
    book_instance = db.query(Book).filter(Book.id == book_id).first()
    
    if not book_instance:
        return None

    for key, value in book_data.model_dump().items():
        setattr(book_instance, key, value)

    db.commit()
    db.refresh(book_instance)
    return book_instance


def delete_book(db: Session, book_id: int):
    book_instance = db.query(Book).filter(Book.id == book_id).first()
    
    if not book_instance:
        return None

    db.delete(book_instance)
    db.commit()
    return book_instance