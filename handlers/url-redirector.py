'''
Return a redirect location set in the environment.
'''

import json
import logging
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

REDIRECT_LOCATION = os.environ.get('REDIRECT_LOCATION')
STATUS_CODE = int(os.environ.get('STATUS_CODE'))

def _get_location(redirect_location, path, parameters):
    '''Return the full location path'''
    location = redirect_location + path
    if parameters:
        location += '?' + '&'.join(parameters)
    return location


def _get_path_from_event(event):
    '''Get path from event'''
    return event.get('path')


def _get_query_parameters_from_event(event):
    '''Get query parameters from event'''
    query_parameters = event.get('queryStringParameters') or {}
    query_parameter_list = []
    for k in query_parameters:
        query_parameter_list.append('{}={}'.format(k, query_parameters.get(k)))
    return query_parameter_list


def handler(event, context):
    _logger.debug('Event received: {}'.format(json.dumps(event)))

    path = _get_path_from_event(event)
    query_parameters = _get_query_parameters_from_event(event)
    location = _get_location(REDIRECT_LOCATION, path, query_parameters)

    # Need to get URL from request so I can return full path
    return {
        'statusCode': STATUS_CODE,
        'headers': {
            'Location': location
        }
    }

