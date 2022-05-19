from marshmallow import fields, Schema


class Metadata(Schema):
    total = fields.Int()
    has_next = fields.Boolean()
    current_page = fields.Int()
    next_page = fields.Int()
    page = fields.Int()
    has_previous = fields.Int()
    previous_page = fields.Int()