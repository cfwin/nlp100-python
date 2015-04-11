#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
improved version of q21_split.py
USAGE: cat medline.txt | python q22_split.py
"""

import re
import sys

def split():
	pattern = re.compile(r'\. ([A-Z])') #added
	for line in sys.stdin:
		#replaced
		#for sentence in line.strip('\n').split('. '):
		#	print sentence
		print re.sub(pattern, repl, line)

def repl(obj):
	return  '.\n' + obj.group(1)

if __name__ ==  "__main__":
	split()
