from app.repository import dynamodb


def lambda_handler(event, context):
    payloads = []

    for record in event['Records']:
        payload = record["body"]
        payloads.append(payload)

    dynamodb.save(payloads)

    return {
        "statusCode": 200,
        "body": payloads
    }
