#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q12_nau.py
"""

import sys

def search_string(string):
	for line in sys.stdin:
		line = line.strip('\n')
		if line.endswith(string):
			print line

if __name__ == '__main__':
	search_string('なう') 