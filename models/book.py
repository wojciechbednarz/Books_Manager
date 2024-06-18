from db import db


class BookModel(db.Model):
    __tablename__ = "books"

    book_author = db.Column(db.String, nullable=False)
    book_name = db.Column(db.String, unique=True, nullable=False)
    book_id = db.Column(db.Integer, primary_key=True)
    bookshelf_id = db.Column(db.Integer, db.ForeignKey('bookshelfs.bookshelf_id'), nullable=False)
    bookshelf = db.relationship('BookshelfModel', back_populates='books')
