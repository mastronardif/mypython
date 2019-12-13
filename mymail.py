#!/usr/bin/env python
import os
import sys
import requests

#print(os.environ['HOME'])
#print(os.environ['Mg__api_key'])
#url = os.environ.get('Mg__api_key', 'amqp://guest:guest@localhost/%2f')  #os.environ['CLOUDAMQP_URL'] || 
Mg__api_key= os.environ['Mg__api_key'] #'key-0-rxwnpe9gllqe6odwxebn79vicgxf76'
Mg__dontuse=1

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/joeschedule.mailgun.org/messages",
        auth=("api", Mg__api_key),
        data={"from": "mastronardif@netcarrier.com",
              "to": ["mastronardif@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


print(' [*]  for send_simple_message.')
resp = send_simple_message()
print (resp)

print("THE END")
