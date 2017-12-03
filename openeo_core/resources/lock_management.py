# -*- coding: utf-8 -*-
from flask import jsonify, make_response
from copy import deepcopy
from flask_restful_swagger_2 import swagger
from flask_restful import Resource
from openeo_core.resources.common.response_models import SimpleResponseModel


__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"



class ResourceLockManagementResource(Resource):

    @swagger.doc({
        'tags': ['resource locking'],
        'description': 'Return the resource lock status. ',
        'parameters': [
            {
                'name': 'resource_id',
                'description': 'The id of the resource that should be checked for locking',
                'required': True,
                'in': 'path',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'Get the resource lock status, either "True" or "None"',
                'schema':SimpleResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':SimpleResponseModel
            }
        }
    })
    def get(self, resource_id):
        """Get the lock status
        """
        return make_response(jsonify("Mapset locked?"), 200)

    @swagger.doc({
        'tags': ['resource locking'],
        'description': 'Create a resource lock.',
        'parameters': [
            {
                'name': 'resource_id',
                'description': 'The id of the resource that should be locked',
                'required': True,
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'expiration_time',
                'description': 'The expiration time in seconds for the created resource lock',
                'required': False,
                'in': 'query',
                'type': 'integer',
                'default': '3600'
            }
        ],
        'responses': {
            '200': {
                'description': 'Success message if the resource was locked successfully',
                'schema':SimpleResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':SimpleResponseModel
            }
        }
    })
    def post(self, resource_id):
        """Lock a mapset
        """
        return make_response(jsonify("Resource locked"), 200)

    @swagger.doc({
        'tags': ['resource locking'],
        'description': 'Extend the expiration time of a resource lock.',
        'parameters': [
            {
                'name': 'resource_id',
                'description': 'The id of the resource for which the locked should be extended',
                'required': True,
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'expiration_time',
                'description': 'The expiration time in seconds for the resource lock',
                'required': False,
                'in': 'query',
                'type': 'integer',
                'default': '3600'
            }
        ],
        'responses': {
            '200': {
                'description': 'Success message if the resource locked was successfully extended.',
                'schema':SimpleResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':SimpleResponseModel
            }
        }
    })
    def put(self, resource_id):
        """Lock a mapset
        """
        return make_response(jsonify("Resource locked extended"), 200)

    @swagger.doc({
        'tags': ['resource locking'],
        'description': 'Delete a resource lock.',
        'parameters': [
            {
                'name': 'resource_id',
                'description': 'The id of the resource for which the lock should be deleted.',
                'required': True,
                'in': 'path',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'Success message if the resource was unlocked successfully',
                'schema':SimpleResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':SimpleResponseModel
            }
        }
    })
    def delete(self, resource_id):
        """Unlock a locked resource
        """
        return make_response(jsonify("Resource unlocked"), 200)
