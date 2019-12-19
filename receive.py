#!/usr/bin/env python
import pika
import os
import sys
import logging
import logging.config
import yaml
import uuid
from environs import Env
import datetime

env = Env()
env.read_env()  # read .env file, if it exists

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

def testLogging():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    
url= env("CLOUDAMQP_URL", 'amqp://guest:guest@localhost/%2f') #os.environ['Mg__api_key'] #'key-0-rxwnpe9gllqe6odwxebn79vicgxf76'

params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)  
channel = connection.channel()

channel.queue_declare(queue='hello')

def makeDir(path):
    try:
        os.mkdir(path)
    except OSError as err:
        logging.error(err)
        logging.error("Creation of the directory %s failed" % path)
        print ("Creation of the directory %s failed" % path)
        return False
    else:
        logging.info("Successfully created the directory %s " % path)
        print ("Successfully created the directory %s " % path)
        return True

folder = './Messages'
if os.path.isdir(folder) == False:
    makeDir(folder)

def callback(ch, method, properties, body):
    try:
        id = str(uuid.uuid1())
        print (id)
        print(" [x] Received %r" % body)
        print(properties)
        print(body.decode())
        # printToFile(id, )
        saveAs= folder+"\\"+  id+".msg.txt"
        with open(saveAs, "w") as text_file:
                        text_file.writelines("ID= "+id)
                        text_file.writelines("Date received= "+str(datetime.datetime.now()))
                        text_file.write("\n___________________________\n")
                        text_file.writelines("properties= "+str(properties))
                        text_file.write("\n___________________________\n")
                        text_file.write(body.decode())
    except Exception as err:
        logging.error("@callback: "+ str(err))
        #print('err= '+ err)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

print("THE END")
