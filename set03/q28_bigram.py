#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE:
cat medline.txt.sent.tok | python q28_bigram.py > bigram.lst
python set01/set01.py --src bigram.lst q10 -c1 | head -100

RESULT:
in	404878
th	391687
re	313451
ti	310837
on	295740
he	288366
at	284333
an	279983
er	265087
en	243370
"""

import sys

def bigram():
	for line in sys.stdin:
		token = line.strip('\n').split('\t')[1]
		if token:
			for i in xrange(len(token) - 1):
				print token[i:i+2]

if __name__ == '__main__':
	bigram()

