#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat japanese.txt.cabocha | python q59_taigen.py
"""

from q53_chunk import *

def unpunctuate(chunk):
	morph = chunk.morphs[-1]
	if morph.pos == '記号':
		return ''.join([m.surface for m in chunk.morphs[:-1]])
	return ''.join([m.surface for m in chunk.morphs])

def has_pos(chunk, pos):
	for morph in chunk.morphs:
		if morph.pos == pos and morph.pos1 != '非自立':  #added
			return True
	return False

def print_dependency():
	for S in reader():
		for chunk in S:
			head, dep = chunk, S[chunk.dst]
			if has_pos(head, '名詞') and has_pos(dep, '名詞'):
				print unpunctuate(head) + ' --> ' + unpunctuate(dep)

if __name__ == '__main__':
	print_dependency()