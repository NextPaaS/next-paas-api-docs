from crypt import methods
import logging
import sys
from src.api import bp
from src.schema.error_schema import *
from src.schema.taskEvent_schema import *
from src.schema.role_schema import *
from flask import jsonify, request


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@bp.route('/app', methods=["GET"])

@bp.route('/app/info', methods=["GET"])
def getAppInfo():
    """
    Get information of an Application
    ---
    get:
        summary: Get information of an Application
        tags:
            - Apps
        description: Get information of an Application
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
                schema:
                    type: string
        responses:
            200:
                description: Success Response
                content:
                    application/json:
                        schema: ApplicationInfoSchema
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

@bp.route('/app/resource/plan', methods=["GET"])
def getAppPlan():
    """
    Get plan of Application
    ---
    get:
        summary: Get plan of Application
        tags:
        - Apps
        description: Get plan of Application
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
                schema:
                    type: string
        responses:
            200:
                description: Success Response
                content:
                    application/json:
                        schema: ApplicationResourceSchema
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

@bp.route('/app/volume/bind', methods=["GET"])
def getBindVolume():
    """
    Get volumes already bind to an Application
    ---
    get:
        summary: Get volumes already bind to an Application
        tags:
        - Apps
        description: Get volumes already bind to an Application
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
                schema:
                    type: string
        responses:
            200:
                description: Success Response
                content:
                    application/json:
                        schema: VolumeSchema
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