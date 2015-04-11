#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt.sent | python q23_tokenize.py
"""

import sys

def tokenize():
	for line in sys.stdin:
		line = line.strip('\n')
		for token in line.split(' '):
			print token
		print

if __name__ ==  "__main__":
	tokenize()
