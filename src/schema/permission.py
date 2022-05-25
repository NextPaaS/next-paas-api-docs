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
