import json
import os
import sys

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        try:
            regular_string = body.decode('utf-8')

            # Replace single quotes with double quotes to make it valid JSON
            json_string = regular_string.replace("'", '"')

            # Parse the JSON string into a Python dictionary
            body = json.loads(json_string)

        except Exception as e:
            print("errpr", e)
        print(f"receiver got id: {body['id']} and name: {body['name']}")

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback
                          )
    print("receiver waiting for message")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
