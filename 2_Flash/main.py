import os
#*************** functions *******************

# Write file
def writeFile(value):
    f=open("myfile.txt","w")
    f.write(str(value))
    f.close()
    print("done")

# Read File
def readFile():
    f=open("myfile.txt","r")
    myfile = f.read()
    f.close()
    return myfile

i = 0
print("go")

