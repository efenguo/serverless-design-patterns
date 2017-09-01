import json
import sys

from pathlib import Path

# Munge our sys path so libs can be found
CWD = Path(__file__).resolve().cwd() / 'lib'
sys.path.insert(0, str(CWD))

from cupping.handlers.session import handle_session



def session(event, context):
    http_method = event['httpMethod']
    response = handle_session(http_method, event)

    response = {
        "statusCode": 200,
        "body": json.dumps(response)
    }

    return response


# if __name__ == '__main__':
#     from cupping.models import *
#     from cupping.db import (
#             _drop_tables,
#             create_tables,
#             setup_db,
#     )
#     setup_db()
#     _drop_tables(force=True)
#     create_tables()
