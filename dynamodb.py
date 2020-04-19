import os

import boto3
from boto.awslambda.exceptions import ResourceNotFoundException

table_name = os.environ['TABLE_NAME']


def save(payloads):
    table = boto3.resource('dynamodb', region_name="us-east-1").Table(table_name)

    for payload in payloads:
        try:
            table.get_item(Key={'hash': payload['hash']})
        except ResourceNotFoundException:
            table.put_item(
                Item={
                    'hash': payload['hash'],
                    'url': payload['url'],
                    'position': payload['position'],
                    'description': payload['description'],
                    'company': payload['company'],
                    'date': payload['date'],
                    'tags': payload['tags']
                }
            )
