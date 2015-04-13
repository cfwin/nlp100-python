#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Morph:
	def __init__(self, line):
		line = line.strip('\n')
		surface, features, ne = line.split('\t')
		features = features.split(',')
		self.surface = surface
		self.base = features[6]
		self.pos = features[0]
		self.pos1 = features[1]

	def __str__(self):
		return '%s\t%s' % (self.surface, ','.join((self.base, self.pos, self.pos1)))

def reader():
	S = []
	for line in sys.stdin:
		if line.startswith('*'):
			pass
		elif line.startswith('EOS'):
			yield S
			S = []
		else:
			S.append(Morph(line))

if __name__ == '__main__':
	for sentence in reader():
		for morph in sentence:
			print morph
		print