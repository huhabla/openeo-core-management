# -*- coding: utf-8 -*-
"""
This module is designed to deliver the API calls of a specific user
"""
from flask import jsonify, make_response
from flask_restful import Resource

from flask_restful_swagger_2 import swagger
from flask_restful_swagger_2 import Schema

from openeo_core.resources.common.response_models import SimpleResponseModel

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

    example = {u'endpoint': u'apilogresource',
               u'method': u'POST',
               u'node': u'node',
               u'path': u'/api_log',
               u'request_str': u"<Request 'http://localhost:5000/api_log' [POST]>",
               u'time_stamp': u'Fri, 01 Dec 2017 19:53:36 GMT',
               u'url': u'http://localhost:5000/api_log'}


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

    example = [{u'endpoint': u'apilogresource',
                u'method': u'POST',
                u'node': u'node',
                u'path': u'/api_log',
                u'request_str': u"<Request 'http://localhost:5000/api_log' [POST]>",
                u'time_stamp': u'Fri, 01 Dec 2017 19:53:36 GMT',
                u'url': u'http://localhost:5000/api_log'},
               {u'endpoint': u'apilogresource',
                u'method': u'POST',
                u'node': u'node',
                u'path': u'/api_log',
                u'request_str': u"<Request 'http://localhost:5000/api_log' [POST]>",
                u'time_stamp': u'Fri, 01 Dec 2017 19:53:36 GMT',
                u'url': u'http://localhost:5000/api_log'},
               {u'endpoint': u'apilogresource',
                u'method': u'POST',
                u'node': u'node',
                u'path': u'/api_log',
                u'request_str': u"<Request 'http://localhost:5000/api_log' [POST]>",
                u'time_stamp': u'Fri, 01 Dec 2017 19:53:36 GMT',
                u'url': u'http://localhost:5000/api_log'},
               {u'endpoint': u'apilogresource',
                u'method': u'POST',
                u'node': u'node',
                u'path': u'/api_log',
                u'request_str': u"<Request 'http://localhost:5000/api_log' [POST]>",
                u'time_stamp': u'Fri, 01 Dec 2017 19:53:36 GMT',
                u'url': u'http://localhost:5000/api_log'}]


class APILogResource(Resource):
    """API log management
    """

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
        return make_response(jsonify("A list of API calls"), 200)


    @swagger.doc({
        'tags': ['api_log'],
        'description': 'Log an API call. ',
        'consumes':['application/json'],
        'parameters': [
            {
                'name': 'user_id',
                'description': 'The unique user name/id',
                'required': True,
                'in': 'path',
                'type': 'string'
            },
            {
                'name': 'api_log',
                'description': 'An API log entry',
                'required': True,
                'in': 'body',
                'schema': ApiLogEntryModel
            }
        ],
        'responses': {
            '200': {
                'description': 'API call entry successfully logged.',
                'schema':SimpleResponseModel
            },
            '400': {
                'description': 'The error message why API call logging did not succeeded',
                'schema':SimpleResponseModel
            }
        }
     })
    def post(self, user_id):
        return make_response(jsonify("API call logged"), 200)


