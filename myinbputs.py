#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getopt, sys
import re

def hello():
    print("Hello World") 
    return 

def help():
    print("""
    -h display help.
    -o output file
    -y yanl file what to search replace
    -t template file what to change
    """)
    return 

def getArgs22(argumentList, unixOptions, gnuOptions):
    #unixOptions = "hoxs:v"
    #gnuOptions = ["help", "output=", "xml=", "slt=", "verbose"]
    #python arguments-getopt.py --output=green --help -v

    d = dict(); 
    try:
        #print('0 argumentList=', argumentList)
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
        #print('0 arguments=', arguments)
    except getopt.error as err:
        # output error, and return with an error code
        print ('ZZZZZZZZZZZZZZZZZZZZZZ', str(err))
        return d

 
    #print('arguments=', arguments)
    for currentArgument, currentValue in arguments:
        print(currentArgument)
        if currentArgument in ("-v", "--verbose"):
            print ("enabling verbose mode")
        elif currentArgument in ("-h", "--help"):
            help ()
        elif currentArgument in ("-o", "--output"):
            d['o']   = currentValue
            print (("enabling special output mode (%s)") % (currentValue))
        elif currentArgument in ("-t", "--t"):
            d['t']   = currentValue
            print (("t input (%s)") % (currentValue))
        elif currentArgument in ("-y", "--yml"):
            print (("y input (%s)") % (currentValue))
            d['y'] = currentValue
    
    return d 

def makeDBList(list):
    print ('\t***** makeDBList')
    #normalize
    print (list)
    list = re.sub('[,\'"]', ' ', list)
    print (list)
    list = list.strip()
    list = re.split('\s+', list)
    list = ','.join("'{0}'".format(w) for w in list)
    print (list)
    return list


def applyRule(right, rule): 
    if re.match(rule, 'DATA_OBJ_ID make a list for db.', re.IGNORECASE):
        right = makeDBList(right)

    return right

def getRule(rules, key):
    for i, rule in enumerate(rules):
        #print(i, 'FIND ', key, 'in ', val)
        if re.search(key, rule, re.IGNORECASE):
            return rule

    return None
