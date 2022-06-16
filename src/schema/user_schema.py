from marshmallow import Schema, fields

from .project_schema import ProjectSchemaWithRole, ProjectSchema
from .utils import *

class userRoleProject(Schema):
    user_name = fields.Str()
    project_name = fields.Str()
    role = fields.Str()

class Project(Schema):
    project_name = fields.Str()
    description = fields.Str()
    roles = fields.List(fields.Nested(userRoleProject))

class ListProject(Schema):
    projects = fields.List(fields.Nested(Project))

class UserInfo(Schema):
    user_name = fields.Str()
    quota = fields.Int()
    projects = fields.List(fields.Nested(Project))
