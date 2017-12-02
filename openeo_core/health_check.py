#!flask/bin/python
# -*- coding: utf-8 -*-

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Soeren Gebbert"
__email__      = "soerengebbert@googlemail.com"

from resources.common.app import flask_app
from flask import make_response

# This is needed by Google load balancer
@flask_app.route('/health_check')
def health_check():
    return make_response("OK", 200)
