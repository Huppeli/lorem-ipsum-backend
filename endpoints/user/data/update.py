import decimal
import json
import os

import boto3

from common import helpers

DYNAMODB = boto3.resource('dynamodb')


def update_user_data(table, uuid, dimension, metric, new_value):
    expression = "set {}.{} = :r".format(dimension, metric)
    print(expression)
    response = table.update_item(
        Key={
            'uuid': uuid
        },
        UpdateExpression=expression,
        ExpressionAttributeValues={
            ':r': decimal.Decimal(new_value),
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def handler(event, context):
    data = json.loads(event['body'])

    uuid = data['uuid']
    dimension = data['dimension']
    metric = data['metric']
    new_value = data['value']

    table = DYNAMODB.Table(os.environ['USER_TABLE'])
    updated_new = update_user_data(table, uuid, dimension, metric, new_value)
    return helpers.gen_response(body=updated_new)
