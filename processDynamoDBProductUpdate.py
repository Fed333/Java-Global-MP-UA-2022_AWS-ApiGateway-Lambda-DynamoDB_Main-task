import json

def lambda_handler(event, context):
    # TODO implement
    print('DynamoDB product update!')
    print("Event:")
    print(event)
    print("-"*20)
    print("Context:")
    print(context)
    print("-"*20)
    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDBProductUpdate')
    }
