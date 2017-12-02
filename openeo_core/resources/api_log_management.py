# -*- coding: utf-8 -*-
"""
This module is designed to deliver the API calls of a specific user
"""
from flask import g
from flask import jsonify, make_response
from flask_restful import Resource

from flask_restful_swagger_2 import swagger
from flask_restful_swagger_2 import Schema

from core.resources.common.response_models import SimpleResponseModel

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"


class ApiLogEntryModel(Schema):
    """Response schema for a single API log entry that is used to track all API calls of a user.
    """
    type = 'object'
    properties = {
        'time_stamp': {
            'type': 'string',
            'description': 'The time stamp of the API call'
        },
        'node': {
            'type': 'string',
            'description': 'The node that executed the API call'
        },
        'endpoint': {
            'type': 'string',
            'description': 'The endpoint of the API call'
        },
        'method': {
            'type': 'string',
            'description': 'The HTTP method of the request'
        },
        'path': {
            'type': 'string',
            'description': 'The path of the REST API call'
        },
        'url': {
            'type': 'string',
            'description': 'The request URL'
        },
        'request_str': {
            'type': 'string',
            'description': 'The request string'
        }
    }
    required = ["time_stamp", "node", "endpoint",
                "method", "path", "url", "request_str"]


class ApiLogListModel(Schema):
    """Response schema that represents a list of API log entries.
    """
    type = 'object'
    properties = {
        'api_log_list': {
            'type': 'array',
            'items': ApiLogEntryModel,
            'description': 'A list of ApiLogEntryModel objects'
        }
    }
    required = ["api_log_list"]


class APILogResource(Resource):
    """API log management
    """

    def __init__(self):

    @swagger.doc({
        'tags': ['api_log'],
        'description': 'Get a list of all API calls that have been called by the provided user. ',
        'parameters': [
            {
                'name': 'user_id',
                'description': 'The unique user name/id',
                'required': True,
                'in': 'path',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Returned a list of all API calls that have been called by the provided user.',
                'schema':ApiLogListModel
            },
            '400': {
                'description': 'The error message why API log gathering did not succeeded',
                'schema':SimpleResponseModel
            }
        }
     })
    def get(self, user_id):
        return make_response(jsonify("API model"), 200)
