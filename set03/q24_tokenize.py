#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
improved version of q23_tokenize.py
USAGE: cat medline.txt.sent | python q24_tokenize.py
"""

import re
import sys

def tokenize():
	stopwords = re.compile(r'[^a-z^A-Z^0-9]+$') #added
	for line in sys.stdin:
		line = line.strip('\n')
		for token in line.split(' '):
			print re.sub(stopwords, repl, token) #changed
		print

def repl(obj):
	return '\n' + obj.group(0)

if __name__ ==  "__main__":
	tokenize()
