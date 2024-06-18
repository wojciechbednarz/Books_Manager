from schemas.schemas import BookShelfSchema
from db import db
from flask_smorest import Blueprint, abort
from models import BookshelfModel
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Bookshelf's", __name__, "Operations on bookshelf's.")


@blp.route("/bookshelf")
class Bookshelf(MethodView):
    @blp.arguments(BookShelfSchema)
    @blp.response(201, BookShelfSchema)
    def post(self, bookshelf_data):
        bookshelf = BookshelfModel(**bookshelf_data)
        # try:
        #     db.session.add(bookshelf)
        #     db.session.commit()
        # except SQLAlchemyError:
        #     abort(500, message="An error occured while inserting bookshelf data.")
        # return 201, bookshelf
        db.session.add(bookshelf)
        db.session.commit()
        return bookshelf


@blp.route("/bookshelf/<string:bookshelf_id>")
class BookshelfById(MethodView):
    @blp.response(200, BookShelfSchema)
    def get(self, bookshelf_id):
        try:
            booskshelf = BookshelfModel.query.get_or_404(bookshelf_id)
            return booskshelf
        except KeyError:
            abort(404, message="Book was not found.")
