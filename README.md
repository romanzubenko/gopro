GoPro challenge
=====

Code is both compatible with python 2.7 and python 3.3

Non-significant word overcounting occurs due to the fact that wc doesn't break down url into multiple words, disregarding url altogether.

To run tests:
```sh
python parser.py constitution.txt 
python3.3 parser.py constitution.txt
```


Output:
======
```sh
all: 871    7654   45118 constitution.txt
proper: 871    6273   38267 
Articles: 7
Sections: 21
Total Sections per Article: 
     Article1: 10
	 Article2: 4
	 Article3: 3
	 Article4: 4
	 Article5: 0
	 Article6: 0
	 Article7: 0
```

