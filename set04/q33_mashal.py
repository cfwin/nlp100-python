#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt.sent.tok.stem | python set04/q33_mashal.py
"""

import argparse
import marshal
import sys

def reader(column, dict):
	D = marshal.load(open(dict))
	for line in sys.stdin:
		line = line.strip('\n')
		token = line.split('\t')[column - 1]
		if D.has_key(token):
			entries = []
			for item in D[token]:
				entries.append('(%s)' % ','.join(item))
			print '%s\t[%s]' % (line, ', '.join(entries))
		else:
			print line

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--column', type=int, default="2")
	parser.add_argument('-d', '--dict', type=str, default="inflection.table.txt.msl")
	args = parser.parse_args()
	return args

if __name__ == "__main__":
	args = parse_args()
	reader(args.column, args.dict)