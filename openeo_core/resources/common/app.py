# -*- coding: utf-8 -*-

from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from flask import Flask
# from flask_socketio import SocketIO
# Instead of using this: from flask.ext.restful import  Api
# Use this:
from flask_restful_swagger_2 import Api, swagger

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Soeren Gebbert"
__email__      = "soerengebbert@googlemail.com"

flask_app = Flask(__name__)
CORS(flask_app)

flask_api = Api(flask_app, api_version='0.1pre-alpha', api_spec_url='/api/swagger',
                title="openEO core management",
                description="openEO core management",
                consumes=['application/gml+xml', 'application/json'])

# Set the security definition in an unconventional way
flask_api._swagger_object["securityDefinitions"] = {"basicAuth":{"type": "basic"}}
flask_api._swagger_object["security"]=[{"basicAuth":[]}]

auth = HTTPBasicAuth()
