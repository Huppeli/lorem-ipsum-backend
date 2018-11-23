from boto3.dynamodb.conditions import Key, Attr


def query_with_limit_from(table, hash_key, key_value, limit=1):
    response = table.query(
        KeyConditionExpression=Key(hash_key).eq(key_value),
        Limit=limit
    )
    return response


def delete_from(table, hash_key, range_key, hash_value, range_value):
    response = table.delete_item(
        Key={
            hash_key: hash_value,
            range_key: range_value
        }
    )
    return response


def pop_row_from(table, hash_key, hash_key_value, range_key):
    q_response = query_with_limit_from(table, hash_key=hash_key, key_value=hash_key_value)

    try:
        row = q_response['Items'].pop()
        d_response = delete_from(
            table=table,
            hash_key=hash_key,
            range_key=range_key,
            hash_value=row[hash_key],
            range_value=row[range_key]
        )

        return row
    except IndexError:
        raise IndexError
