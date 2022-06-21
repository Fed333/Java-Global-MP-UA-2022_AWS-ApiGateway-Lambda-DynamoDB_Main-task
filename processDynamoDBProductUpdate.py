import json
import boto3

client = boto3.client('dynamodb')


def get_handler(event, context):
    req_context = event["requestContext"]
    http = req_context["http"]
    print("get_handler invoked!")
    path = http["path"]
    protocol = http["protocol"]
    print(f"path: {path}")
    print(f"protocol: {protocol}")
    return {
        'statusCode': 200,
        'body': "method GET isn't properly implemented yet."
    }


def add_attribute(data_item, key, db_type, value):
    if value is not None:
        data_item[key] = {f'{db_type}': f'{value}'}


def is_item_present(key_item):
    response = client.get_item(
        TableName='Product',
        Key=key_item
    )
    print('response')
    print(response)
    item = response.get('Item', None)
    return True if item is not None else False


def post_handler(event, context):
    print("post_handler invoked")
    body = json.loads(event["body"])
    product_id = body['product_id']
    name = body.get('name', None)
    picture_id = body.get('picture_id', None)
    price = body.get('price', None)
    data_item = {
        'product_id': {
            'N': f'{product_id}'
        },
        'name': {
            'S': f'{name}'
        }
    }

    if is_item_present(data_item):
        return {
            'statusCode': 400,
            'body': f'Item with partition id \'{product_id}\' and sort id \'{name}\' already exists!'
        }

    add_attribute(data_item, 'picture_id', 'S', picture_id)
    add_attribute(data_item, 'price', 'N', price)

    data = client.put_item(
        TableName='Product',
        Item=data_item
    )
    print(f"product_id: {product_id}")
    print(f"name: {name}")

    print("data: ")
    print(data)
    response_body = 'Successfully added item to DynamoDB table Product!\n' + json.dumps(data_item)
    return {
        'statusCode': 200,
        'body': response_body
    }


dispatch = {
    "GET": get_handler,
    "POST": post_handler
}


def lambda_handler(event, context):
    method = event["requestContext"]["http"]["method"]
    response = dispatch[method](event, context)

    print(f"event: {event}")

    return response
