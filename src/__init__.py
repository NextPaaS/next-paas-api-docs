import os
import yaml
from flask import Flask, jsonify
from conf import config
from apispec import APISpec
from apispec.utils import validate_spec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory
from src.api.taskEventId import listTaskEvent
from flask_cors import CORS

env = os.getenv("ENV", "development")

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['JSON_SORT_KEYS'] = False
    CORS(app, origins=[
			"https://staging.bizflycloud.vn",
            "https://staging2.bizflycloud.vn",
            "https://dev-iam.bizflycloud.vn",
			"https://beta-staging.vccloud.vn",
            "https://beta-staging2.bizflycloud.vn",
            "https://manage.bizflycloud.vn",
            "https://hn.manage.bizflycloud.vn",
            "https://hcm.manage.bizflycloud.vn",
			"https://*.vccloud.vn",
			"http://*.bizflycloud.vn:8081",
			"http://*.bizflycloud.vn:8080",
			"http://local.bizflycloud.vn:8080",
			"http://local.bizflycloud.vn:8000",
			"http://hn-local.bizflycloud.vn",
			"http://hcm-local.bizflycloud.vn",
			"http://hn-local.bizflycloud.vn:8000",
			"http://hn-local.bizflycloud.vn:8080",
			"http://hcm-local.bizflycloud.vn:8000",
			"http://hcm-local.bizflycloud.vn:8080",
			"http://hn-local.manage.bizflycloud.vn",
			"http://hcm-local.manage.bizflycloud.vn",
			"http://hn-local.manage.bizflycloud.vn:8080",
			"http://hcm-local.manage.bizflycloud.vn:8080",
        ], expose_headers=["Content-Length"], 
        supports_credentials=True
    )

    OPENAPI_SPEC = """
        servers:
        - url: http://127.0.0.1:9997/
        - url: https://staging.bizflycloud.vn/api/iam/v2
        - url: https://staging2.bizflycloud.vn/api/iam/v2
        - url: https://manage.bizflycloud.vn/api/iam/v2
        - url: https://dev-iam.bizflycloud.vn/api/iam/v2
    """

    settings = yaml.safe_load(OPENAPI_SPEC)
    spec = APISpec(
        title='OpenAPI for iam v2 public api',
        version='1.0.0',
        openapi_version='3.0.2',
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
        **settings
    )
    validate_spec(spec)
    @app.route('/')
    def introduce():
        return jsonify({
            "auth": "Thifnmi",
            "full name": "Tu Van Thin",
            "email": {
                "VCCorp": "thintuvan@vccorp.vn",
                "VCCloud": "thintv@vccloud.vn"
            },
            "telegram": "@Thifnmi"
        })

    @app.route('/api-docs')
    def api_docs():
        return jsonify(spec.to_dict())

    from src.api import bp
    app.register_blueprint(bp)

    from src.api.project import listProject, getProject, getUserProject, updateProject, deleteProject, createProject
    from src.api.healthCheck import healthCheck
    from src.api.taskEventId import getTaskEvent
    from src.api.user import listUser, inviteUser, getUser, updateUser, deleteUser, getProjectsOfUser
    from src.api.role import createRole, getRole, updateRole, listRole, deleteRole
    from src.api.permission import listResource

    with app.test_request_context():
        spec.path(view=healthCheck)
        spec.path(view=listTaskEvent)
        spec.path(view=getTaskEvent)
        spec.path(view=listProject)
        spec.path(view=getProject)
        spec.path(view=getUserProject)
        spec.path(view=createProject)
        spec.path(view=updateProject)
        spec.path(view=deleteProject)
        spec.path(view=listUser)
        spec.path(view=getProjectsOfUser)
        spec.path(view=getUser)
        spec.path(view=inviteUser)
        spec.path(view=updateUser)
        spec.path(view=deleteUser)
        spec.path(view=listRole)
        spec.path(view=getRole)
        spec.path(view=createRole)
        spec.path(view=updateRole)
        spec.path(view=deleteRole)
        spec.path(view=listResource)

    @app.route('/docs')
    @app.route('/docs/<path:path>')
#    @app.route('/<path:uri>/docs/<path:path>')
    def swagger_docs(uri=None, path=None):
        if not path or path == 'index.html':
            return render_template('index.html', base_url=f"/api/iam/v2/docs")
#            if uri == None:
#                return render_template('index.html', base_url=f"/docs")
#            else:
#                return render_template('index.html', base_url=f"{uri}/docs")
        else:
            return send_from_directory('../static', path)
    return app
