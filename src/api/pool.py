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

@bp.route('/pool', methods=["GET", "POST", "PUT","DELETE"])
def pool():
    """
    Custom pool allow user can deploy in any place
    ---
    get:
        summary: Get all pools of user
        tags:
            - Pool
        description: Get all pools of user
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
                        schema: ListPool
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
        
    post:
        summary: Create pool
        tags:
            - Pool
        description: Create pool
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: pool_name
                in: query
                description: name of the pool
                required: true
                schema:
                    type: string
            -   name: address
                in: query
                description: Address of the pool
                required: true
                schema:
                    type: string
            -   name: default
                in: query
                description: set as a default pool
                required: true
                schema:
                    type: boolean

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
        summary: Update pool
        tags:
            - Pool
        description: Update pool
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: pool_name
                in: query
                description: name of the pool
                schema:
                    type: string
            -   name: address
                in: query
                description: Address of the pool
                schema:
                    type: string
            -   name: default
                in: query
                description: set as a default pool
                schema:
                    type: boolean

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
        summary: Create pool
        tags:
            - Pool
        description: Create pool
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: pool_name
                in: query
                description: name of the pool
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