from crypt import methods
import logging
import sys
from src.api import bp
from src.schema.error_schema import *
from src.schema.taskEvent_schema import *
from src.schema.user_schema import *
from src.schema.success_schema import *
from flask import jsonify, request


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@bp.route('/user/info', methods=["GET", "PUT"])
def getUserInfo():
    """
    Get information of user
    ---
    get:
        summary: Get information of user
        tags:
            - User
        description: Get information of user
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
                        schema: UserInfo
            401:
                description: Access token is missing or invalid
                content:
                    application/json:
                        schema: UnauthorizedError
            403:
                description: Permission Deny
                content:
                    application/json:
                        schema: UnauthorizedError
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
    
    put:
        summary: Update information of user
        tags:
            - User
        description: Update information of user
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: quota
                in: query
                description: Update quota of user
                example: 10
                required: true
                schema:
                    type: int
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
                        schema: UnauthorizedError
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

@bp.route('/user/project', methods=["POST", "PUT", "DELETE"])
def userProject():
    """
    User vs Project
    ---
    post:
        summary: Add user to a project
        tags:
            - User
        description: Add user to a project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: user_name
                in: query
                description: Username of user
                required: true
                schema:
                    type: string
            -   name: project_name
                in: query
                description: Name of project
                required: true
                schema:
                    type: string
            -   name: role
                in: query
                description: role of user in project
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
                        schema: UnauthorizedError
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

    put:
        summary: Update user role in a project
        tags:
            - User
        description: Update user role in a project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: user_name
                in: query
                description: Username of user
                required: true
                schema:
                    type: string
            -   name: project_name
                in: query
                description: Name of project
                required: true
                schema:
                    type: string
            -   name: role
                in: query
                description: role of user in project
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
                        schema: UnauthorizedError
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
        summary: Delete user role in a project
        tags:
            - User
        description: Delete user role in a project
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: user_name
                in: query
                description: Username of user
                required: true
                schema:
                    type: string
            -   name: project_name
                in: query
                description: Name of project
                required: true
                schema:
                    type: string
            -   name: role
                in: query
                description: role of user in project
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
                        schema: UnauthorizedError
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