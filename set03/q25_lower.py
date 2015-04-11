#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt.sent | python q24_tokenize.py | python q25_lower.py
"""

import sys

for line in sys.stdin:
	token = line.strip('\n')
	print token + '\t' + token.lower()