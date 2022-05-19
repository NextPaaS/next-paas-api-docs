from uuid import UUID
from src.api import bp
from src.schema.error_schema import *
from src.schema.project_schema import *
from src.schema.taskEvent_schema import *
from src.schema.user_schema import *
from flask import jsonify, request, make_response


@bp.route('/task-event/project/<uuid:project_uuid>')
def listTaskEvent(project_uuid):
    """List task event of project
    ---
    get:
        summary: List task event of project
        tags:
            - Task Event (for websocket)
        description: List task event of project
        parameters:
            -   name: projecUuid
                in: path
                description: uuid of project
                required: true
                schema:
                    type: string
            -   name: type
                in: query
                description: type of event
                required: true
                schema:
                    type: string
                    enum: [all, create, update, delete]
        responses:
            200:
                description: List task event of project %s
                content:
                    application/json:
                        schema: ListTaskEventResponse
            401:
                description: Access token is missing or invalid
                content:
                    application/json:
                        schema: UnauthorizedError
            403:
                description: Permission Deny
                content:
                    application/json:
                        schema: PermissionDeny
            404:
                description: Page Notfound
                content:
                    application/json:
                        schema: PageNotFound
            417:
                description: Status Expectation Failed
                content:
                    application/json:
                        schema: StatusExpectationFailed
            500:
                description: Server Error
                content:
                    application/json:
                        schema: ServerError
            default:
                description: Default response
                content:
                    application/json:
                        schema: DefaultError 
    """

    if project_uuid:
        if not request.args.get('type') or request.args.get('type').upper() == "ALL":
            response = {
                    "success": True,
                    "message": f"List {(request.args.get('type'))} task event of project {project_uuid} success",
                    "error_code": 0,
                    "data": [
                        {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d825",
                            "status": "pending",
                            "type": "create"
                        }, {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d826",
                            "status": "pending",
                            "type": "update"
                        }, {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d827",
                            "status": "success",
                            "type": "create"
                        }, {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d828",
                            "status": "pending",
                            "type": "delete"
                        }
                    ]
                }
        elif request.args.get('type').upper() == "CREATE":
            response = {
                    "success": True,
                    "message": f"List {(request.args.get('type'))} task event of project {project_uuid} success",
                    "error_code": 0,
                    "data": [
                        {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d825",
                            "status": "pending",
                            "type": "create"
                        }, {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d827",
                            "status": "success",
                            "type": "create"
                        }
                    ]
                }
        elif request.args.get('type').upper() == "UPDATE":
            response = {
                    "success": True,
                    "message": f"List {(request.args.get('type'))} task event of project {project_uuid} success",
                    "error_code": 0,
                    "data": [
                        {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d826",
                            "status": "pending",
                            "type": "update"
                        }
                    ]
                }

        elif request.args.get('type').upper() == "DELETE":
            response = {
                    "success": True,
                    "message": f"List {(request.args.get('type'))} task event of project {project_uuid} success",
                    "error_code": 0,
                    "data": [
                        {
                            "task_event_id": "c8f044f9-b2fb-49fd-ace4-45d7c740d828",
                            "status": "pending",
                            "type": "delete"
                        }
                    ]
                }
        else:
            return make_response(jsonify(
                {
                    "success": False,
                    "message": "Invalid type '%s'" % (request.args.get('type')),
                    "error_code": 417,
                    "data": []
                }
            ), 417)

    return jsonify(response)

@bp.route('/task-event/<uuid:task_event_id>')
def getTaskEvent(task_event_id):
    """Get result task event info
    ---
    get:
        summary: Get result task event info
        tags:
            - Task Event (for websocket)
        description: Get result task event info
        parameters:
            -   name: taskEventId
                in: path
                description: ID of task event
                required: true
                example:
                    -   c8f044f9-b2fb-49fd-ace4-45d7c740d825
                    -   c8f044f9-b2fb-49fd-ace4-45d7c740d826
                    -   c8f044f9-b2fb-49fd-ace4-45d7c740d827
                    -   c8f044f9-b2fb-49fd-ace4-45d7c740d828
                schema:
                    type: string
                    format: uuid
        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: TaskEventResponse
            401:
                description: Access token is missing or invalid
                content:
                    application/json:
                        schema: UnauthorizedError
            403:
                description: Permission Deny
                content:
                    application/json:
                        schema: PermissionDeny
            404:
                description: Page Notfound
                content:
                    application/json:
                        schema: PageNotFound
            417:
                description: Status Expectation Failed
                content:
                    application/json:
                        schema: StatusExpectationFailed
            500:
                description: Server Error
                content:
                    application/json:
                        schema: ServerError
            default:
                description: Default response
                content:
                    application/json:
                        schema: DefaultError 
    """
    print(task_event_id, type(task_event_id))
    if str(task_event_id) == "c8f044f9-b2fb-49fd-ace4-45d7c740d825":
        return jsonify(
            {
                "success": True,
                "message": "Get task event success",
                "error_code": 0,
                "data": {
                    'task_event_id': (task_event_id),
                    'status': 'success',
                    'type': "create"
                }
            }
        )
    elif str(task_event_id) == "c8f044f9-b2fb-49fd-ace4-45d7c740d826":
        return jsonify(
            {
                "success": True,
                "message": "Get task event success",
                "error_code": 0,
                "data": {
                    'task_event_id': (task_event_id),
                    'status': 'success',
                    'type': "update"
                }
            }
        )
    elif str(task_event_id) == "c8f044f9-b2fb-49fd-ace4-45d7c740d827":
        return jsonify(
            {
                "success": True,
                "message": "Get task event success",
                "error_code": 0,
                "data": {
                    'task_event_id': (task_event_id),
                    'status': 'success',
                    'type': "update"
                }
            }
        )
    elif str(task_event_id) == "c8f044f9-b2fb-49fd-ace4-45d7c740d828":
        return jsonify(
            {
                "success": True,
                "message": "Get task event success",
                "error_code": 0,
                "data": {
                    'task_event_id': (task_event_id),
                    'status': 'success',
                    'type': "delete"
                }
            }
        )

