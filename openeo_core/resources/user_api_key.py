# -*- coding: utf-8 -*-

from flask import jsonify, make_response
from flask_restful import Resource
from flask_restful_swagger_2 import Schema, swagger


__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"


class TokenResponseModel(Schema):
    """Response schema that is used for authentication token generation.

    """
    type = 'object'
    properties = {
        'status': {
            'type': 'string',
            'description': 'The status of the resource, values: success, error'
        },
        'token': {
            'type': 'string',
            'description': 'The generated token for authentication'
        },
        'message': {
            'type': 'string',
            'description': 'The message of the token generation'
        }
    }
    required = ["status", "token"]


class APIKeyCreationResource(Resource):
    """Get an API key that has no expiration time
    """

    @swagger.doc({
        'tags': ['api key management'],
        'description': 'Create an API key for permanent authentication. API keys have no expiration time. '
                       'Minimum required user role: admin.',
        'responses': {
            '200': {
                'description': 'The API key generation response',
                'schema':TokenResponseModel
            },
            '400': {
                'description': 'The error message in case of failure',
                'schema':TokenResponseModel
            }
        }
    })
    def get(self):
        try:
            return make_response(jsonify(TokenResponseModel(status="success",
                                                            token="Jo",
                                                            message="API key successfully generated")), 200)
        except:
            return make_response(jsonify(TokenResponseModel(status="error",
                                                            token="",
                                                            message="Error while generating API key")), 400)


class TokenCreationResource(Resource):
    """Get an authorization token
    """

    @swagger.doc({
        'tags': ['api key management'],
        'description': 'Create an authentication token. Tokens have an expiration time. '
                       'The default expiration time is one day (86400s). maximum length is 365 days. '
                       'Minimum required user role: user.',
        'parameters': [
            {
                'name': 'expiration_time',
                'description': 'The expiration time in seconds for the generated token',
                'required': False,
                'in': 'query',
                'type': 'integer',
                'default': '86400'
            }],
        'responses': {
            '200': {
                'description': 'The token generation response',
                'schema':TokenResponseModel
            },
            '400': {
                'description': 'The error message in case of failure',
                'schema':TokenResponseModel
            }
        }
    })
    def get(self):

        try:
            return make_response(jsonify(TokenResponseModel(status="success",
                                                            token="Jo",
                                                            message="API key successfully generated")), 200)
        except:
            return make_response(jsonify(TokenResponseModel(status="error",
                                                            token="",
                                                            message="Error while generating API key")), 400)
