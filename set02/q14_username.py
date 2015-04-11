#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q14_username.py
"""

import re
import sys

def search_user():
	username = re.compile('@\w+')
	for line in sys.stdin:
		line = line.strip('\n')
		for usr in username.findall(line):
			print usr

if __name__ == '__main__':
	search_user()