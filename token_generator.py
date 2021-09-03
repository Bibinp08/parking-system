import json
import logging


def generate_token(payload):
    with open('data.json', 'w') as fp:
        json.dump(payload, fp)

    logging.info("Token generated successfully")
