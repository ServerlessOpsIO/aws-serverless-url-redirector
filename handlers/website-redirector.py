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

def handler(event, context):
    _logger.debug('Event received: {}'.format(json.dumps(event)))

    path = event.get('path')

    query_parameters = event.get('queryStringParameters') or {}
    query_parameter_list = []
    for k in query_parameters:
        query_parameter_list.append('{}={}'.format(k, query_parameters.get(k)))

    location = REDIRECT_LOCATION + event.get('path', '/') + '?' + '&'.join(query_parameter_list)

    # Need to get URL from request so I can return full path
    return {
        'statusCode': STATUS_CODE,
        'headers': {
            'Location': location
        }
    }

