from crypt import methods
import logging
import sys
from src.api import bp
from src.schema.error_schema import *
from src.schema.taskEvent_schema import *
from src.schema.role_schema import *
from src.schema.success_schema import *
from flask import jsonify, request

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@bp.route('/app/service', methods=["GET"])
def serviceInfo():
    """
    Services is database or broker
    ---
    get:
        summary: Get all services
        tags:
        - Apps
        description: Get all services
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
                description: Success Response
                content:
                    application/json:
                        schema: ListServiceSchema
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
                description: Application Not Found
                content:
                    application/json:
                        schema: PageNotFound
            500:
                description: Server Error
                content:
                    application/json:
                        schema: ServerError
    """

@bp.route('/app/service/bind', methods=["GET,POST,DELETE"])
def BindService():
    """
    Create a service and bind into application
    ---
    get:
        summary: Get services already bind to an Application
        tags:
        - Apps
        description: Get services already bind to an Application
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: app
                in: query
                description: Name of application
                example: python-application
                required: true
                schema:
                    type: string
        responses:
            200:
                description: Success Response
                content:
                    application/json:
                        schema: ListServiceSchema
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
                description: Application Not Found
                content:
                    application/json:
                        schema: PageNotFound
            500:
                description: Server Error
                content:
                    application/json:
                        schema: ServerError
    post:
        summary: Create service and bind to application
        tags:
        - Apps
        description: Create service and bind to application
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: appname
                in: query
                description: Name of application
                example: python-application
                required: true
                schema:
                    type: string
            -   name: servicename
                in: query
                description: Name of service
                example: mysql-production
                required: true
                schema:
                    type: string
            -   name: servicetype
                in: query
                description: type of services
                example: mysql
                required: true
                schema:
                    type: string
            -   name: plan
                in: query
                description: Plan of services
                example: 1c_1g
                required: true
                schema:
                    type: string
        responses:
            200:
                description: Success Response
                content:
                    application/json:
                        schema: DefaultSuccess
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
                description: Application Not Found
                content:
                    application/json:
                        schema: PageNotFound
            500:
                description: Server Error
                content:
                    application/json:
                        schema: ServerError

    delete:
        summary: Delete service
        tags:
        - Apps
        description: Delete service
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: app
                in: query
                description: Name of application
                example: python-application
                required: true
                schema:
                    type: string
            -   name: servicename
                in: query
                description: Name of volume
                example: mysql-production
                required: true
                schema:
                    type: string
        responses:
            200:
                description: Success Response
                content:
                    application/json:
                        schema: DefaultSuccess
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
                description: Application Not Found
                content:
                    application/json:
                        schema: PageNotFound
            500:
                description: Server Error
                content:
                    application/json:
                        schema: ServerError
    
    """