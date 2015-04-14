#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
improved version of q52_morph.py
USAGE: cat japanese.txt.cabocha | python set06/q53_chunk.py
"""

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

class Chunk:
	def __init__(self, line):
		line = line.split(' ') #* 0 7D 0/0 4.270366
		self.morphs = []
		self.index = int(line[1])
		self.dst = int(line[2].strip('D'))
		self.srcs = [] #int

	def __str__(self):
		return '%d\t%s\t%d\t(%s)' % (self.index,
								''.join(m.surface for m in self.morphs),
								self.dst,
								','.join([str(src) for src in self.srcs]))

def reader():
	S = []
	for line in sys.stdin:
		if line.startswith('*'):
			S.append(Chunk(line)) #new chunk
		elif line.startswith('EOS'):
			#get srcs
			for chunk in S:
				if chunk.dst != -1:
					S[chunk.dst].srcs.append(chunk.index)
			yield S
			S = []
		else:
			S[-1].morphs.append(Morph(line)) #add Morph

if __name__ == '__main__':
	for sentence in reader():
		for chunk in sentence:
			print chunk
