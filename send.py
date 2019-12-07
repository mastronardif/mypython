#!/usr/bin/env python
import pika
import os
import sys
import time
import datetime

def msg001():
    msg = """
    async def asdf
    asdf
    as
    fas
    fas
    f(parameter_list):
        pass
    """
    return msg
#print(os.environ['HOME'])
#print(os.environ['CLOUDAMQP_URL'])
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')  #os.environ['CLOUDAMQP_URL'] || 

params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) #   
channel = connection.channel()

channel.queue_declare(queue='hello')

msg = " [x] Sent 'Hello World! '" + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+msg001()
channel.basic_publish(exchange='', routing_key='hello', body=msg)
print(" [x] Sent 'Hello World! '",datetime.datetime.now())
connection.close()

print("THE END")

