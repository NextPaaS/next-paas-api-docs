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


@bp.route('/users', methods=["GET"])
def listUser():
    """list danh sách các user kèm project mà user đó tham gia dưới quyền owner do tôi phụ trách
    ---
    get:
        summary: list danh sách các user kèm project mà user đó tham gia dưới quyền owner do tôi phụ trách
        tags:
            - Users
        description: list danh sách các user kèm project mà user đó tham gia dưới quyền owner do tôi phụ trách
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: email
                in: query
                schema:
                    type: string
                    format: email
                description: filter based on email
            -   name: sortField
                in: query
                schema:
                    type: string
                    enum: [email, createdAt]
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

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: ListProjectOfUserResponse
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
    data = [
        {
            "uuid": "b0a6dc1e-dda8-4562-b62c-007bb7993f27",
            "email": "user1@gmail.com",
            "is_active": True,
            "created_at": "2022-04-26T02:51:40.905Z",
            "projects": [
                {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                    'origin_name': 'project1',
                    'alias_name': "day la project 1",
                    'description': "day la description project 1",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }, {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-070dd6355r05',
                    'origin_name': 'project2',
                    'alias_name': "day la project 2",
                    'description': "day la description project 1",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }
            ],
        }, {
            "uuid": "b0a6dc1e-dda8-4562-b62c-007bb7993fp7",
            "email": "user2@gmail.com",
            "is_active": True,
            "created_at": "2022-04-26T02:51:40.905Z",
            "projects": [
                {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                    'origin_name': 'project1',
                    'alias_name': "day la project 1",
                    'description': "day la description project 1",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }, {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f09',
                    'origin_name': 'project3',
                    'alias_name': "day la project 3",
                    'description': "day la description project 3",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }, {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f09',
                    'origin_name': 'project4',
                    'alias_name': "day la project 4",
                    'description': "day la description project 4",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }
            ],
        }, {
            "uuid": "b0a6dc1e-dda8-4562-b62c-007bb7993fo7",
            "email": "user3@gmail.com",
            "is_active": False,
            "created_at": "2022-04-26T02:51:40.905Z",
            "projects": [
                {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                    'origin_name': 'project1',
                    'alias_name': "day la project 1",
                    'description': "day la description project 1",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }, {
                    'uuid': 'b0a6dc1e-dda8-4562-b62c-007bb7993f99',
                    'origin_name': 'project1',
                    'alias_name': "day la project 1",
                    'description': "day la description project 1",
                    'is_active': True,
                    'created_at': '2022-04-26T02:51:40.905Z',
                    'updated_at': '2022-04-26T02:51:40.905Z'
                }
            ],
        }
        ]

    response = {
        "success": True,
        "message": "list users with projects success",
        "error_code": 0,
        "data": data,
        "metadata": {
            "total": 9,
            "current_page": 1,
            "has_next": False,
            "has_previous": None,
            "previous_page": None,
            "next_page": None
        }
    }
    return jsonify(response)


@bp.route('/user/invite', methods=["POST"])
def inviteUser():
    """invite user join project
    ---
    post:
        summary: invite user join project
        tags:
            - Users
        description: invite user join project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
        requestBody:
            content:
                application/json:
                    schema: InviteUser

        responses:
            200:
                description: Response success
                content:
                    application/json:
                        schema: InviteUserResponse
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
    req = request.get_json()
    project_uuid = req["project_uuid"]
    email = req["email"]
    role_uuid = req["role_uuid"]
    response = {
        "success": True,
        "message": "Attach user %s with role %s to project %s successfully",
        "error_code": 0,
    }
    return jsonify(response)


@bp.route('/user/<uuid:user_uuid>/<uuid:project_uuid>', methods=["GET"])
def getUser(user_uuid, project_uuid):
    """get user info in project
    ---
    get:
        summary: detail user in project
        tags:
            - Users
        description: detail user in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: user_uuid
                in: path
                description: user_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid
            -   name: project_uuid
                in: path
                description: project_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid
        responses:
            200:
                description: Response success
                content:
                    application/json:
                        schema: UserProjectResponse
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

    data = {
        "user": 
            {
                'uuid': user_uuid,
                'email': f'test3@gmail.com',
                'description': "day la role custom",
                'role': "reader",
                'is_active': True,
                'created_at': '2022-04-21T02:30:28.911Z',
                'updated_at': '2022-04-26T02:51:40.905Z'
            },
        "project":
            {
            'uuid': project_uuid,
            'origin_name': 'project1',
            'alias_name': "day la project 1",
            'description': "day la description project 1",
            'is_active': True,
            'created_at': '2022-04-26T02:51:40.905Z',
            'updated_at': '2022-04-26T02:51:40.905Z'
            }
        }
    response = {
        "success": True,
        "message": "get users %s of project %s success",
        "error_code": 0,
        "data": data
    }
    return jsonify(response)

@bp.route('/user/update/<uuid:user_uuid>', methods=["PUT"])
def updateUser(user_uuid):
    """update user in project
    ---
    put:
        summary: update user in project
        tags:
            - Users
        description: update user in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: user_uuid
                in: path
                description: user_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid
        requestBody:
            content:
                application/json:
                    schema: UpdateUserInProject

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: InviteUserResponse
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
    req = request.get_json()
    project_uuid = req["project_uuid"]
    role_uuid = req["role_uuid"]
    user_uuid = req["user_uuid"]
    response = {
        "success": True,
        "message": "Attach user %s with role %s to project %s successfully" % (user_uuid, role_uuid, project_uuid),
        "error_code": 0,
    }
    return jsonify(response)

@bp.route('/user/delete/<uuid:user_uuid>', methods=["DELETE"])
def deleteUser(user_uuid):
    """delete user from project
    ---
    delete:
        summary: delete user from project
        tags:
            - Users
        description: delete user from project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: user_uuid
                in: path
                description: user_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid
        requestBody:
            content:
                application/json:
                    schema: GetProjectSchema

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: DeleteUserResponse
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
    req = request.get_json()
    project_uuid = req["project_uuid"]
    response = {
        "success": True,
        "message": "Detach user %s from project %s successfully" % (user_uuid, project_uuid),
        "error_code": 0,
    }
    return jsonify(response)