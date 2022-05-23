from marshmallow import Schema, fields

from .utils import *


class ResourceSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    name = fields.Str(metadata={"format": "string"})
    type = fields.Str(metadata={"format": "string"})
    service_type = fields.Str(metadata={"format": "string"})
    service_name = fields.Str(metadata={"format": "string"})
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()

class ListResourceSchemaResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(ResourceSchema))
    metadata = fields.Nested(Metadata)