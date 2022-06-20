import json


def lambda_handler(event, context):
    print('DynamoDB product update!')
    records = event['Records']
    print_sep("-", 20)
    print(f'Number of records:{len(records)}')
    print_sep("-", 20)

    for record in records:
        print_record(record)
        print_sep("-", 20)

    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDBProductUpdate')
    }


def print_sep(symb, repeat):
    print(symb * repeat)


def resolve_item_name(event_name):
    if event_name == "REMOVE":
        return "OldImage"
    elif event_name == "INSERT":
        return "NewImage"


def print_record(db_record):
    dynamo = db_record['dynamodb']
    print(f"{db_record['eventName']}")
    item_name = resolve_item_name(db_record['eventName'])
    item = {**dynamo['Keys'], **dynamo[item_name]}
    print(f'item: {item}')
