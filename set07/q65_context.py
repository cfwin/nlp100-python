#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
from chunkreader import *

def noun_phrase(chunk):
	np = ''
	nplist =[]
	for morph in chunk.morphs:
		if morph.pos == '名詞':
			np += morph.surface
		elif morph.pos != '名詞' and np:
			nplist.append(np)
			np = ''
	return nplist

def print_context(S, np, direction, nodes):
	nodes = [nodes,] if type(nodes) == int else nodes
	for node in nodes:
		if node >= 0:
			for morph in S[node].morphs:
				if morph.pos in ('名詞', '動詞', '形容詞'):
					print '%s\t%s %s' % (np, direction, morph.base)

def context():
	top100 = [line.strip('\n').split('\t')[1] for line in open('tfidf100.lst')]
	srcs = 'chapter7cabocha/'
	for src in os.listdir(srcs):
		for S in reader(open(srcs + src)):
			for chunk in S:
				nplist = noun_phrase(chunk)
				for np in nplist:
					if np in top100:
						print_context(S, np, '->', chunk.dst)
						print_context(S, np, '<-', chunk.srcs)

if __name__ == '__main__':
	context()