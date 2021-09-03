from flaskr.app import app
import json


def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Hello World!"


def test_create_token():
    payload = {
        "carNum": "123884",
        "name": "test"
    }
    response = app.test_client().post('/create_token', data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 200
    assert json.loads(response.data.decode()) == {"success": True}


def test_create_token_without_body():
    payload = {}
    response = app.test_client().post('/create_token', data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 400
    assert json.loads(response.data.decode()) == {"error": "request body not found"}


def test_create_token_with_key_error():
    payload = {
        "carNum": "12345"
    }
    response = app.test_client().post('/create_token', data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 500
