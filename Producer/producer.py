import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue (if it doesn't already exist)
channel.queue_declare(queue='hello')

# Send a message
channel.basic_publish(exchange='', routing_key='hello', body='Komen de berichten aan?!')
print(" [x] Sent: Komen de berichten aan?!'")

# Close the connection
connection.close()
