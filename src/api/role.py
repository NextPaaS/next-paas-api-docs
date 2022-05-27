import logging
import sys
from src.api import bp
from src.schema.error_schema import *
from src.schema.taskEvent_schema import *
from src.schema.role_schema import *
from flask import jsonify, request


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@bp.route('/roles', methods=["GET"])
def listRole():
    """list role created by user
    ---
    get:
        summary: list role created by user
        tags:
            - Roles
        description: list role created by user
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
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
    """create role CHUA CO MOCK API
    ---
    post:
        summary: create role CHUA CO MOCK API
        tags:
            - Roles
        description: create role CHUA CO MOCK API
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
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


@bp.route('/role/<uuid:role_uuid>', methods=["GET"])
def getRole(role_uuid):
    """get role info
    ---
    get:
        summary: get role info
        tags:
            - Roles
        description: get role info
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: role_uuid
                in: path
                description: role_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid

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
    data = {
        "role": {
            "uuid": role_uuid,
            "name": "Owner",
            "description": "role owner",
            "is_custom": False,
            "is_active": True,
            "created_at": "2022-04-26T02:51:40.905Z",
            "updated_at": None,
            "deleted_at": None,
        },
        "resources": [
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                "name": "chua nghi ra",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.servers.*",
                "description": "toan quyen voi server",
                "action": "allow",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm8",
                "name": "",
                "type": "Create",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.servers.create",
                "description": "co quyen tao server",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm9",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.servers.*.details",
                "description": "co quyen xem chi tiet server",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm6",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.volumes.*",
                "description": "toan quyen voi volumes",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm3",
                "name": "",
                "type": "Create",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.volumes.create",
                "description": "co quyen tao volumne",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm4",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.backup.*",
                "description": "toan quyen voi dich vu backup",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm0",
                "name": "",
                "type": "Create",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.backup.create",
                "description": "co quyen tao backup",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffz8",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Cloud server",
                "endpoint": "iaas-cloud.quotas.*",
                "description": "toan quyen voi quotas",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeff96",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Simple Storage",
                "endpoint": "simple-storage.listing",
                "description": "co quyen xem danh sach storage",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeff9x",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Simple Storage",
                "endpoint": "simple-storage.detail.*.files",
                "description": "co quyen xem chi tiet cac file",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeff66",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Simple Storage",
                "endpoint": "simple-storage.detail.*.settings",
                "description": "co quyen xem chi tiet cai dat",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeff65",
                "name": "",
                "type": "Get",
                "service_type": "infra",
                "service_name": "Simple Storage",
                "endpoint": "simple-storage.detail.*.statistics",
                "description": "khong nho mo ta",
                "action": "",
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
        ]
    }
    response = {
        "success": True,
        "message": "get info role %s success" % role_uuid,
        "error_code": 0,
        "data": data,
    }
    return jsonify(response)


@bp.route('/role/update/<uuid:role_uuid>', methods=["GET"])
def updateRole(role_uuid):
    """update role CHUA CO MOCK API
    ---
    put:
        summary: update role CHUA CO MOCK API
        tags:
            - Roles
        description: update role CHUA CO MOCK API
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: role_uuid
                in: path
                description: role_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid

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
    """delete role
    ---
    delete:
        summary: delete role
        tags:
            - Roles
        description: delete role
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: role_uuid
                in: path
                description: role_uuid
                example: b0a6dc1e-dda8-4562-b62c-007bb7993f25
                required: true
                schema:
                    type: string
                    format: uuid

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: TaskEventDeleteRoleResponse
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
    role = {
        "uuid": role_uuid,
        "name": "Custom role",
        "description": "Role custom",
        "is_custom": True,
        "is_active": True,
        "created_at": "2022-04-26T02:51:40.905Z",
        "updated_at": None,
        "deleted_at": None,
    }

    response = {
        "success": True,
        "message": "Delete role %s success",
        "error_code": 0,
        "data": [
            {
                "task_event": {
                    'task_event_id': "c8f044f9-b2fb-49fd-ace4-45d7c740d828",
                    'status': 'success',
                    'type': 'delete'
                }
            }, {
                "role": role
            }
        ]
    }

    return jsonify(response)
