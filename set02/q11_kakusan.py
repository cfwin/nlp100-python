#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q11_kakusan.py
"""

import sys

def search_string(string):
	for line in sys.stdin:
		line = line.strip('\n')
		if string in line:
			print line

if __name__ == '__main__':
	search_string('拡散希望')