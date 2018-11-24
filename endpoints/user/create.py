import boto3
import os
import uuid
import json
import decimal
from common import helpers

DYNAMODB = boto3.resource('dynamodb')

PROFILE_DIMENSIONS = ['meat', 'veggies', 'fruits', 'dairy', 'fish']


def create_user(table: DYNAMODB.Table, custom_id=None):
    # meat veggies fruits dairy, fish kg euros
    unique_id = None
    if custom_id:
        unique_id = custom_id
    else:
        unique_id = str(uuid.uuid4())
    item_content = {'uuid': unique_id}
    for dimension in PROFILE_DIMENSIONS:
        item_content[dimension] = {'kg': decimal.Decimal(0.0), 'euros': decimal.Decimal(0.0)}
    response = table.put_item(
        Item=item_content
    )
    return {'response': response,
            'uuid': unique_id}


def handler(event, context):
    data = None
    unique_id = None
    try:
        data = json.loads(event.get('body'))
    except TypeError:
        pass
    if data:
        unique_id = data.get('uuid')

    table = DYNAMODB.Table(os.environ['USER_TABLE'])
    response = create_user(table, unique_id)
    return helpers.gen_response(response, statuscode=201)
