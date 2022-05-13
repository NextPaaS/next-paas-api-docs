import logging
import re
import sys
from src.api import bp
from src.schema.error_schema import *
from src.schema.project_schema import *
from src.schema.taskEvent_schema import *
from src.schema.user_schema import *
from flask import jsonify, request


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@bp.route('/projects', methods=["GET"])
def listProject():
    """Get List of project
    ---
    get:
        summary: get list of project
        tags:
            - Projects
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
            -   name: email
                in: query
                schema:
                    type: string
                description: filter based on email 
            -   name: userUuid
                in: query
                schema:
                    type: string
                    format: uuid
            -   name: sortField
                in: query
                schema:
                    type: string
                    enum: [projectName, role, createdAt]
                description: sort field 
            -   name: projectName
                in: query
                schema:
                    type: string
                description: filter based on project name 
            -   name: projectUuid
                in: query
                schema:
                    type: string
                description: filter based on project id
            -   name: projectAliasName
                in: query
                schema:
                    type: string
                description: filter based on project alias name
            -   name: sort
                in: query
                schema:
                    type: string
                    enum: [asc, desc]
                description: >
                    Sort order:
                        * `projectName:asc` - Ascending, from A to Z
                        * `projectName:desc` - Descending, from Z to A
                        * `role:asc` - Ascending, from A to Z
                        * `role:desc` - Descending, from Z to A
                        * `createdAt:asc` - Ascending, from A to Z
                        * `createdAt:desc` - Descending, from Z to A
            -   name: limit
                in: query
                description: How many items to return at one time (max 100)
                required: false
                schema:
                    type: integer
                    format: int32
            -   name: page
                in: query
                description: specific page that reach to
                required: false
                schema:
                    type: integer
                    format: int32
            -   name: offset
                in: query
                description: specific size page that want
                required: false
                schema:
                    type: integer
                    format: int32
        description: Get List of project
        responses:
            200:
                description: list project
                content:
                    application/json:
                        schema: ProjectListResponseSchema
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

    response = {
        "success": True,
        "message": "List project success",
        "error_code": 0,
        "data": [
            {
                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                'origin_name': 'project1',
                'alias_name': "day la project 1",
                'description': "day la description project 1",
                'role': "owner",
                'is_active': True,
                'created_at': '2022-04-26T02:51:40.905Z',
                'updated_at': ''
            }, {
                'uuid': '0bea2c68-01eb-43c1-8fc8-bacfefb6f63d',
                'origin_name': "project2",
                'alias_name': "cai nay to lam",
                'description': "",
                'role': "admin",
                'is_active': False,
                'created_at': '2022-04-26T02:51:40.905Z',
                'updated_at': '2022-04-26T02:51:40.905Z'
            }
        ],
        "metadata": {
            "total": 100,
            "current_page": 1,
            "has_next": False,
            "has_previous": 1,
            "previous_page": 1,
            "next_page": 1
        }
    }

    return jsonify(response)


@bp.route('/project/create', methods=["POST"])
def createProject():
    """create project
    ---
    post:
        summary: create project
        tags:
            - Projects
        description: create project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
        requestBody:
            content:
                application/json:
                    schema: PayloadCreateProject

        responses:
            200:
                description: Task event info
                content:
                    application/json:
                        schema: TaskEventCreateProjectResponse
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

    payload = request.get_json()
    response = {
        "success": True,
        "message": "Create project success",
        "error_code": 0,
        "data": {
            "task_event": {
                'task_event_id': "c8f044f9-b2fb-49fd-ace4-45d7c740d825",
                'status': 'success',
                'type': 'create'
            },
            'project': payload
        }
    }

    return jsonify(response)


@bp.route('/project/<uuid:project_uuid>', methods=["GET"])
def getProject(project_uuid):
    """Get info project
    ---
    get:
        summary: get info project
        tags:
            - Projects
        description: Get info project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
            -   name: projectUuid
                in: path
                description: UUID of project
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid
        responses:
            200:
                description: info project
                content:
                    application/json:
                        schema: ProjectResponseSchema
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
    response = {
        "success": True,
        "message": "Get info project %s success",
        "error_code": 0,
        "data": {
            'uuid': project_uuid,
            'origin_name': 'project1',
            'alias_name': "day la project 1",
            'description': "day la description project 1",
            'is_active': True,
            'created_at': '2022-04-26T02:51:40.905Z',
            'updated_at': '2022-04-26T02:51:40.905Z'
        }
    }
    return jsonify(response)


@bp.route('/project/<uuid:project_uuid>/users', methods=["GET"])
def getUserProject(project_uuid):
    """Get user of project
    ---
    get:
        summary: get user of project
        tags:
            - Projects
        description: Get user of project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
            -   name: projectUuid
                in: path
                description: UUID of project
                required: true
                schema:
                    type: string
                    format: uuid
            -   name: username
                in: query
                schema:
                    type: string
                description: filter based on username 
            -   name: groupName
                in: query
                schema:
                    type: string
                    format: uuid
                description: filter based on groupName 
            -   name: sortField
                in: query
                schema:
                    type: string
                    enum: [email, role, created_at]
                description: sort field 
            -   name: sort
                in: query
                schema:
                    type: string
                    enum: [asc, desc]
                description: >
                    Sort order:
                        * `email:asc` - Ascending, from A to Z
                        * `email:desc` - Descending, from Z to A
                        * `role:asc` - Ascending, from A to Z
                        * `role:desc` - Descending, from Z to A
                        * `created_at:asc` - Ascending, from A to Z
                        * `created_at:desc` - Descending, from Z to A
            -   name: limit
                in: query
                description: How many items to return at one time (max 100)
                required: false
                schema:
                    type: integer
                    format: int32
            -   name: page
                in: query
                description: specific page that reach to
                required: false
                schema:
                    type: integer
                    format: int32
            -   name: offset
                in: query
                description: specific size page that want
                required: false
                schema:
                    type: integer
                    format: int32 
        responses:
            200:
                description: List user of project
                content:
                    application/json:
                        schema: ListUserOfProject
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
    args = request.args
    sortField = args.get("sortField")
    username = args.get("username")
    sort = args.get("sort")
    page = args.get("page")
    if page:
        if username:
            if sortField == "email":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }

            elif sortField == "role":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }
            elif sortField == "created_at":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }
            else:
                response = {
                    "success": True,
                    "message": "List user in project %s success" % "project1",
                    "error_code": 0,
                    "data": {
                        "project": {
                            'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                            'origin_name': 'project1',
                            'alias_name': "day la project 1",
                            'description': "day la description project 1",
                            'is_active': True,
                            'created_at': '2022-04-26T02:51:40.905Z',
                            'updated_at': '2022-04-26T02:51:40.905Z'
                        },
                        "users": [
                            {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                'email': f'{username}test@gmail.com',
                                'description': "day la description project 1",
                                'role': "admin",
                                'is_active': True,
                                'created_at': '2022-04-21T02:30:28.911Z',
                                'updated_at': ''
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                'email': f'{username}test1@gmail.com',
                                'description': "user full permission",
                                'role': "owner",
                                'is_active': True,
                                'created_at': '2022-04-22T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': f'{username}test2@gmail.com',
                                'description': "day la role reader",
                                'role': "reader",
                                'is_active': False,
                                'created_at': '2022-04-23T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': f'{username}test3@gmail.com',
                                'description': "day la role custom",
                                'role': "dev",
                                'is_active': False,
                                'created_at': '2022-04-24T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }
                        ]
                    },
                    "metadata": {
                        "total": 4,
                        "current_page": int(page),
                        "has_next": False,
                        "has_previous": 1,
                        "previous_page": 1,
                        "next_page": int(page) + 1
                    }
                }
        else:
            if sortField == "email":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test1@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }

            elif sortField == "role":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }
            elif sortField == "created_at":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }
            else:
                response = {
                    "success": True,
                    "message": "List user in project %s success" % "project1",
                    "error_code": 0,
                    "data": {
                        "project": {
                            'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                            'origin_name': 'project1',
                            'alias_name': "day la project 1",
                            'description': "day la description project 1",
                            'is_active': True,
                            'created_at': '2022-04-26T02:51:40.905Z',
                            'updated_at': '2022-04-26T02:51:40.905Z'
                        },
                        "users": [
                            {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                'email': 'test@gmail.com',
                                'description': "day la description project 1",
                                'role': "admin",
                                'is_active': True,
                                'created_at': '2022-04-21T02:30:28.911Z',
                                'updated_at': ''
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                'email': 'test1@gmail.com',
                                'description': "user full permission",
                                'role': "owner",
                                'is_active': True,
                                'created_at': '2022-04-22T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': 'test2@gmail.com',
                                'description': "day la role reader",
                                'role': "reader",
                                'is_active': False,
                                'created_at': '2022-04-23T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': 'test3@gmail.com',
                                'description': "day la role custom",
                                'role': "dev",
                                'is_active': False,
                                'created_at': '2022-04-24T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }
                        ]
                    },
                    "metadata": {
                        "total": 4,
                        "current_page": int(page),
                        "has_next": False,
                        "has_previous": 1,
                        "previous_page": 1,
                        "next_page": int(page) + 1
                    }
                }
    else:
        page = 1
        if username:
            if sortField == "email":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }

                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }

            elif sortField == "role":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }

                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }

            elif sortField == "created_at":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }

                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': f'{username}test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': f'{username}test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                },
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': f'{username}test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }

            else:
                response = {
                    "success": True,
                    "message": "List user in project %s success" % "project1",
                    "error_code": 0,
                    "data": {
                        "project": {
                            'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                            'origin_name': 'project1',
                            'alias_name': "day la project 1",
                            'description': "day la description project 1",
                            'is_active': True,
                            'created_at': '2022-04-26T02:51:40.905Z',
                            'updated_at': '2022-04-26T02:51:40.905Z'
                        },
                        "users": [
                            {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                'email': f'{username}test@gmail.com',
                                'description': "day la description project 1",
                                'role': "admin",
                                'is_active': True,
                                'created_at': '2022-04-21T02:30:28.911Z',
                                'updated_at': ''
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                'email': f'{username}test1@gmail.com',
                                'description': "user full permission",
                                'role': "owner",
                                'is_active': True,
                                'created_at': '2022-04-22T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': f'{username}test2@gmail.com',
                                'description': "day la role reader",
                                'role': "reader",
                                'is_active': False,
                                'created_at': '2022-04-23T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': f'{username}test3@gmail.com',
                                'description': "day la role custom",
                                'role': "dev",
                                'is_active': False,
                                'created_at': '2022-04-24T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }
                        ]
                    },
                    "metadata": {
                        "total": 4,
                        "current_page": int(page),
                        "has_next": False,
                        "has_previous": 1,
                        "previous_page": 1,
                        "next_page": int(page) + 1
                    }
                }

        else:
            if sortField == "email":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test1@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }

                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                },
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }

            elif sortField == "role":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                },
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }
            elif sortField == "created_at":
                if sort == 'desc':
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test2@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test1@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": 1
                        }
                    }
                else:
                    response = {
                        "success": True,
                        "message": "List user in project %s success" % "project1",
                        "error_code": 0,
                        "data": {
                            "project": {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                                'origin_name': 'project1',
                                'alias_name': "day la project 1",
                                'description': "day la description project 1",
                                'is_active': True,
                                'created_at': '2022-04-26T02:51:40.905Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            },
                            "users": [
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                    'email': 'test@gmail.com',
                                    'description': "day la description project 1",
                                    'role': "admin",
                                    'is_active': True,
                                    'created_at': '2022-04-21T02:30:28.911Z',
                                    'updated_at': ''
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                    'email': 'test1@gmail.com',
                                    'description': "user full permission",
                                    'role': "owner",
                                    'is_active': True,
                                    'created_at': '2022-04-22T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                },
                                {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test2@gmail.com',
                                    'description': "day la role reader",
                                    'role': "reader",
                                    'is_active': False,
                                    'created_at': '2022-04-23T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }, {
                                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                    'email': 'test3@gmail.com',
                                    'description': "day la role custom",
                                    'role': "dev",
                                    'is_active': False,
                                    'created_at': '2022-04-24T02:30:28.911Z',
                                    'updated_at': '2022-04-26T02:51:40.905Z'
                                }
                            ]
                        },
                        "metadata": {
                            "total": 4,
                            "current_page": int(page),
                            "has_next": False,
                            "has_previous": 1,
                            "previous_page": 1,
                            "next_page": int(page) + 1
                        }
                    }
            else:
                response = {
                    "success": True,
                    "message": "List user in project %s success" % "project1",
                    "error_code": 0,
                    "data": {
                        "project": {
                            'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                            'origin_name': 'project1',
                            'alias_name': "day la project 1",
                            'description': "day la description project 1",
                            'is_active': True,
                            'created_at': '2022-04-26T02:51:40.905Z',
                            'updated_at': '2022-04-26T02:51:40.905Z'
                        },
                        "users": [
                            {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                                'email': 'test@gmail.com',
                                'description': "day la description project 1",
                                'role': "admin",
                                'is_active': True,
                                'created_at': '2022-04-21T02:30:28.911Z',
                                'updated_at': ''
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                                'email': 'test1@gmail.com',
                                'description': "user full permission",
                                'role': "owner",
                                'is_active': True,
                                'created_at': '2022-04-22T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': 'test2@gmail.com',
                                'description': "day la role reader",
                                'role': "reader",
                                'is_active': False,
                                'created_at': '2022-04-23T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }, {
                                'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                                'email': 'test3@gmail.com',
                                'description': "day la role custom",
                                'role': "dev",
                                'is_active': False,
                                'created_at': '2022-04-24T02:30:28.911Z',
                                'updated_at': '2022-04-26T02:51:40.905Z'
                            }
                        ]
                    },
                    "metadata": {
                        "total": 4,
                        "current_page": int(page),
                        "has_next": False,
                        "has_previous": 1,
                        "previous_page": 1,
                        "next_page": int(page) + 1
                    }
                }

    if not args:
        page = 1
        response = {
            "success": True,
            "message": "List user in project %s success" % "project1",
            "error_code": 0,
            "data": {
                "project": {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                    'origin_name': 'project1',
                    'alias_name': "day la project 1",
                    'description': "day la description project 1",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                },
                "users": [
                    {
                        'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f26',
                        'email': 'test@gmail.com',
                        'description': "day la description project 1",
                        'role': "admin",
                        'is_active': True,
                        'created_at': '2022-04-21T02:30:28.911Z',
                        'updated_at': ''
                    }, {
                        'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f25',
                        'email': 'test1@gmail.com',
                        'description': "user full permission",
                        'role': "owner",
                        'is_active': True,
                        'created_at': '2022-04-22T02:30:28.911Z',
                        'updated_at': '2022-04-26T02:51:40.905Z'
                    }, {
                        'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                        'email': 'test2@gmail.com',
                        'description': "day la role reader",
                        'role': "reader",
                        'is_active': False,
                        'created_at': '2022-04-23T02:30:28.911Z',
                        'updated_at': '2022-04-26T02:51:40.905Z'
                    }, {
                        'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f27',
                        'email': 'test3@gmail.com',
                        'description': "day la role custom",
                        'role': "dev",
                        'is_active': False,
                        'created_at': '2022-04-24T02:30:28.911Z',
                        'updated_at': '2022-04-26T02:51:40.905Z'
                    }
                ]
            },
            "metadata": {
                "total": 4,
                "current_page": int(page),
                "has_next": False,
                "has_previous": 1,
                "previous_page": 1,
                "next_page": int(page) + 1
            }
        }
    return jsonify(response)


@bp.route('/project/update/<uuid:project_uuid>', methods=['PUT'])
def updateProject(project_uuid):
    """Get info project
    ---
    put:
        summary: get info project
        tags:
            - Projects
        description: Get info project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
            -   name: projectUuid
                in: path
                description: UUID of project
                required: true
                schema:
                    type: string
                    format: uuid
        requestBody:
            content:
                application/json:
                    schema: ValuesProject
        responses:
            200:
                description: info project
                content:
                    application/json:
                        schema: TaskEventUpdateProjectResponse
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
    payload = request.get_json()
    before_values = {
        'project_name': 'project1',
        'description': "day la description project 1"
    }

    response = {
        "success": True,
        "message": "Update project %s success",
        "error_code": 0,
        "data": {
            "task_event": {
                'task_event_id': "c8f044f9-b2fb-49fd-ace4-45d7c740d826",
                'status': 'success',
                'type': 'update'
            },
            "project": {
                "before_values": before_values,
                "after_values": payload
            }
        }
    }

    return jsonify(response)


@bp.route('/project/delete/<uuid:project_uuid>', methods=['DELETE'])
def deleteProject(project_uuid):
    """Delete project
    ---
    delete:
        summary: Delete project
        tags:
            - Projects
        description: Delete project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
            -   name: projectUuid
                in: path
                description: UUID of project
                required: true
                schema:
                    type: string
                    format: uuid
        responses:
            200:
                description: delete project
                content:
                    application/json:
                        schema: TaskEventDeleteProjectResponse
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

    project = {
        'project_name': 'project1',
        'description': "day la description project 1"
    }

    response = {
        "success": True,
        "message": "Delete project %s success",
        "error_code": 0,
        "data": [
            {
                "task_event": {
                    'task_event_id': "c8f044f9-b2fb-49fd-ace4-45d7c740d828",
                    'status': 'success',
                    'type': 'delete'
                }
            }, {
                "project": project
            }
        ]
    }

    return jsonify(response)
