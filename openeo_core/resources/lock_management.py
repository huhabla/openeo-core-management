# -*- coding: utf-8 -*-
from flask import jsonify, make_response
from copy import deepcopy
from flask_restful_swagger_2 import swagger
from flask_restful import Resource
from openeo_core.resources.common.response_models import ProcessingResponseModel


__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"


class ResourceLockManagementResponseModel(ProcessingResponseModel):
    """The response content that is returned by the GET request
    """
    type = 'object'
    properties =  deepcopy(ProcessingResponseModel.properties)
    properties["process_results"] = {}
    properties["process_results"]["type"] = "boolean"
    required =  deepcopy(ProcessingResponseModel.required)


class ResourceLockManagementResource(Resource):
    """Lock a mapset
    """
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
                'schema':ResourceLockManagementResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':ProcessingResponseModel
            }
        }
    })
    def get(self, location_name, mapset_name):
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
            }
        ],
        'responses': {
            '200': {
                'description': 'Success message if the resource was locked successfully',
                'schema':ProcessingResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':ProcessingResponseModel
            }
        }
    })
    def post(self, location_name, mapset_name):
        """Lock a mapset
        """
        return make_response(jsonify("Resource locked"), 200)

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
                'schema':ProcessingResponseModel
            },
            '400': {
                'description': 'The error message',
                'schema':ProcessingResponseModel
            }
        }
    })
    def delete(self, location_name, mapset_name):
        """Unlock a locked resource
        """
        return make_response(jsonify("Resource unlocked"), 200)
