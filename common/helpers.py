import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def gen_response(body, statuscode=200, dynamodb_results=None):
    if dynamodb_results:
        body = json.dumps(dynamodb_results['Items'], cls=DecimalEncoder)
    else:
        body = json.dumps(body, cls=DecimalEncoder)
    response = {
        "statusCode": statuscode,
        "body": body,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true"
        }
    }
    return response
