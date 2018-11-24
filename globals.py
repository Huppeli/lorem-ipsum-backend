import os

import boto3

DYNAMODB = boto3.resource('dynamodb')
USER_TABLE = DYNAMODB.Table(os.environ['USER_TABLE'])
