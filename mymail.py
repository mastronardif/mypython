#!/usr/bin/env python
import os
import sys
import requests

#print(os.environ['HOME'])
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

print("THE END")
