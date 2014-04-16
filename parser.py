import sys,re

def parser(filename,text):
	newLines = len(text.split("\n"))
	words = len([string for string in re.split(r"(\s|\%|\#|\$|\^|\*|\+|\=|\"|\t|\.|\!|\?|\(|\)|\,|\:|\;|\n|\_|\~|\@|\'|\<|\>|\`|\[|\]|\||\{|\})",text) if (re.match('^[\w-]+$', string) is not None)])
	bytes = len(text) 
	print("     " +str(newLines) + "    " + str(words) + "   " + str(bytes) + " " + filename)


# if filename is not passed
if len(sys.argv) < 2:
	exit 

# get the first command line argument
filename = sys.argv[1]

# open file
try:
	fObject = open(filename, "r")
	fileData = fObject.read()
	
except :
	print("parser: " + filename + ": open: No such file or directory")
	exit 


parser(filename,fileData)
