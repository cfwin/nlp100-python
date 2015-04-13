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

def extract_verbs():
	for sentence in readiter():
		for token in sentence:
			if token['pos'] == '動詞':
				#print '%(surface)s\t%(base)s\t%(pos)s\t%(pos1)s' % token
				print token['base']
		print

if __name__ == '__main__':
	extract_verbs()

