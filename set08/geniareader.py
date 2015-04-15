#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Genia:
	def __init__(self, w, lem, pos, chunk):
		self.w = w
		self.lem = lem
		self.pos = pos
		self.chunk = chunk

	def __str__(self):
		return self.w

def reader():
	S = []
	names = ('w', 'lem', 'pos', 'chunk')
	for line in sys.stdin:
		line = line.strip('\n')
		if not line:
			yield S
			S = []
		else:
			args = dict(zip(names, tuple(line.split('\t'))))
			S.append(Genia(**args))

if __name__ == '__main__':
	for S in reader():
		for token in S:
			print token,
		print 
