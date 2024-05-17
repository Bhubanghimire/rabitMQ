import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="", exclusive=True)
data = {
    "name":"bhuban",
    "id":"2"
}

channel.basic_publish(
    exchange="",
    routing_key="hello",
    body=str(data)
)

print("A sent 'hello world'")
connection.close()

