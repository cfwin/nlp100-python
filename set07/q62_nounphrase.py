#! /usr/bin/python
# -*- coding: utf-8 -*-

from chunkreader import *

def noun_phrase():
	np = ''
	nplist = []
	for S in reader():
		for chunk in S:
			for morph in chunk.morphs:
				if morph.pos == '名詞':
					np += morph.surface
				else:
					if np:
						print np
						np = ''
			if np:
				print np

if __name__ == '__main__':
	noun_phrase()