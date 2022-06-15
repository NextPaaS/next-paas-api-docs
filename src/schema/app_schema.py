from csv import field_size_limit
from platform import platform
from attr import field
from marshmallow import Schema, fields
from .utils import *

class ApplicationResourceSchema(Schema):
    name = fields.Str()
    cpu = fields.Int()
    ram = fields.Int()
    default = fields.Boolean()

class VolumeBindSchema(Schema):
    app = fields.Str()
    mountPoint = fields.Str()
    readOnly = fields.Boolean()

class VolumeSchema(Schema):
    name = fields.Str()
    pool = fields.Str()
    owner = fields.Str()
    status = fields.Str()
    capacity = fields.Int()
    binds = fields.List(fields.Nested(VolumeBindSchema))

class UnitSchema(Schema):
    name = fields.Str()
    processname = fields.Str()
    appname = fields.Str()
    platformType = fields.Str()
    status = fields.Str()
    restarts = fields.Int()
    ready = fields.Boolean()

class AutoScaleSchema(Schema):
    process = fields.Str()
    minUnits = fields.Int()
    maxUnits = fields.Int()
    avgCPU = fields.Int()

class EnvSchema(Schema):
    name = fields.Str()
    value = fields.Str()
    public = fields.Boolean()

class EnvListSchema(Schema):
    envs = fields.List(fields.Nested(EnvSchema))

class EventSchema(Schema):
    id = fields.Int()
    date = fields.Date()
    success = fields.Boolean()
    owner = fields.Str()
    kind = fields.Str()
    target = fields.Str()

class ListEventSchema(Schema):
    events = fields.List(fields.Nested(EventSchema))

class ServicePlans(Schema):
    name = fields.Str()
    cpu = fields.Int()
    ram = fields.Int()

class ServiceSchema(Schema):
    name = fields.Str()
    pool = fields.Str()
    plans = fields.List(fields.Nested(ServicePlans))

class ListServiceSchema(Schema):
    services = fields.List(fields.Nested(ServiceSchema))


class ApplicationInfoSchema(Schema):
    name = fields.Str()
    cluster = fields.Str()
    deploy = fields.Int()
    cname = fields.List(fields.Str())
    teamowner = fields.Str()
    owner = fields.Str()
    pool = fields.Str()
    platform = fields.Str()
    plan = fields.List(fields.Nested(ApplicationResourceSchema))
    volumes = fields.List(fields.Nested(VolumeBindSchema))
    units = fields.List(fields.Nested(UnitSchema))
    autoscale = fields.List(fields.Nested(AutoScaleSchema))
    envs = fields.List(fields.Nested(EnvSchema))