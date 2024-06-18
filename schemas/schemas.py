from marshmallow import Schema, fields


class PlainBookSchema(Schema):
    book_author = fields.Str(required=True)
    book_name = fields.Str(required=True)
    book_id = fields.Int(dump_only=True)


class PlainBookshelfSchema(Schema):
    bookshelf_name = fields.Str(required=True)
    bookshelf_id = fields.Int(dump_only=True)


class BookSchema(PlainBookSchema):
    bookshelf_id = fields.Int()


class BookShelfSchema(PlainBookshelfSchema):
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only=True)
