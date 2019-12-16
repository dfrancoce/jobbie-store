from moto import mock_dynamodb2

import dynamodb
from models import JobOffer

test_payload_1 = {
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
}

test_payload_2 = {
    "hash": "a7ff38ad4d0546381be5e14704222eca692579a56c73cc26abab1ae101c1c42b",
    "url": "https://europeremotely.com/position/1111/senior-fullstack-go-rust-developer-remote-or-berlin",
    "position": "Senior Go / Rust developer (remote or Berlin)",
    "description": "",
    "company": "Cool company",
    "date": "about 1 month ago",
    "tags": [
        "Programming",
        "Go",
        "Rust"
    ]
}


@mock_dynamodb2
def test_save():
    payloads = [test_payload_1]
    dynamodb.save(payloads)

    assert JobOffer.count() == 1


@mock_dynamodb2
def test_save_no_duplicates():
    payloads = [test_payload_1, test_payload_2]
    dynamodb.save(payloads)

    assert JobOffer.count() == 1
