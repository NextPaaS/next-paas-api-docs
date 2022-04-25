from src.api import bp
from src.schema.error_schema import *
from src.schema.project_schema import *
from src.schema.taskEvent_schema import *
from src.schema.user_schema import *
from flask import jsonify, request


@bp.route('/task-event/project/<project_uuid>')
def listTaskEvent(project_uuid):
    """List task event of project
    ---
    get:
        summary: List task event of project
        tags:
            - Task Event (for websocket)
        description: List task event of project
        parameters:
            -   name: project_uuid
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
                    enum: [ALL, CREATE, UPDATE, DELETE]
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
                description: Status Expectation Failed
                content:
                    application/json:
                        schema: DefaultError 
    """

    if project_uuid:
        if request.args.get('type') == "ALL":
            response = [
                {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": [{
                            "task_event_id": 1,
                            "status": "pending",
                            "type": "create"
                        }, {
                            "task_event_id": 2,
                            "status": "pending",
                            "type": "update"
                        }, {
                            "task_event_id": 3,
                            "status": "success",
                            "type": "create"
                        }, {
                            "task_event_id": 9,
                            "status": "pending",
                            "type": "delete"
                        }
                    ]
                }
            ]
        elif request.args.get('type') == "CREATE":
            response = [
                {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": [{
                            "task_event_id": 1,
                            "status": "pending",
                            "type": "create"
                        }, {
                            "task_event_id": 3,
                            "status": "success",
                            "type": "create"
                        }
                    ]
                }
            ]
        elif request.args.get('type') == "UPDATE":
            response = [
                {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": [{
                            "task_event_id": 2,
                            "status": "pending",
                            "type": "update"
                        }
                    ]
                }
            ]
        elif request.args.get('type') == "DELETE":
            response = [
                {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": [{
                            "task_event_id": 9,
                            "status": "pending",
                            "type": "delete"
                        }
                    ]
                }
            ]

    return jsonify(response)

@bp.route('/task-event/<task_event_id>')
def getTaskEvent(task_event_id):
    """Get result task event info
    ---
    get:
        summary: Get result task event info
        tags:
            - Task Event (for websocket)
        description: Get result task event info
        parameters:
            -   name: task_event_id
                in: path
                description: ID of task event
                required: true
                schema:
                    type: string
        responses:
            200:
                description: task event info
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
                description: Status Expectation Failed
                content:
                    application/json:
                        schema: DefaultError 
    """

    if int(task_event_id) == 1:
        response = {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": {
                        'task_event_id': int(task_event_id),
                        'status': 'success',
                        'type': "create"
                    }
                }
    elif int(task_event_id) == 2:
        response = {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": {
                        'task_event_id': int(task_event_id),
                        'status': 'success',
                        'type': "update"
                    }
                }
    elif int(task_event_id) == 3:
        response = {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": {
                        'task_event_id': int(task_event_id),
                        'status': 'success',
                        'type': "update"
                    }
                }
    elif int(task_event_id) == 9:
        response = {
                    "success": boolean(1),
                    "message": "Update project success",
                    "error_code": 0,
                    "data": {
                        'task_event_id': int(task_event_id),
                        'status': 'success',
                        'type': "delete"
                    }
                }

    return jsonify(response)
