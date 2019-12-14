def lambda_handler(event, context):
    payloads = []

    for record in event['Records']:
        payload = record["body"]
        payloads.append(payload)

    return {
        "statusCode": 200,
        "body": payloads
    }
