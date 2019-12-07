import os

# define the name of the directory to be created
path = "/tmp/year"




def makeDirs(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def makeDir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

path = "GWY_"
for x in "1234":
  print(path+x)
  #makeDir(path+x)

#makeDir(path)