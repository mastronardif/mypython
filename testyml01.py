#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getopt, sys
import yaml
import re

#from lxml import etree
from myinbputforsteps import hello
from myinbputforsteps import goodby
from myinbputs import getArgs22
from myinbputs import getRule
from myinbputs import applyRule

#> py testyml01.py --out=myout.txt  --t=templatePLTAP141_DATA_OBJ_ID.txt --yml=fruits.yaml 

# read commandline arguments, first
fullCmdArguments = sys.argv

# - further arguments
argumentList = fullCmdArguments[1:]
unixOptions = "hoty:v"
gnuOptions = ["help", "output=", "t=", "yml=", "verbose"]
retval22 = getArgs22(argumentList, unixOptions, gnuOptions)

ttt =  retval22['t'] if "t" in retval22 else None
yyy =  retval22['y']  if "y" in retval22 else None
ooo =  retval22['o'] if "o" in retval22 else None

if ttt is None:
  sys.exit(0)

with open(yyy, 'r') as file:
  doc = yaml.load(file, Loader=yaml.FullLoader)       
  rules =  doc['rules']
  #print (rules)
  
  thingsToReplace = [x.strip() for x in doc['thingsToReplace'].split(',')]
  #print('thingsToReplace', thingsToReplace)

  with open(ttt, 'r') as file:
    data = file.read()

    for ii in thingsToReplace: 
      left = ii
      left = "{0}{1}{2}".format('<', left, '/>')
      right = doc[ii]  

      # if DATA_OBJ_ID, make list for db
      #if needsFormat(rules, ii) = 
      # 
      rule = getRule(rules, ii)
      if (rule):
        print('right= applyRule(RULE ** ', rule, '\n to ', ii, right, ')\n\n')
        right = applyRule(right, rule)
        

      data = data.replace(left, right)
  
  print ('data=\n---------\n', data)

  if ooo is not None:
    with open(ooo, 'w') as file:
      file.write(data)

sys.exit(0)



def transform(xmlPath, xslPath, fout):
  # read xsl file
  #xslRoot = etree.fromstring(open(xslPath).read())
  #transform = etree.XSLT(xslRoot)

  xslt_tree = etree.parse(xslPath)
  transform = etree.XSLT(xslt_tree)


  # read xml
  xmlRoot = etree.fromstring(open(xmlPath).read())

  # transform xml with xslt
  transRoot = transform(xmlRoot)

  #etree.write('000output.xml')
  if fout:
    transRoot.write(fout, pretty_print=True, xml_declaration=True,   encoding="utf-8")
  # return transformation result
  return etree.tostring(transRoot)

if __name__ == '__main__':
  #print(transform('GL562Q2019.xml', 'geniusXml.xsl', fout).decode()) 
  print('fffff') 
  ##print(transform(fxml, fxslt, fout).decode())