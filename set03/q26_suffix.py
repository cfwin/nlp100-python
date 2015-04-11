#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def suffix():
	less = set()
	ly = set()
	for line in sys.stdin:
		token = line.strip('\n').split('\t')[1]
		if token.endswith('ness'):
			less.add(token[:-4])
		elif token.endswith('ly'):
			ly.add(token[:-2])
	for co in less.intersection(ly):
		print co

if __name__ == '__main__':
	suffix()