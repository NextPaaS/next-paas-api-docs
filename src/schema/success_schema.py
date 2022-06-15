from importlib_metadata import metadata
from marshmallow import Schema, fields

class DefaultSuccess(Schema):
    message = fields.Str(metadata={"format":"string", "example":"Successful Request!!!"})
    code = fields.Int(metadata={"example":200})
    success = fields.Boolean(metadata={"example":True})