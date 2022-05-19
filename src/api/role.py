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


@bp.route('/roles/<uuid:project_uuid>', methods=["GET"])
def listRole(project_uuid):
    """list role in project
    ---
    get:
        summary: list role in project
        tags:
            - Roles
        description: list role in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string
            -   name: role
                in: query
                schema:
                    type: string
                description: filter based on role name
            -   name: sortField
                in: query
                schema:
                    type: string
                    enum: [role, createdAt]
                description: sort field 
            -   name: sort
                in: query
                schema:
                    type: string
                    enum: [asc, desc]
                description: >
                    Sort order:
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

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: ListRoleSchemaResponse
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
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffa7",
                "name": "Owner",
                "description": "role owner",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffr7",
                "name": "Admin",
                "description": "role admin",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffw7",
                "name": "Billing",
                "description": "role Billing",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffx7",
                "name": "Reader",
                "description": "role Reader",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffg7",
                "name": "Member",
                "description": "role Member",
                "is_custom": False,
                "is_active": False,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": "2022-04-29T02:51:40.905Z",
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffj7",
                "name": "custom role 1",
                "description": "role custom 1",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": "2022-04-28T02:51:40.905Z",
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                "name": "custom role 2",
                "description": "role custom 2",
                "is_custom": False,
                "is_active": False,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": "2022-04-30T02:51:40.905Z",
                "deleted_at": None,
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


@bp.route('/role/create', methods=["POST"])
def createRole():
    """create role in project
    ---
    post:
        summary: create role in project
        tags:
            - Roles
        description: create role in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: 
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
    pass


@bp.route('/role/<uuid:role_uid>', methods=["GET"])
def getRole(role_uuid):
    """get role info in project
    ---
    get:
        summary: get role info in project
        tags:
            - Roles
        description: get role info in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: GetRoleSchemaResponse
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
    pass


@bp.route('/role/update/<uuid:role_uuid>', methods=["GET"])
def updateRole(role_uuid):
    """update role in project
    ---
    put:
        summary: update role in project
        tags:
            - Roles
        description: update role in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: 
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
    pass


@bp.route('/role/<uuid:role_uuid>', methods=["DELETE"])
def deleteRole(role_uuid):
    """delete role in project
    ---
    delete:
        summary: delete role in project
        tags:
            - Roles
        description: delete role in project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                required: true
                schema:
                    type: string

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: 
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
    pass
