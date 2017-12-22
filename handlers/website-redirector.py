'''
Return a redirect location set in the environment.
'''
import os

REDIRECT_LOCATION = os.environ.get('REDIRECT_LOCATION')
STATUS_CODE = int(os.environ.get('STATUS_CODE'))

def handler(event, context):
    path = event.get('path')

    location = REDIRECT_LOCATION + event.get('path', '/')

    # Need to get URL from request so I can return full path
    return {
        'statusCode': STATUS_CODE,
        'headers': {
            'Location': location
        }
    }

