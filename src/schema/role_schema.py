from marshmallow import Schema, fields
from .utils import *
from .resource_schema import ResourceSchema
from .permission import PermissionSchema


class RoleSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    name = fields.Str(metadata={"format": "string"})
    description = fields.Str()
    is_custom = fields.Boolean()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()

class ListRoleSchemaResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(RoleSchema))
    metadata = fields.Nested(Metadata)

class FullInfoRole(Schema):
    role = fields.Nested(RoleSchema)
    resources = fields.List(fields.Nested(ResourceSchema))

class GetRoleSchemaResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(FullInfoRole)


class CreateRoleSchemaResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(PermissionSchema)