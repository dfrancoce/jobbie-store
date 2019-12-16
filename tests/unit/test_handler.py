import pytest

import app


@pytest.fixture()
def sqs_event():

    return {
        "Records": [
            {
                "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
                "receiptHandle": "MessageReceiptHandle",
                "body": {
                    "hash": "a7ff38ad4d0546381be5e14704222eca692579a56c73cc26abab1ae101c1c42b",
                    "url": "https://europeremotely.com/position/4580/senior-fullstack-ruby-js-developer-remote-or-berlin",
                    "position": "Senior Fullstack Ruby / JS Developer (remote or Berlin)",
                    "description": "",
                    "company": "GOhiring - multiposting & analytics",
                    "date": "about 1 month ago",
                    "tags": [
                        "Programming",
                        "Full-stack",
                        "Ruby",
                        "JavaScript",
                        "Ruby on Rails"
                    ]
                },
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1523232000000",
                    "SenderId": "123456789012",
                    "ApproximateFirstReceiveTimestamp": "1523232000001"
                },
                "messageAttributes": {},
                "md5OfBody": "1a54030ee9d1b40058a97103a93f47f3",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:111111111111:job_offers",
                "awsRegion": "us-east-1"
            }
        ]
    }


def test_lambda_handler(sqs_event, mocker):
    mocker.patch('app.dynamodb.save')

    ret = app.lambda_handler(sqs_event, "")
    data = ret["body"]

    assert ret["statusCode"] == 200
    assert data[0]["hash"] == "a7ff38ad4d0546381be5e14704222eca692579a56c73cc26abab1ae101c1c42b"
    assert data[0]["url"] == "https://europeremotely.com/position/4580/senior-fullstack-ruby-js-developer-remote-or-berlin"
    assert data[0]["position"] == "Senior Fullstack Ruby / JS Developer (remote or Berlin)"
    assert data[0]["description"] == ""
    assert data[0]["company"] == "GOhiring - multiposting & analytics"
    assert data[0]["date"] == "about 1 month ago"
    assert data[0]["tags"] == [
        "Programming",
        "Full-stack",
        "Ruby",
        "JavaScript",
        "Ruby on Rails"
    ]
