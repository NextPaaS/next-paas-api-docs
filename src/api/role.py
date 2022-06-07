import logging
import sys
import uuid
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
                "uuid": "b0a6dc1e-dda8-4562-b62c-007bb7993f25",
                "name": "Owner",
                "description": "role owner",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            {
                "uuid": "b0a6dc1e-dda8-4562-b62c-007bb7993f26",
                "name": "custom111",
                "description": "role custom leu leu leu",
                "is_custom": False,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": "2022-04-28T02:51:40.905Z",
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
    """create role
    ---
    post:
        summary: create role
        tags:
            - Roles
        description: create role
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
                    schema: CreateRoleSchema

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: CreateRoleSchemaResponse
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
    try:
        name = req['name']
        description = req['description']
        permissions = req['permissions']
        version = req['version']
        if req['version'] != "1.0.0":
            response = {
                'success': False,
                'error_code': 417,
                'message': 'Invalid version'
            }
            logging.info(e)
            return jsonify(response)
    except Exception as e:
        response = {
            'success': False,
            'error_code': 417,
            'message': 'Invalid body request'
        }
        logging.info(e)
        return jsonify(response)
    per = []
    try :
        for permission in permissions:
            effect = permission['effect']
            for action in permission['action']:
                for resource in permission['resources']:
                    endpoint = f"{resource}.{action}"
                    per.append(endpoint)
                    logging.info(f"endpoint: {endpoint}, action: {effect}")
    except Exception as e:
        response = {
            'success': False,
            'error_code': 417,
            'message': 'Invalid body request'
        }
        logging.info(e)
        return jsonify(response)
    data = {
        "task_event": {
            "task_event_id": uuid.uuid4(),
            "status": "success",
            "type": "create",
        },
        "role": {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": name,
            "description": description,
            "is_custom": True,
            "is_active": True,
            "created_at": "2022-06-01T08:48:45.351Z",
            "updated_at": None,
            "deleted_at": None,
        }
    }
    response = {
        "success": True,
        "message": "Create role %s success",
        "error_code": 0,
        "data": data
    }
    return jsonify(response)


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
                required: true
                schema:
                    type: string
                    format: uuid
                    enum: [b0a6dc1e-dda8-4562-b62c-007bb7993f25, b0a6dc1e-dda8-4562-b62c-007bb7993f26]

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
    if role_uuid == uuid.UUID("b0a6dc1e-dda8-4562-b62c-007bb7993f25"):
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
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffmf",
                    "name": "chua nghi ra",
                    "type": "Get",
                    "service_type": "infra",
                    "service_name": "Nen tang nhu mot dich vu",
                    "endpoint": "iaas-cloud.*",
                    "description": "toan quyen voi server",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                },
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                    "name": "chua nghi ra",
                    "type": "Get",
                    "service_type": "infra",
                    "service_name": "Cloud server",
                    "endpoint": "iaas-cloud.servers.*",
                    "description": "toan quyen voi server",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None
                },
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm8",
                    "name": "",
                    "type": "Create",
                    "service_type": "infra",
                    "service_name": "Cloud server",
                    "endpoint": "iaas-cloud.servers.create",
                    "description": "co quyen tao server",
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
                    "endpoint": "iaas-cloud.servers.details",
                    "description": "co quyen xem chi tiet server",
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
                    "endpoint": "iaas-cloud.servers.delete",
                    "description": "co quyen xoa server",
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
                    "endpoint": "iaas-cloud.servers.update",
                    "description": "co quyen update server",
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
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None, },
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm3",
                    "name": "",
                    "type": "Create",
                    "service_type": "infra",
                    "service_name": "Cloud server",
                    "endpoint": "iaas-cloud.volumes.create",
                    "description": "co quyen tao volumne",
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
                    "endpoint": "iaas-cloud.volumes.update",
                    "description": "co quyen update volumne",
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
                    "endpoint": "iaas-cloud.volumes.delete",
                    "description": "co quyen xoa volumne",
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
                    "endpoint": "iaas-cloud.volumes.details",
                    "description": "co quyen xem chi tiet volumne",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                },
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffmf",
                    "name": "chua nghi ra",
                    "type": "Get",
                    "service_type": "infra",
                    "service_name": "bizflydriver",
                    "endpoint": "cloud-storage.*",
                    "description": "toan quyen voi server",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None, },
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                    "name": "chua nghi ra",
                    "type": "Post",
                    "service_type": "infra",
                    "service_name": "bizflydriver",
                    "endpoint": "cloud-storage.create",
                    "description": "tao bizflydriver",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                }, {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                    "name": "chua nghi ra",
                    "type": "Get",
                    "service_type": "infra",      
                    "service_name": "bizflydriver",
                    "endpoint": "cloud-storage.drive",
                    "description": "get list drive",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                }
            ]
        }
    if role_uuid == uuid.UUID("b0a6dc1e-dda8-4562-b62c-007bb7993f26"):
        data = {
            "role": {
                "uuid": role_uuid,
                "name": "custom111",
                "description": "role custom leu leu leu",
                "is_custom": True,
                "is_active": True,
                "created_at": "2022-04-26T02:51:40.905Z",
                "updated_at": None,
                "deleted_at": None,
            },
            "resources": [
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm9",
                    "name": "",
                    "type": "Get",
                    "service_type": "infra",
                    "service_name": "Cloud server",
                    "endpoint": "iaas-cloud.servers.details",
                    "description": "co quyen xem chi tiet server",
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
                    "endpoint": "iaas-cloud.volumes.update",
                    "description": "co quyen update volumne",
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
                    "endpoint": "iaas-cloud.volumes.details",
                    "description": "co quyen xem chi tiet volumne",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                },
                {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                    "name": "chua nghi ra",
                    "type": "Post",
                    "service_type": "infra",
                    "service_name": "bizflydriver",
                    "endpoint": "cloud-storage.create",
                    "description": "tao bizflydriver",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                }, {
                    "uuid": "9be65172-e1d6-4e61-95ed-d35d92eeffm7",
                    "name": "chua nghi ra",
                    "type": "Get",
                    "service_type": "infra",      
                    "service_name": "bizflydriver",
                    "endpoint": "cloud-storage.drive",
                    "description": "get list drive",
                    "is_active": True,
                    "created_at": "2022-04-26T02:51:40.905Z",
                    "updated_at": None,
                    "deleted_at": None,
                }
            ]
        }
    response = {
        "success": True,
        "message": "get info role %s success" % role_uuid,
        "error_code": 0,
        "data": data,
    }
    return jsonify(response)


@bp.route('/role/update/<uuid:role_uuid>', methods=["PUT"])
def updateRole(role_uuid):
    """update role
    ---
    put:
        summary: update role
        tags:
            - Roles
        description: update role
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
                description: role uuid
                example: da28fd31-4f48-4c27-a478-2b6e917717b5
                required: true
                schema:
                    type: string
                    format: uuid
        requestBody:
            content:
                application/json:
                    schema: CreateRoleSchema

        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: UpdateRoleSchemaResponse
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
    try:
        name = req['name']
        description = req['description']
        permissions = req['permissions']
        version = req['version']
        if version != "1.0.0":
            response = {
                'success': False,
                'error_code': 417,
                'message': 'Invalid version'
            }
            logging.info(e)
            return jsonify(response)
    except Exception as e:
        response = {
            'success': False,
            'error_code': 417,
            'message': 'Invalid body request'
        }
        logging.info(e)
        return jsonify(response)
    per = []
    try :
        for permission in permissions:
            effect = permission['effect']
            for action in permission['action']:
                for resource in permission['resources']:
                    endpoint = f"{resource}.{action}"
                    per.append(endpoint)
                    logging.info(f"endpoint: {endpoint}, action: {effect}")
    except Exception as e:
        response = {
            'success': False,
            'error_code': 417,
            'message': 'Invalid body request'
        }
        logging.info(e)
        return jsonify(response)
    data = {
        "task_event": {
            "task_event_id": uuid.uuid4(),
            "status": "success",
            "type": "update",
        },
        "role": {
            "before_values": {
                "uuid": role_uuid,
                "name": "old name",
                "description": "old description",
                "is_custom": True,
                "is_active": True,
                "created_at": "2022-06-01T08:48:45.351Z",
                "updated_at": None,
                "deleted_at": None,
            }, "after_values": {
                "uuid": role_uuid,
                "name": name,
                "description": description,
                "is_custom": True,
                "is_active": True,
                "created_at": "2022-06-01T08:48:45.351Z",
                "updated_at": "2022-06-02T08:48:45.351Z",
                "deleted_at": None,
            }
        }
    }
    response = {
        "success": True,
        "message": "update role %s success",
        "error_code": 0,
        "data": data
    }
    return jsonify(response)


@bp.route('/role/delete/<uuid:role_uuid>', methods=["DELETE"])
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
