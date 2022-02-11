import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    'localhost', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()