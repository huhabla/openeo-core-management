#!flask/bin/python
# -*- coding: utf-8 -*-

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Soeren Gebbert"
__email__      = "soerengebbert@googlemail.com"

from resources.common.app import flask_app
from resources.common.config import global_config
from flask import make_response, jsonify

# Return the version of GRaaS as REST API call
@flask_app.route('/version')
def version():
    """Return the version information and the roles that are activated

    Returns: Response

    """
    info = {"version":"0.01", "roles":global_config.ROLES}
    return make_response(jsonify(info), 200)
