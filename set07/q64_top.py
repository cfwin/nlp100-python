#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat tfidf.lst | python q64_top.py
"""

import re
import sys

def top_100():
	D = []
	numbers = re.compile(ur'[0-9０-９ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ]')
	for line in sys.stdin:
		np, tfidf, tf, df = line.strip('\n').split('\t')
		if not numbers.search(unicode(np)):
			D.append((np, float(tfidf)))

	for k, v in sorted(D, key=lambda x:x[1], reverse=True)[:100]:
		print str(v) + '\t' + k

if __name__ == '__main__':
	top_100()
