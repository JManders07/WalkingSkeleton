import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue='hello')

# Callback function to process the message
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Subscribe to the queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()