#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
improved version of q73_np.py
USAGE: gzcat data00.genia.gz | python q74_article.py
"""

from geniareader import *

def article_tag(np):
	if np.lower().startswith('the '):
		return 'THE'
	elif np.lower().startswith(('a ', 'an ')):
		return 'A'
	else:
		return 'NONE'

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
					np_str = ' '.join([t.w for t in np])
					print '#%s\n%s' % (np_str, article_tag(np_str))
				np = []
		print

if __name__ == '__main__':
	noun_phrase()