# Code iplemented by Roman Zubenko
import sys,re

def parser(filename,text):
	# step one
	printOutput(text,"all",filename)
	
	properText = re.sub(r'(I|We|You|They|a|and|the|that|of|for|with|)',"",text)

	# step two
	printOutput(properText,"proper","")

	'''
		For step three I need to made some assumptions:
			1. Articles are separated with "\nArticle [0-9]*\."
			2. Sections are nested withing article and delimited with: "\nSection [0-9]*"
	'''

	# Count variables for sections, articles
	articleCount = 0
	totalSectionCount = 0

	# dictionary for section counts in every article
	sectionCounts = {}


	articles = re.split(r"(\nArticle [0-9]*\.)",text)
	
	# disregard first portion of the text before first article
	articles = articles[1:]

	for e in articles:
		# count for every article
		sectionCount = 0
		
		if len(re.findall(r"Article [0-9]*\.",e)) == 0:
			articleCount += 1
			sections = re.split(r"(\nSection [0-9]*)",e)
			
			# Count the section numbers in current article
			for s in sections:
				if len(re.findall(r"Section [0-9]*",s)) == 0:
					if articleCount in sectionCounts:
						sectionCounts[articleCount] += 1
					else: # if count for this article hasn't been initialized 
						sectionCounts[articleCount] = 1
			
			# Eliminate overcounting by one
			if articleCount not in sectionCounts:
				sectionCounts[articleCount] = 0
				
			
			# If there are no sections in the article, initialize count to 0
			if sectionCounts[articleCount] != 0:
				sectionCounts[articleCount] -= 1
			
			totalSectionCount += sectionCounts[articleCount]



	print("Articles: " + str(articleCount))
	print("Sections: " + str(totalSectionCount))
	print("Total Sections per Article: ")

	for i in range(1, articleCount + 1):
		print("\t Article " + str(i) + ": "+ str(sectionCounts[i]))

	
# Code to output first two steps
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
