from token_generator import generate_token


BODY = {"carNum": "1234", "name": "test"}


def test_token_generator():
    # given
    body = BODY
    try:
        # when
        generate_token(body)
        # then
        assert True
    except TypeError:
        assert False
