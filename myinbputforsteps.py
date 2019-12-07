#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getopt, sys

def hello():
    print("Hello World") 
    return 

def goodby():
    print("Goodb by World") 
    return 

def getArgs(argumentList):
    unixOptions = "hoxs:v"
    gnuOptions = ["help", "output=", "xml=", "slt=", "verbose"]
    #python arguments-getopt.py --output=green --help -v

    d = dict(); 
    try:
        print('0 argumentList=', argumentList)
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
        print('0 arguments=', arguments)
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
            print ("displaying help")
        elif currentArgument in ("-o", "--output"):
            d['out']   = currentValue
            print (("enabling special output mode (%s)") % (currentValue))
        elif currentArgument in ("-x", "--xml"):
            d['xml']   = currentValue
            print (("Xml input (%s)") % (currentValue))
        elif currentArgument in ("-s", "--slt"):
            print (("Xslt input (%s)") % (currentValue))
            d['xslt'] = currentValue
    
    #d['xslt'] = "sssxxxllltttxxx"
    #d['xml']   = 'xxxxxxxxxxmmmmmmmmmmmmmmmmmlllllllll'
    #d['out']   = '000000000000'
    return d 

    #Sreturn argumentList

