from marshmallow import Schema, fields

from .project_schema import ProjectResponseSchema
from .utils import *

class UserOfProject(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    user_email = fields.Str()
    description = fields.Str()
    user_role = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updaed_at = fields.DateTime()

class ListUser(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(UserOfProject))
    metadata = fields.Nested(Metadata)


class ProjectUser(Schema):
    project = fields.Nested(ProjectResponseSchema)
    users = fields.List(fields.Nested(UserOfProject))


class ListUserOfProject(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(ProjectUser)
    metadata = fields.Nested(Metadata)