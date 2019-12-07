
import requests
import getopt, sys
import re
from myinputforgeturl import getArgs22

# read commandline arguments, first
fullCmdArguments = sys.argv

# - further arguments
argumentList = fullCmdArguments[1:]
unixOptions = "houy:v"
gnuOptions = ["help", "output=", "u=", "yml=", "verbose"]
retval22 = getArgs22(argumentList, unixOptions, gnuOptions)
uuu =  retval22['u'] if "u" in retval22 else None
yyy =  retval22['y'] if "y" in retval22 else None
ooo =  retval22['o'] if "o" in retval22 else None

print (retval22)
#sys.exit(123)

response = requests.get(uuu)
if response.history:
    print ("Request was redirected")
    for resp in response.history:
        print (resp.status_code, resp.url)

    print ("Final destination:")
    print (resp.status_code, resp.url)
    #print (response.content)
else:
    print ("Request was not redirected")
    print (uuu, "\n")
    #print (response.content)

print (response.content)
with open(ooo, 'wb') as fout:
    fout.write(response.content) 
sys.exit(9)

r = requests.get(uuu)
r = requests.head(uuu, allow_redirects=True)

print ("r.status_code= \n", r.status_code, "\n\n")
print (r)
if (r.url != uuu):
    r = requests.get(r.url)
print("\nfinalurl= \n",r.url, "\n\n")
with open(ooo, 'wb') as fout:
    fout.write(r.content) 

#print (r.content).decode()
