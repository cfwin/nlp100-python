#! /usr/bin/python
# -*- coding: utf-8 -*-

import pymongo

db_name = 'nlp100_pizzaboi'

def bigram(sentence):
	bigrams = []
	sentence_uni = unicode(sentence)
	for i in xrange(len(sentence_uni) - 1):
		bigrams.append(sentence_uni[i:i+2])
	return bigrams

def tweet2dict(t):
	names = ('url','data','user','name','body','rt','rep','qt','rtf','repf','qtf','bigram')
	t = t.strip('\n').split('\t')
	t.append(bigram(t[4]))
	if len(t) == 12:
		D = dict(zip(t, names))
	return D

if __name__ == '__main__':
	conn = pymongo.Connection()
	db = conn[db_name]

	for t in sys.stdin:
		db.tweets.insert( tweet2dict(t) )
	db.tweets.create_index([
		('url', 1),
		('date', 1),
		('user', 1),
		('rt', 1),
		('rep', 1),
		('qt', 1),
		('bigram', 1))