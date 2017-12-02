# -*- coding: utf-8 -*-

import cPickle
import time
from datetime import datetime
from flask import jsonify
from flask_restful_swagger_2 import Schema
from copy import deepcopy

__author__     = "Sören Gebbert"
__copyright__  = "Copyright 2016, Sören Gebbert"
__maintainer__ = "Sören Gebbert"
__email__      = "soerengebbert@googlemail.com"


class ProgressInfoModel(Schema):
    """This class defines the model for progress information.

    Progress information is generated in case a chain of several commands is processed.
    """
    type = 'object'
    properties = {
        'step': {
            'type': 'integer',
            'format': 'int64',
            'description': 'The current step of processing'
        },
        'num_of_steps': {
            'type': 'integer',
            'format': 'int64',
            'description': 'The total number of processing steps'
        },
        'sub_step': {
            'type': 'integer',
            'format': 'int64',
            'description': 'The current sub step of the current processing step'
        },
        'num_of_sub_steps': {
            'type': 'integer',
            'format': 'int32',
            'description': 'The total number of sub steps of the current processing step'
        },
    }
    required = ['step', 'num_of_steps']

    example = {
        "num_of_steps": 6,
        "step": 6
      }


class ProcessLogModel(Schema):
    """This class defines the model for Unix process information.

    Each time a Unix process
    is invoked, this model must be used to inform the user of the return process state. Each process
    has parameters, stdout/stderr output and a return value. This model is not designed to inform
    about running processes, but about finished processes.
    """
    type = 'object'
    properties = {
        'executable': {
            'type': 'string',
            'description': 'The name of the executable that was executed'
        },
        'parameter': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': 'The parameter of the executable that was executed'
        },
        'stdout': {
            'type': 'string',
            'description': 'The stdout output of the executable'
        },
        'stderr': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': 'The stderr output of the executable as list of strings'
        },
        'return_code': {
            'type': 'number',
            'format': 'int32',
            'description': 'The return code of the executable'
        },
        'run_time': {
            'type': 'number',
            'format': 'float',
            'description': 'The runtime of the executable in seconds'
        }
    }
    required = ['executable', 'parameter', 'stdout', 'stderr', 'return_code']

    example = {
      "executable": "g.region",
      "parameter": [
        "raster=elevation@PERMANENT",
        "res=10000",
        "-p",
        "--v"
      ],
      "return_code": 0,
      "stderr": [
        "NS resolution has been changed",
        "EW resolution has been changed",
        "NS and EW resolutions are different",
        ""
      ],
      "stdout": "projection: 99 (Lambert Conformal Conic)\nzone:       0\ndatum:      nad83\nellipsoid:  a=6378137 es=0.006694380022900787\nnorth:      228500\nsouth:      215000\nwest:       630000\neast:       645000\nnsres:      13500\newres:      7500\nrows:       1\ncols:       2\ncells:      2\n"
    }


class UrlModel(Schema):
    """URL schema that points to the status URL
    of the resource and to all generated resources (files, images, ...).

    """
    type = 'object'
    properties = {
        'status': {
            'type': 'string',
            'description': 'The URL to check the status of the resource'
        },
        'resources': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': 'A list of URLs to generated resources'
        }
    }
    required = ["status", "resources"]


class SimpleResponseModel(Schema):
    """Response schema that is used in cases that no asynchronous run was performed.

    """
    type = 'object'
    properties = {
        'status': {
            'type': 'string',
            'description': 'The status of the resource, values: accepted, running, finished, terminated, error'
        },
        'message': {
            'type': 'string',
            'description': 'A simple message to describes the status of the resource'
        }
    }
    required = ["status", "message"]


class ApiInfoModel(Schema):
    """Response schema that contains API information of the called endpoint.

    This information is used in the ProcessResponseModel schema and
    important for the accounting system.

    """
    type = 'object'
    properties = {
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
        'request_url': {
            'type': 'string',
            'description': 'The request URL'
        }
    }
    required = ["endpoint", "method", "path", "request_url"]

    example = {
        "endpoint": "asyncephemeralresource",
        "method": "POST",
        "path": "/locations/nc_spm_08/processing_async",
        "request_url": "http://localhost/locations/nc_spm_08/processing_async"
      }


class ProcessingResponseModel(Schema):
    """This is the base class for all asynchronous response models. This class must
    or a derivative must be used in all asynchronous responses. Usually
    specify derivatives different process_result schemas.

    """
    type = 'object'
    properties = {
        'status': {
            'type': 'string',
            'description': 'The status of the response'
        },
        'user_id': {
            'type': 'string',
            'description': 'The id of the user that issued a request'
        },
        'resource_id': {
            'type': 'string',
            'description': 'The unique resource id'
        },
        'process_log': {
            'type': 'array',
            'items': ProcessLogModel,
            'description': 'A list of ProcessLogModels'
        },
        'process_results': {
            'type': 'string',
            'description': 'An arbitrary class that stores the processing results'
        },
        'progress': ProgressInfoModel,
        'message': {
            'type': 'string',
            'description': 'Message for the user, maybe status, finished or error message'
        },
        'accept_timestamp': {
            'type': 'number',
            'format': 'double',
            'description': 'The acceptance timestamp in seconds of the response'
        },
        'accept_datetime': {
            'type': 'string',
            'description': 'The acceptance timestamp of the response in human readable format'
        },
        'timestamp': {
            'type': 'number',
            'format': 'double',
            'description': 'The current timestamp in seconds of the response'
        },
        'time_delta': {
            'type': 'number',
            'format': 'double',
            'description': 'The time delta of the processing in seconds'
        },
        'datetime': {
            'type': 'string',
            'description': 'The current timestamp of the response in human readable format'
        },
        'http_code': {
            'type': 'number',
            'format': 'int32',
            'description': 'The HTTP code of the response'
        },
        'urls': UrlModel,
        'api_info': ApiInfoModel
    }
    required = ['status', 'user_id', 'resource_id', 'timestamp', 'datetime', 'accept_timestamp',
                'accept_datetime', 'message']

    example = {
      "accept_datetime": "2017-05-24 22:37:21.607255",
      "accept_timestamp": 1495658241.607252,
      "api_info": {
        "endpoint": "asyncephemeralresource",
        "method": "POST",
        "path": "/locations/nc_spm_08/processing_async",
        "request_url": "http://localhost/locations/nc_spm_08/processing_async"
      },
      "datetime": "2017-05-24 22:37:21.608717",
      "http_code": 200,
      "message": "Resource accepted",
      "process_results": {},
      "resource_id": "resource_id-2be8cafe-b451-46a0-be15-f61d95c5efa1",
      "status": "accepted",
      "timestamp": 1495658241.608716,
      "urls": {
        "resources": [],
        "status": "http://localhost/status/admin/resource_id-2be8cafe-b451-46a0-be15-f61d95c5efa1"
      },
      "user_id": "admin"
    }


class ProcessingResponseListModel(Schema):
    """Response schema that represent a list of ProcessingResponseModel's
    """
    type = 'object'
    properties = {
        'resource_list': {
            'type': 'array',
            'items': ProcessingResponseModel,
            'description': 'A list of ProcessingResponseModel objects'
        }
    }
    required = ["resource_list"]

