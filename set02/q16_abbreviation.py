#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q16_abbreviation.py
"""

import re
import sys

def search_abbr():
	abbr = re.compile(ur'([一-龠]+)(（|\()([A-ZＡ-Ｚ]+)(）|\))')
	for line in sys.stdin:
		line = line.strip('\n')
		for m in abbr.finditer(unicode(line)):
			print '\t'.join(m.group(1,3))

if __name__ == '__main__':
	search_abbr()