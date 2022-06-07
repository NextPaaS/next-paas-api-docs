from marshmallow import Schema, fields

from .utils import *


class ResourceSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    name = fields.Str(metadata={"format": "string"})
    type = fields.Str(metadata={"format": "string"})
    service_type = fields.Str(metadata={"format": "string"})
    service_name = fields.Str(metadata={"format": "string"})
    endpoint = fields.Str()
    description = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()


class Sub2ResourceSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    name = fields.Str(metadata={"format": "string"})
    type = fields.Str(metadata={"format": "string"})
    service_type = fields.Str(metadata={"format": "string"})
    service_name = fields.Str(metadata={"format": "string"})
    endpoint = fields.Str()
    description = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
    sub_resource = fields.List(fields.Nested(ResourceSchema))

class SubResourceSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    name = fields.Str(metadata={"format": "string"})
    type = fields.Str(metadata={"format": "string"})
    service_type = fields.Str(metadata={"format": "string"})
    service_name = fields.Str(metadata={"format": "string"})
    endpoint = fields.Str()
    description = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
    sub_resource = fields.List(fields.Nested(Sub2ResourceSchema))

class ListResourceSchemaResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(ResourceSchema))
    metadata = fields.Nested(Metadata)