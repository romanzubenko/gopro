import sys


# if filename is not passed
if len(sys.argv) < 2:
	exit 

# get the first command line argument
filename = sys.argv[1]
# open file
try:
	fObject = open(filename, "r")
	fileData = fObject.read()
except:
	print "wc: " + filename + ": open: No such file or directory"
	exit 
# 


def parser(text):
	return text