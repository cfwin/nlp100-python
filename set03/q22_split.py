#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt | python q22_split.py
"""

import re
import sys

def split():
	pattern = re.compile(r'\. ([A-Z])')
	for line in sys.stdin:
		print re.sub(pattern, repl, line)

def repl(obj):
	return  '.\n' + obj.group(1)

if __name__ ==  "__main__":
	split()
