#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat japanese.txt.cabocha | python q55_dependency.py
"""

from q53_chunk import *

def unpunctuate(chunk):
	morph = chunk.morphs[-1]
	if morph.pos == '記号':
		return ''.join([m.surface for m in chunk.morphs[:-1]])
	return ''.join([m.surface for m in chunk.morphs])

def print_dependency():
	for S in reader():
		for chunk in S:
			print unpunctuate(chunk) + '\t' + unpunctuate(S[chunk.dst])
		print #end of sentence

if __name__ == '__main__':
	print_dependency()