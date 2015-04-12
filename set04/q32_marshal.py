#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
improved version of q31_mapping.py, function dump() added.
USAGE: cat inflection.table.txt | python q32_marshal.py
"""

import marshal
import sys

def dictionarize():
	D = {}
	for line in sys.stdin:
		line = line.strip('\n').split('|')
		token, pos, cf, base = line[0], line[1], line[3], line[6]

		#Do not use defaultdict because it is unmarshallable
		if token not in D:
			D[token] = [(pos, cf, base)]
		else:
			D[token].append((pos, cf, base))

	return D

def search(string):
	D = dictionarize()
	print string
	for values in D[string]:
		print '(%s)' % ','.join(values)

#added. dump() just dump dictinary D as binary file.
def dump():
	D = dictionarize()
	marshal.dump(D, open('inflection.table.txt.msl', 'wb'))

if __name__ == '__main__':
	#search('news')
	dump()