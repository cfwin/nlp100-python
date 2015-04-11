#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q20_emotions.py
"""

import re
import sys

def search_emotions():
	emotion = re.compile(ur'\([^a-zA-Z0-9aぁ-んァ-ヴ]{2,5}\)')
	for line in sys.stdin:
		line = line.strip('\n')
		for m in emotion.finditer(unicode(line)):
			print m.group(0)

if __name__ == '__main__':
	search_emotions()