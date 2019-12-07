#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getopt, sys

from lxml import etree
from myinbputforsteps import hello
from myinbputforsteps import goodby
from myinbputforsteps import getArgs
# def hello():
#     print("Hello World") 
#     return 

# read commandline arguments, first
fullCmdArguments = sys.argv

# unixOptions = "ho:v"
# gnuOptions = ["help", "output=", "verbose"]

# - further arguments
argumentList = fullCmdArguments[1:]

# try:
#     arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
# except getopt.error as err:
#     # output error, and return with an error code
#     print (str(err))
#     sys.exit(2)
# print (argumentList)

# for currentArgument, currentValue in arguments:
#     if currentArgument in ("-v", "--verbose"):
#         print ("enabling verbose mode")
#     elif currentArgument in ("-h", "--help"):
#         print ("displaying help")
#     elif currentArgument in ("-o", "--output"):
#         print (("enabling special output mode (%s)") % (currentValue))

hello()
goodby()
retval = getArgs(argumentList)
print(retval)
 
fxml  =  retval['xml']  if "xml"  in retval else 'GL562Q2019.xml'
fxslt =  retval['xslt'] if "xslt" in retval else 'geniusXml.xslt'
fout  =  retval['out']  if "out"  in retval else ''
print ('\t\t\t*** fxml= ', fxml)
print ('\t\t\t*** fxslt= ', fxslt)
print ('\t\t\t*** fout= ', fout)

#print(retval['xml'])
#print(retval['xslt'])
#print(retval['out'])
 
##sys.exit(0)

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
  # print(transform('./s0101m.mul0.xml', './tipitaka-latn.xsl'))
  #C:\FxM\Downloads\Dev\MyXml\MyXml\Data
  #print(transform('GL562Q2019.xml', 'geniusXml.xsl'))
  #print(transform('GL562Q2019.xml', 'geniusXml.xsl', fout).decode())  
  print(transform(fxml, fxslt, fout).decode())
  #transRoot.write('000output.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")

  #print('Trying works() ...')
  #print works(myXML)
  #print(works('GL562Q2019.xml', 'geniusXml.xsl'))

