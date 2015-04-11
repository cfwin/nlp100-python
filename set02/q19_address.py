#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q19_address.py
"""

import re
import sys

def search_address():
	address = re.compile(
		ur'〒([0-9０-９]{3}[-ー][0-9０-９]{4})' +
		ur'[ 　]*' +
		ur'([一-龠^県]+県)' +
		ur'([^市^町^村]+[市町村])')
	for line in sys.stdin:
		line = line.strip('\n')
		for m in address.finditer(unicode(line)):
			print '\t'.join((m.group(1,2,3)))

if __name__ == '__main__':
	search_address()