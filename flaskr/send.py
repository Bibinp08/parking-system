import pika
import logging
from pika.exceptions import AMQPChannelError, AMQPConnectionError


def send_message(message: str):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="my_rabbitmq")
        )
        channel = connection.channel()
        channel.queue_declare(queue="generate token")
        channel.basic_publish(
            exchange="", routing_key="generate token", body=message
        )
        connection.close()
        return True
    except AMQPConnectionError as ex:
        logging.exception(f"caught exception, error={ex}")
        raise ex

    except AMQPChannelError as ex:
        logging.exception(f"caught exception, error={ex}")
        raise ex

