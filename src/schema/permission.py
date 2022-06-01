from marshmallow import Schema, fields
from .utils import *


class PermissionSchema(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    role_uuid = fields.Str(metadata={"format": "uuid"})
    resource_uuid = fields.Str(metadata={"format": "uuid"})
    action = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class PermissionCreateSchema(Schema):
    effect = fields.Str(metadata={"example": "allow"})
    action = (fields.Str(metadata={"example": ("create", "delete")}))
    resources = fields.Str(metadata={"example": ("iaas-cloud.servers", "iaas-cloud.volumes")})
    conditions = fields.Nested(Schema)