event = {
    'Records':
        [{
            'eventID': '982c6b1caf9b6a4ebe7ecfdc6f770ebc',
            'eventName': 'REMOVE',
            'eventVersion': '1.1',
            'eventSource': 'aws:dynamodb',
            'awsRegion': 'eu-central-1',
            'dynamodb': {
                'ApproximateCreationDateTime': 1655663772.0,
                'Keys': {
                    'product_id': {'N': '4'},
                    'name': {'S': 'ruler'}
                },
                'OldImage': {
                    'picture_url': {'S': 'https://www.ldoceonline.com/media/english/illustration/ruler.jpg?version=1.2.50'},
                    'price': {'N': '14'},
                    'product_id': {'N': '4'},
                    'name': {'S': 'ruler'}
                },
                'SequenceNumber': '186600000000003977376045',
                'SizeBytes': 139,
                'StreamViewType': 'NEW_AND_OLD_IMAGES'
            },
            'eventSourceARN': 'arn:aws:dynamodb:eu-central-1:999565175928:table/Product/stream/2022-06-19T17:58:09.745'
        },
        {
            'eventID': '298d9b3f91000c906be6539456a8168d',
            'eventName': 'INSERT',
            'eventVersion': '1.1',
            'eventSource': 'aws:dynamodb',
            'awsRegion': 'eu-central-1',
            'dynamodb': {
                'ApproximateCreationDateTime': 1655663772.0,
                'Keys': {
                    'product_id': {'N': '4'},
                    'name': {'S': 'metal ruler'}
                },
                'NewImage': {
                    'picture_url': {'S': 'https://www.ldoceonline.com/media/english/illustration/ruler.jpg?version=1.2.50'},
                    'price': {'N': '24'},
                    'product_id': {'N': '4'},
                    'name': {'S': 'metal ruler'}
                },
                'SequenceNumber': '186700000000003977376177',
                'SizeBytes': 151,
                'StreamViewType': 'NEW_AND_OLD_IMAGES'
            },
            'eventSourceARN': 'arn:aws:dynamodb:eu-central-1:999565175928:table/Product/stream/2022-06-19T17:58:09.745'
        }]
}
