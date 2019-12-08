#!/usr/bin/env python
import os
import sys
import requests

#print(os.environ['HOME'])
<<<<<<< HEAD

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
=======
#print(os.environ['CLOUDAMQP_URL'])
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')  #os.environ['CLOUDAMQP_URL'] || 
Mg__api_key='key-0-rxwnpe9gllqe6odwxebn79vicgxf76'
Mg__dontuse=1

def send_simple_message():
    return requests.post(
        " https://api.mailgun.net/v3/joeschedule.mailgun.org/messages",
        auth=("api", Mg__api_key),
        data={"from": "'Excited User <mastronardif@netcarrier.com>",
              "to": ["mastronardif@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


print(' [*] Waiting for send_simple_message. To exit press CTRL+C')
resp = send_simple_message()
print (resp)
>>>>>>> 53ab988e6ec1bdec1ab34995152ff5c9d194c0fe

print("THE END")
