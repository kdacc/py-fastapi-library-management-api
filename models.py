from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    summary = Column(String(511))
    publication_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey("author.id"))


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    bio = Column(String(511))
    books = relationship(Book)

