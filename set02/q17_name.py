#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets.txt.gz | python q17_name.py
TODO:
1. エラーの排除: お母さん、お父さん、彼氏など
2. cueの追加: 様、君、先生、選手など
"""

import re
import sys

def search_name():
	name = re.compile(ur'([一-龠]+)(さん|くん|ちゃん|氏)')
	for line in sys.stdin:
		line = line.strip('\n')
		for m in name.finditer(unicode(line)):
			print m.group(1)

if __name__ == '__main__':
	search_name()