from csv import field_size_limit
from marshmallow import Schema, fields
from .utils import *

class ApplicationResourceSchema(Schema):
    name = fields.Str()
    cpu = fields.Int()
    ram = fields.Int()
    default = fields.Boolean()

class VolumeSchema(Schema):
    name = fields.Str()
    pool = fields.Str()
    owner = fields.Str()
    status = fields.Str()
    capacity = fields.Int()


class ApplicationInfoSchema(Schema):
    name = fields.Str()
    cluster = fields.Str()
    deploy = fields.Int()
    cname = fields.List(fields.Str())
    plan = fields.List(fields.Nested(ApplicationResourceSchema))
    volume = fields.List(fields.Nested(VolumeSchema))