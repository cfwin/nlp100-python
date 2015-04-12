#! /usr/bin/python
# -*- codin: utf-8 -*-

import sys
from porter_stemmer import PorterStemmer

def stem():
	for line in sys.stdin:
		line = line.strip('\n')
		if line:
			token = line.split('\t')[1]
			ps = PorterStemmer().stem(token, 0, len(token)-1)
			print line + '\t' + ps

if __name__ == '__main__':
	stem()