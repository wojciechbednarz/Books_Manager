from schemas.schemas import BookSchema
from db import db
from flask_smorest import Blueprint, abort
from models import BookModel
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Books", __name__, "Operations on books.")


@blp.route("/book")
class Books(MethodView):
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, book_data):
        book = BookModel(**book_data)

        try:
            db.session.add(book)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting book data.")
        return book


@blp.route('/book/<string:book_id>')
class BookById(MethodView):
    @blp.response(200, BookSchema())
    def get(self, book_id):
        try:
            book = BookModel.query.get_or_404(book_id)
            return book
        except KeyError:
            abort(404, message="Book was not found.")
