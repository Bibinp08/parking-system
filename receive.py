import os
import pika
import sys
import json
import logging

from token_generator import generate_token


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="my_rabbitmq")
    )
    channel = connection.channel()
    channel.queue_declare(queue="generate token")
    def callback(ch, method, properties, body):
        queue_message = json.loads(body.decode("UTF-8"))
        generate_token(queue_message)
    channel.basic_consume(
        queue="generate token",
        on_message_callback=callback,
        auto_ack=True,
    )
    logging.info(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)