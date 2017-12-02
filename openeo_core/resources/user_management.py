# -*- coding: utf-8 -*-
"""The user specific resources

This module specifies all endpoints to manage user accounts
in the redis database via REST API calls.

TODO: Implement POST full permission creation
      Implement PUT to modify existing users
"""

from flask import jsonify, make_response
from flask_restful import reqparse
from flask_restful import Resource


__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"


class UserAuthentificationResource(Resource):
    """Authentify a single user

    """
    def get(self, user_id, password):
        """Return True if the user is valid
        """
        return make_response(jsonify({"Status":"success", "Messages":"User %s is valid"%user_id}), 200)


class UserListResource(Resource):
    """List all user in the database.
    """
    def get(self):
        """List all users in the database

        These methods work only if the
        authorized user has an admin role.

        Returns:
            flask.Response: A HTTP response with
                            JSON payload containing a list of users

            A HTTP status 200 response JSON content::

                {
                  "Status": "success",
                  "User list": [
                    "soeren"
                  ]
                }

        """
        return make_response(jsonify({"Status":"success",
                                      "User list":[]}))

class UserManagementResource(Resource):
    """Get, Create and Delete a single user

    These methods work only if the
    authorized user has an admin role.

    Only normal users (role=user) can be created with this class.

    """


    def get(self, user_id):
        """Return the credentials of a single user
        """
        return make_response(jsonify({"Status":"success", "Messages":"User %s"%user_id}), 200)

    def post(self, user_id):
        """Create a user in the database
        """

        return make_response(jsonify({"Status":"success", "Messages":"User %s created"%user_id}), 200)

    def delete(self, user_id):
        """Delete a specific user
        """
        return make_response(jsonify({"Status":"success", "Messages":"User %s deleted"%user_id}), 200)

