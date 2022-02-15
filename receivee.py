import pika, sys, os

# port=15672
def main():

    # username = os.environ['RabbitMq/Username']
    # password = os.environ['RabbitMq/Password']
    # host = os.environ['ElasticUrl']
    # print(host)
    # credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host='10.104.76.240', virtual_host='storage-collector-dev', heartbeat=5)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
