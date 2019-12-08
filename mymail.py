#!/usr/bin/env python
import pika
import os
import sys

#print(os.environ['HOME'])

print(os.environ['MG_DOMAIN'])
print(os.environ['MG_API_KEY'])
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')  #os.environ['CLOUDAMQP_URL'] || print(url())


sys.exit(23)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(properties)
    print(body.decode())




channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

print("THE END")
