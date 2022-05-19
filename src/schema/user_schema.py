from marshmallow import Schema, fields

from .project_schema import ProjectSchema
from .utils import *

class UserOfProject(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    user_email = fields.Str(metadata={"format": "email"})
    description = fields.Str()
    user_role = fields.Str()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class GetUser(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(UserOfProject)

class ListUser(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(UserOfProject))
    metadata = fields.Nested(Metadata)


class ProjectUser(Schema):
    project = fields.Nested(ProjectSchema)
    users = fields.List(fields.Nested(UserOfProject))


class ListUserOfProject(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(ProjectUser)
    metadata = fields.Nested(Metadata)


class ListProjectOfUser(Schema):
    uuid = fields.Str(metadata={"format": "uuid"})
    email = fields.Str(metadata={"format": "email"})
    project_name = fields.List(fields.Str())
    is_active = fields.Boolean()
    created_at = fields.DateTime()


class ListProjectOfUserResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.List(fields.Nested(ListProjectOfUser))
    metadata = fields.Nested(Metadata)


class InviteUser(Schema):
    project_uuid = fields.Str(metadata={"format": "uuid"})
    email = fields.Str(metadata={"format": "email"})
    role_uuid = fields.Str(metadata={"format": "uuid"})


class UpdateUserInProject(Schema):
    project_uuid = fields.Str(metadata={"format": "uuid"})
    user_uuid = fields.Str(metadata={"format": "uuid"})
    role_uuid = fields.Str(metadata={"format": "uuid"})


class InviteUserResponse(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": True})
    error_code = fields.Int(metadata={"format": "int32", "example": 0})
    message = fields.Str(metadata={"format": "string", "example": "Attach user %s with role %s to project %s successfully"})

class DeleteUserResponse(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": True})
    error_code = fields.Int(metadata={"format": "int32", "example": 0})
    message = fields.Str(metadata={"format": "string", "example": "Detach user %s from project %s successfully"})