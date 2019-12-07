#!/usr/bin/env python
import pika
import os
import sys

#print(os.environ['HOME'])
#print(os.environ['CLOUDAMQP_URL'])
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')  #os.environ['CLOUDAMQP_URL'] || 

params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) #   
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(properties)
    print(body.decode())




channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

print("THE END")
