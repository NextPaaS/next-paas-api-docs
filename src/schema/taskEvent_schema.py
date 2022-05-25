from marshmallow import Schema, fields
from .utils import *
from .role_schema import RoleSchema

class TaskEvent(Schema):
    task_event_id = fields.Str(metadata={"format": "uuid"})
    type = fields.Str()
    status = fields.Str(metadata={"format": "string", "example": "Success"})


class TaskEventResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEvent)

class ListTaskEventResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEvent)
    metadata = fields.Nested(Metadata)


class PayloadCreateProject(Schema):
    user_uuid = fields.Str(metadata={"format": "uuid", "required": "true"})
    user_email = fields.Str(metadata={"format": "email"})
    project_name = fields.Str()
    description = fields.Str()

class ValuesProject(Schema):
    project_name = fields.Str(metadata={"required": "true"})
    description = fields.Str()

class TaskEventCreateProject(Schema):
    task_event = fields.Nested(TaskEvent)
    project = fields.Nested(PayloadCreateProject)

class ValuesUpdate(Schema):
    before_values = fields.Nested(ValuesProject)
    after_values = fields.Nested(ValuesProject)
class TaskEventUpdateProject(Schema):
    task_event = fields.Nested(TaskEvent)
    project = fields.Nested(ValuesUpdate)

class TaskEventDeleteProject(Schema):
    task_event = fields.Nested(TaskEvent)
    project = fields.Nested(ValuesProject)


class TaskEventCreateProjectResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEventCreateProject)

class TaskEventUpdateProjectResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEventUpdateProject)


class TaskEventDeleteProjectResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEventDeleteProject)


class TaskEventDeleteRole(Schema):
    task_event = fields.Nested(TaskEvent)
    role = fields.Nested(RoleSchema)

class TaskEventDeleteRoleResponse(Schema):
    success = fields.Boolean()
    message = fields.Str(metadata={"format": "string", "example": "Delete role %s successfully"})
    error_code = fields.Int()
    data = fields.Nested(TaskEventDeleteRole)