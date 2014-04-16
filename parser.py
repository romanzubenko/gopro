import sys,re

def parser(filename,text):
	# step one
	printOutput(text,"all",filename)
	
	properText = re.sub(r'(I|We|You|They|a|and|the|that|of|for|with|)',"",text)

	# step two
	printOutput(properText,"proper","")

	'''
		For step three I need to made some assumptions:
			1. Articles are separated with "Article [0-9]*"
			2. Sections are nested withing article and delimited with: "Section [0-9]*"
	'''

	articleCount = 0
	sectionCounts = {}

	articles = re.split(r"(\nArticle [0-9]*\.)",text)
	articles = articles[1:]
	for e in articles:
		sectionCount = 0
		if len(re.findall(r"Article [0-9]*\.",e)) == 0:
			articleCount += 1
			sections = re.split(r"(\nSection [0-9]*)",e)
			for s in sections:
				if len(re.findall(r"\nSection [0-9]*",s)) == 0:
					if articleCount in sectionCounts:
						sectionCounts[articleCount] += 1
					else:
						sectionCounts[articleCount] = 1
		else:
			pass

	print("Articles: " + str(articleCount))
	print("Total Sections per Article: ")
	for i in range(1,8):
		print("\t Article " + str(i) + ": "+ str(sectionCounts[i]))
			

	

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
