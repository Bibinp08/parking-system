import json
from unittest import mock
from flaskr.send import send_message
from pika.exceptions import AMQPChannelError, AMQPConnectionError

DATA = {"carNum": "9876", "name": "abcd"}


@mock.patch("flaskr.send.pika.BlockingConnection")
def test_send_with_AMQPConnectionError(mock_error):
    # given
    data = json.dumps(DATA)
    mock_error.side_effect = [AMQPConnectionError()]
    try:
        send_message(data)

        assert False
    except AMQPConnectionError:
        assert True


@mock.patch("flaskr.send.pika.BlockingConnection")
def test_send_with_AMQPChannelError(mock_error):
    # given
    data = json.dumps(DATA)
    mock_error.side_effect = [AMQPChannelError()]
    try:
        send_message(data)

        assert False
    except AMQPChannelError:
        assert True
