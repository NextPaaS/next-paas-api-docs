from marshmallow import Schema, fields
from .utils import *


class ProjectSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    origin_name = fields.Str()
    alias_name = fields.Str()
    description = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ProjectSchemaWithRole(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    origin_name = fields.Str()
    alias_name = fields.Str()
    description = fields.Str()
    role = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class GetProjectSchema(Schema):
    project_uuid = fields.Str(metadata={"format": "uuid"})

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