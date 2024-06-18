from db import db


class BookshelfModel(db.Model):
    __tablename__ = "bookshelfs"

    bookshelf_name = db.Column(db.String(80), unique=True, nullable=False)
    bookshelf_id = db.Column(db.Integer, primary_key=True)
    books = db.relationship("BookModel", back_populates="bookshelf", lazy="dynamic")
