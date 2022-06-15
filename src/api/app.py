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
                required: true
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

@bp.route('/app/logs', methods=["GET"])
def logApp():
    """
    Get logs of an application
    ---
    get:
        summary: Get logs of an application
        tags:
        - Apps
        description: Get logs of an application
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
                        schema:
                            type: string
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

@bp.route('/app/events', methods=["GET"])
def eventApp():
    """
    Get events of an application
    ---
    get:
        summary: Get events of an application
        tags:
        - Apps
        description: Get events of an application
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
                        schema: ListEventSchema
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

@bp.route('/app/resource/plan', methods=["GET,PUT"])
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
                required: true
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
    put:
        summary: Update plan of Application
        tags:
        - Apps
        description: Update plan of Application
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
            -   name: plan
                in: query
                description: New plan
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

@bp.route('/app/volume', methods=["GET","PUT","POST","DELETE"])
def volume():
    """
    Volume attach to an application
    ---
    get:
        summary: Get all volumes
        tags:
        - Apps
        description: Get all volumes
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
        summary: Create a volume
        tags:
        - Apps
        description: Create a volume
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: volumename
                in: query
                description: Name of volume
                example: temp-volume
                required: true
                schema:
                    type: string
            -   name: plan
                in: query
                description: Plan of volume
                example: nfs
                required: true
                schema:
                    type: string
            -   name: capacity
                in: query
                description: Size of volume
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
    put:
        summary: Update a volume
        tags:
        - Apps
        description: Update a volume
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: volumename
                in: query
                description: Name of volume
                example: temp-volume
                required: true
                schema:
                    type: string
            -   name: capacity
                in: query
                description: Size of volume
                example: 30
                required: true
                schema:
                    type: int
        responses:
            200:
                description: Delete Volume Successfully
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
        summary: Delete a volume
        tags:
        - Apps
        description: Delete a volume
        parameters:
            -   name: cookie
                in: header
                description: cookie for authentication
                example: QvJ9NLWOPi5v0XM2tOnz0neVdNI5489AkVw2tUPFsU0NHF7hyn
                required: true
                schema:
                    type: string
            -   name: volumename
                in: query
                description: Name of volume
                example: temp-volume
                required: true
                schema:
                    type: string
        responses:
            200:
                description: Delete Volume Successfully
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

@bp.route('/app/volume/bind', methods=["GET,POST,DELETE"])
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
                required: true
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
        summary: Bind a volume to an application
        tags:
        - Apps
        description: Bind a volume to an application
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
            -   name: volumename
                in: query
                description: Name of volume
                example: temp-volume
                required: true
                schema:
                    type: string
            -   name: mountpoint
                in: query
                description: Mount point of volume in application
                example: /tmp/log
                required: true
                schema:
                    type: string
            -   name: readonly
                in: query
                description: Mount point of volume in application
                schema:
                    type: boolean
                    default: false
            -   name: norestart
                in: query
                description: Restart application after bind volume
                schema:
                    type: boolean
                    default: false
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
        summary: Unbind a volume 
        tags:
        - Apps
        description: Unbind a volume 
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
            -   name: volumename
                in: query
                description: Name of volume
                example: temp-volume
                required: true
                schema:
                    type: string
            -   name: mountpoint
                in: query
                description: Mount point of volume in application
                example: /tmp/log
                required: true
                schema:
                    type: string
            -   name: readonly
                in: query
                description: Mount point of volume in application
                schema:
                    type: boolean
                    default: false
            -   name: norestart
                in: query
                description: Restart application after bind volume
                schema:
                    type: boolean
                    default: false
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

@bp.route('/app/env', methods=["GET","POST","DELETE"])
def getAppEnv():
    """
    Get all environment variables of application 
    ---
    get:
        summary: Get all environment variables of application 
        tags:
        - Apps
        description: Get all environment variables of application 
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
                        schema: EnvListSchema
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
        summary: Add new env variable into an application 
        tags:
        - Apps
        description: Add new env variable into an application 
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
            -   name: key
                in: query
                description: Name of the key
                example: PORT
                required: true
                schema:
                    type: string
            -   name: value
                in: query
                description: value of the key
                example: 8888
                required: true
                schema:
                    type: string
            -   name: public
                in: query
                description: Scope of the key
                example: false
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
        summary: Delete an env variable in an application
        tags:
        - Apps
        description: Delete an env variable in an application
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
            -   name: key
                in: query
                description: Name of the key
                example: PORT
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


@bp.route('/app/resource/unit', methods=["GET","POST"])
def getAppUnits():
    """
    Get all units of an Application
    ---
    get:
        summary: Get all units of an Application
        tags:
        - Apps
        description: Get all units of an Application
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
                        schema: UnitSchema
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
        summary: Update number of units in application
        tags:
        - Apps
        description: Update number of units in application
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
            -   name: process
                in: query
                description: Name of process
                example: web
                schema:
                    type: string
            -   name: units
                in: query
                description: New number of units
                example: 10
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


@bp.route('/app/resource/autoscale', methods=["GET", "POST", "DELETE"])
def getAppAutoscale():
    """
    Get autoscale policy of an application 
    ---
    get:
        summary: Get autoscale policy of an application 
        tags:
        - Apps
        description: Get autoscale policy of an application 
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
                        schema: AutoScaleSchema
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
        summary: Create autoscale policy for application 
        tags:
        - Apps
        description: Create autoscale policy for application 
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
            -   name: process
                in: query
                description: Name of process
                required: true
                schema:
                    type: string
            -   name: minUnits
                in: query
                description: min units
                required: true
                schema:
                    type: int
            -   name: maxUnits
                in: query
                description: max units
                required: true
                schema:
                    type: int
            -   name: avgCPU
                in: query
                description: Average CPU to active autoscale
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
    
    delete:
        summary: Delete autoscale policy of application
        tags:
        - Apps
        description: Delete autoscale policy of application
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
                description: Remove autoscale successfully
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

@bp.route('/app/action/create', methods=["POST"])
def createApp():
    """
    Create an Application
    ---
    post:
        summary: Create application 
        tags:
        - Apps
        description: Create application 
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
            -   name: platform
                in: query
                description: Platform of application
                example: python
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

@bp.route('/app/action/delete', methods=["DELETE"])
def deleteApp():
    """
    Delete an Application
    ---
    delete:
        summary: Delete application 
        tags:
        - Apps
        description: Delete application 
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

@bp.route('/app/action/restart', methods=["POST"])
def restartApp():
    """
    Restart an Application
    ---
    post:
        summary: Restart an application 
        tags:
        - Apps
        description: Restart an application 
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

@bp.route('/app/action/start', methods=["POST"])
def startApp():
    """
    Start an Application
    ---
    post:
        summary: Start an application 
        tags:
        - Apps
        description: Start an application 
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

@bp.route('/app/action/stop', methods=["POST"])
def stopApp():
    """
    Stop an Application
    ---
    post:
        summary: Stop an application 
        tags:
        - Apps
        description: Stop an application 
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

@bp.route('/app/action/rollback', methods=["POST"])
def rollbackApp():
    """
    Rollback an Application
    ---
    post:
        summary: Rollback an application to older version
        tags:
        - Apps
        description: Rollback an application to older version
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
            -   name: version
                in: query
                description: Version of application
                example: v3
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

@bp.route('/app/action/deploy', methods=["POST"])
def deployApp():
    """
    Deploy exist Application
    ---
    post:
        summary: Deploy an application 
        tags:
        - Apps
        description: Deploy an application 
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
            -   name: image
                in: query
                description: Url Image of application
                example: http://registry.com/app:v1
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