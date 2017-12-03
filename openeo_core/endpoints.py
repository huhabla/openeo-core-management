#!flask/bin/python
# -*- coding: utf-8 -*-
"""
Endpoint definitions
"""

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Soeren Gebbert"
__email__      = "soerengebbert@googlemail.com"

from resources.common.app import flask_api


def create_endpoints():

    from resources.lock_management import ResourceLockManagementResource

    flask_api.add_resource(ResourceLockManagementResource, '/lock/<string:resource_id>')

    from resources.user_management import UserListResource, UserManagementResource
    from resources.api_log_management import APILogResource
    from resources.user_api_key import TokenCreationResource, APIKeyCreationResource

    flask_api.add_resource(UserListResource, '/users')
    flask_api.add_resource(UserManagementResource, '/users/<string:user_id>')
    flask_api.add_resource(TokenCreationResource, '/token', )
    flask_api.add_resource(APIKeyCreationResource, '/api_key', )
    flask_api.add_resource(APILogResource, '/api_log/<string:user_id>')

    from resources.resource_management import ResourceManager, ResourcesManager

    flask_api.add_resource(ResourceManager, '/status/<string:user_id>/<string:resource_id>')
    flask_api.add_resource(ResourcesManager, '/resources/<string:user_id>')
