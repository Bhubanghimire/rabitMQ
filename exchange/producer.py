import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# channel.queue_declare(queue="hello")
channel.exchange_declare(exchange="logs", exchange_type="fanout")
data = {
    "name": "bhuban",
    "id": "2"
}

channel.basic_publish(
    exchange="logs",
    routing_key="",
    body=str(data)
)
print(f"producer sent {data}")
connection.close()
