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

def search(q):
	conn = pymongo.Connection()
	db = conn[db_name]

	q_bigram = bigram(q)
	for doc in db.tweets.find({'bigram':{'$all':q_bigram}}).sort('rtf',-1):
		if q in doc['body']:
			print str(doc['rtf']) + '\t' + doc['body']

	conn.disconnect()

if __name__ == '__main__':
	search('天気')