from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas

from db import get_db, create_tables
from sqlalchemy.orm import Session


app = FastAPI()

@app.get("/books", response_model=list[schemas.Book])

def get_all_books(db: Session = Depends(get_db)):
    return services.get_book(db)