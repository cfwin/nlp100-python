#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt.sent.tok | python q36_bigram.py | python q37_freq.py
"""

import sys
from collections import defaultdict

def freq():
	D = defaultdict(int)
	for line in sys.stdin:
		line = line.strip('\n')
		if line:
			D[line] += 1
	for k, v in sorted(D.iteritems(), key=lambda x: x[1], reverse=True):
		print str(v) + '\t' + k

if __name__ == '__main__':
	freq()
