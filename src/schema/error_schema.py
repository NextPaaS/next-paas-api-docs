from xmlrpc.client import boolean
from marshmallow import Schema, fields

class DefaultError(Schema):
    success = fields.Boolean()
    error_code = fields.Int()
    message = fields.Str()
    data = fields.Str(metadata={"format": "json", "example": {}})

class UnauthorizedError(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 401})
    message = fields.Str()

class PermissionDeny(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 403})
    message = fields.Str(metadata={"format": "string", "example": "permission deny"})

class PageNotFound(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 404})
    message = fields.Str()

class StatusExpectationFailed(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 417})
    message = fields.Str()

class ServerError(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 500})
    message = fields.Str()
