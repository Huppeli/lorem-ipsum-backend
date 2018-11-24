import boto3
import os
import json
from common import dynamodb, helpers

DYNAMODB = boto3.resource('dynamodb')


def get_user(table, uuid):
    user = dynamodb.query_with_limit_from(table, hash_key='uuid', key_value=uuid)
    return user


def handler(event, context):
    data = json.loads(event['body'])
    user_uuid = data['uuid']
    table = DYNAMODB.Table(os.environ['USER_TABLE'])
    user = get_user(table, user_uuid)
    return helpers.gen_response(dynamodb_results=user)
