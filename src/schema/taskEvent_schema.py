from marshmallow import Schema, fields
from .utils import *

class TaskEvent(Schema):
    task_event_id = fields.Str()
    type = fields.Str()
    status = fields.Str()


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
    metadata = fields.Nested(Metadata)

class TaskEventUpdateProjectResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEventUpdateProject)
    metadata = fields.Nested(Metadata)


class TaskEventDeleteProjectResponse(Schema):
    success = fields.Boolean()
    message = fields.Str()
    error_code = fields.Int()
    data = fields.Nested(TaskEventDeleteProject)
    metadata = fields.Nested(Metadata)