#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
improved version of q74_article.py
USAGE: gzcat data00.genia.gz | python q75_feature.py > data00.f
"""

from collections import defaultdict
from geniareader import *

def article_tag(head):
	if head.lower() == 'the':
		return 'THE'
	elif head.lower() in ('a', 'an'):
		return 'A'
	else:
		return 'NONE'

def extract_features():
	for S in reader():
		seq = []
		start = -1
		#start and end point of np
		for i in xrange(len(S) - 1):
			if S[i].chunk == 'B-NP':
				start = i
			elif S[i].chunk == 'I-NP':
				pass
			elif start != -1:
				seq.append((start, i-1))
				start = -1
		if start != -1:
			seq.append((start, len(S)-1))

		#features
		for s, e in seq:
			f = {}
			f['hw'] = S[e].w
			f['hpos'] = S[e].pos
			f['hw|hpos'] = S[e].w + '|' + S[e].pos
			f['fw'] = S[s].w
			f['fpos'] = S[s].pos
			f['fw|fpos'] = S[s].w + '|' + S[s].pos
			f['w[0]'] = ' '.join([token.w for token in S[s:e + 1]])
			f['w[-1]'] = S[i - 1].w if i - 1 > 0 else 'NONE'
			f['pos[-1]'] = S[i - 1].pos if i - 1 > 0 else 'NONE'
			f['w[1]'] = S[e + 1].w if e < len(S) - 1 else 'NONE'
			f['pos[1]'] = S[e + 1].pos if e < len(S) - 1 else 'NONE'

			print '#%s' % f['w[0]']
			print article_tag(f['fw']),
			for k, v in f.iteritems():
				print '\t%s:%s' % (k, v),
			print

if __name__ == '__main__':
	extract_features()