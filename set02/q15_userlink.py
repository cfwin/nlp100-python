#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q15_userlink.py
"""

import re
import sys

def user_link():
	username = re.compile('@\w+')
	link =  '<a href="https://twitter.com/#!/%s">@%s</a>'
	for line in sys.stdin:
		line = line.strip('\n')
		for usr in username.findall(line):
			print link % (usr[1:], usr[1:])

if __name__ == '__main__':
	user_link()