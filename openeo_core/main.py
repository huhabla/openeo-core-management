#!flask/bin/python
# -*- coding: utf-8 -*-

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Soeren Gebbert"
__email__      = "soerengebbert@googlemail.com"

import os

import endpoints
import health_check
import version
from resources.common.app import flask_app

endpoints.create_endpoints()

if __name__ == '__main__':
    # Connect to the database
    flask_app.run(debug=True)
