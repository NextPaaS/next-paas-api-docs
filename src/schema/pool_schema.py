from marshmallow import Schema, fields

from .project_schema import ProjectSchemaWithRole, ProjectSchema
from .utils import *

class poolInfoSchema(Schema):
    name = fields.Str()
    address = fields.Str()
    default = fields.Boolean()
    provisioner = fields.Boolean()
    key = fields.Str()

class ListPool(Schema):
    pools = fields.List(fields.Nested(poolInfoSchema))