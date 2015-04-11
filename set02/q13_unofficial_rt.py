#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q13_unofficial_rt.py
"""

import sys

def search_string(string):
	for line in sys.stdin:
		line = line.strip('\n')
		if string in line:
			print line.split(string)[0]

if __name__ == '__main__':
	search_string(' RT ')