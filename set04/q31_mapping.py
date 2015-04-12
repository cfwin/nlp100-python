#! /usr/bin/python
# -*- coding: utf-8 -*-

 """
 USAGE: cat inflection.table.txt | python q31_mapping.py
 """

import sys
from collections import defaultdict

def dictionarize():
	D = defaultdict(list)
	for line in sys.stdin:
		line = line.strip('\n').split('|')
		token, pos, cf, base = line[0], line[1], line[3], line[6]
		D[token].append((token, pos, cf, base))
	return D

def search(string):
	D = dictionarize()
	print string
	for values in D[string]:
		print '(%s)' % ','.join(values)

if __name__ == '__main__':
	search('news')