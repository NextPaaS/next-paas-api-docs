import logging
import sys
from src.api import bp
from src.schema.error_schema import *
from src.schema.taskEvent_schema import *
from src.schema.role_schema import *
from flask import jsonify, request


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@bp.route('/resources', methods=["GET"])
def listResource():
    """list resource service
    ---
    get:
        summary: list resource service
        tags:
            - Resources
        description: list resource service
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string            
            -   name: service_name
                in: query
                schema:
                    type: string
                description: service name
            # -   name: sortField
            #     in: query
            #     schema:
            #         type: string
            #         enum: [email, createdAt]
            #     description: sort field 
            # -   name: sort
            #     in: query
            #     schema:
            #         type: string
            #         enum: [asc, desc]
            #     description: >
            #         Sort order:
            #             * `email:asc` - Ascending, from A to Z
            #             * `email:desc` - Descending, from Z to A
            #             * `createdAt:asc` - Ascending, from A to Z
            #             * `createdAt:desc` - Descending, from Z to A
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
                        schema: ListResourceSchemaResponse
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
            },{
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
            },{
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
            },{
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
            },{
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