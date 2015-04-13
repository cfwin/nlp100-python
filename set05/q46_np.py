#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def readiter():
	sentence = []
	for line in sys.stdin:
		line = line.strip('\n')
		if line == 'EOS':
			yield sentence
			sentence = []
		else:
			surface, feature = line.split('\t')
			features = feature.split(',')
			names = ('surface', 'base', 'pos', 'pos1')
			attrs = (surface, features[6], features[0], features[1])
			sentence.append(dict(zip(names, attrs)))

def extract_noun_phrase():
	for S in readiter():
		for i in xrange(len(S) - 1):
			if S[i]['pos'] == '名詞' and S[i+1]['pos'] == '名詞':
				print '%(surface)s\t%(base)s\t%(pos)s\t%(pos1)s' % S[i]
				print '%(surface)s\t%(base)s\t%(pos)s\t%(pos1)s' % S[i+1]
				print

if __name__ == '__main__':
	extract_noun_phrase()

