#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat contexts.lst | python q66_vector.py
"""

import math
import sys
from collections import defaultdict

def normalize(V):
	for np, contexts in V.iteritems():
		#get size of vector
		sums = 0
		for v in contexts.values():
			sums += v ** 2
		Z = math.sqrt(sums)
		
		#divide by size
		for k, v in contexts.iteritems():
			V[np][k] = v / Z

	return V

def vector():
	V = defaultdict(lambda : defaultdict(float))
	for line in sys.stdin:
		np, context = line.strip('\n').split('\t')
		V[np][context] += 1.0
	return V

def main():
	V = []
	for np, contexts in normalize(vector()).iteritems():
		V.append(np)
		for k, v in contexts.iteritems():
			V.append('%s:%f' % (k, v))
		print '\t'.join(V)

if __name__ == '__main__':
	main()
