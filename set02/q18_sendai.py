#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q18_sendai.py
TODO:
番地の正規表現を拡張する
"""

import re
import sys

def search_sendai():
	sendai = re.compile(ur'仙台市[一-龠]+?区[一-龠]+')
	for line in sys.stdin:
		line = line.strip('\n')
		for m in sendai.finditer(unicode(line)):
			print m.group(0)

if __name__ == '__main__':
	search_sendai()