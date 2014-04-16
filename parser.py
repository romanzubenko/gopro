import sys,re

def parser(filename,text):
	# step one
	printOutput(text,"all",filename)
	
	text = re.sub(r'(I|We|You|They|a|and|the|that|of|for|with|)',"",text)

	# step two
	printOutput(text,"proper","")
	

def printOutput(text,marker,name):
	newLines = len(text.split("\n")) - 1
	words = len([string for string in re.split(r"(\s|\%|\#|\$|\^|\*|\+|\=|\"|\t|\.|\!|\?|\(|\)|\,|\:|\;|\n|\_|\~|\@|\'|\<|\>|\`|\[|\]|\||\{|\})",text) if (re.match('^[\w-]+$', string) is not None)])
	bytes = len(text) 
	print(marker + ": " + str(newLines) + "    " + str(words) + "   " + str(bytes) + " " + name)




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
