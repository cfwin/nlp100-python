#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
derived from q66_vector.py
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

def cosine_similarity(v1, v2):
	cos = 0.0
	for k in v1.keys():
		cos += v1[k] * v2[k]
	return cos

def main():
	V = normalize(vector())

	#cosine similarity
	print cosine_similarity(V['日本'], V['我が国'])

if __name__ == '__main__':
	main()
