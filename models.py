from db import Base
from sqlalchemy import Column, Integer, String, Float

class Book(Base):
     
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, index=True)
    year = Column(Integer)  
    price = Column(Float)

