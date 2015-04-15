#! /usr/bin/python
# -*- coding: utf-8 -*-

from geniareader import *

def noun_phrase():
	for S in reader():
		np = []
		for token in S:
			if token.chunk == 'B-NP':
				np = [token]
			elif token.chunk == 'I-NP':
				np.append(token)
			else:
				if np:
					print '# %s' % ' '.join([t.w for t in np])

if __name__ == '__main__':
	noun_phrase()