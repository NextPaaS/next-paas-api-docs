from marshmallow import Schema, fields
from .utils import *


class ProjectSchema(Schema):
    uuid = fields.Str()
    origin_name = fields.Str()
    alias_name = fields.Str()
    description = fields.Str()
    role = fields.Str()


class ProjectResponseSchema(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(ProjectSchema)

class ProjectListResponseSchema(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(ProjectSchema))
    metadata = fields.Nested(Metadata)