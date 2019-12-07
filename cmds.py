#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getopt, sys
import yaml
import re
import os
import time
import datetime

yyy = 'cmds.yaml'

def sTest():
    msg = """
commands:
  - ZgetUrl
  - Ztest
  - ZExit 
  - ping
  - Zmail
"""
    return msg

with open(yyy, 'r') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)  
    cmds =  doc['commands']
    print (cmds)

def runCmd(cmd):
    print ('\t run Cmd:  ', cmd)
    os.system('py '+cmd) #("py ping.py aaaa BBB ccc")


def getCmd(cmds, key):
    # find ii in rules
    #print ("\n\t{0}\n{1}\n{2}\n".format('isRule', rules, key))
    for i, cmd in enumerate(cmds):
        key = key.split(' ', 1)[0]
        #print(i, 'FIND ', key, 'in ', cmd)
        if re.match(key.strip(), cmd, re.IGNORECASE):
            #print('kkkkkkkkkkkkkkk(' +key + ') ttttttt True')
            #print('ccccccccccccccc(' +cmd + ') ddddddddd True')
            # chomp first word
            cmd = cmd.split(' ', 1)[1]
            #print('ddddddd(' +cmd + ') eeeeee ')
            return cmd

    return None
bob = yaml.load(sTest(), Loader=yaml.FullLoader)
print (bob['commands'])
#print (sTest().split('\n'))
#sys.exit(22)

for key in bob['commands']:
    key = key.strip()
    #print (getCmd(cmds, key))
    cmd = getCmd(cmds, key)
    if (cmd):
        runCmd(cmd)
        #runCmd(cmd, 'args whatever they may be!')
        print ("run: "+ key)

#sys.exit(9)


print("cmds.py THE END")

