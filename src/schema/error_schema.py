from marshmallow import Schema, fields

class DefaultError(Schema):
    success = fields.Boolean()
    error_code = fields.Int()
    message = fields.Str()
    data = fields.Str(metadata={"format": "json", "example": {}})

class UnauthorizedError(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 401})
    message = fields.Str(metadata={"format": "string", "example": "Unauthorized"})

class PermissionDeny(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 403})
    message = fields.Str(metadata={"format": "string", "example": "Permission Deny"})

class PageNotFound(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 404})
    message = fields.Str(metadata={"format": "string", "example": "NotFound"})

class StatusExpectationFailed(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 417})
    message = fields.Str()

class ServerError(Schema):
    success = fields.Boolean(metadata={"format": "boolean", "example": False})
    error_code = fields.Int(metadata={"format": "int32", "example": 500})
    message = fields.Str(metadata={"format": "string", "example": "Server Error"})
