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
	parser(fileData)
except:
	print "parser: " + filename + ": open: No such file or directory"
	exit 
# 


def parser(text):
	newLines = len(text.split("\n"))
	words = len(text.split(" |\n"))
	bytes = len(text.split("")) * 8
	print newLines + " " + words + " " + bytes