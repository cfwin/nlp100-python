#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
derived from q67_cossim.py
USAGE: cat contexts.lst | python q68_threshold.py
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

def similar():
	TH = 0.6
	V = normalize(vector())
	np = V.keys()

	similars = []
	for i in xrange(len(np)):
		for j in xrange(i+1, len(np)):
			cos = cosine_similarity(V[np[i]], V[np[j]])
			if cos > TH:
				similars.append((cos, np[i], np[j]))

	return similars

if __name__ == '__main__':
	similars = similar()
	for cs, v1, v2 in sorted(similars, key=lambda x:x[0], reverse=True):
		print '%.6f\t%s\t%s' % (cs, v1, v2)
