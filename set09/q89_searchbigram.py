#! /usr/bin/python
# -*- coding: utf-8 -*-

db_name = 'nlp100_pizzaboi'

import pymongo

def search_by_bigram(bigrams):
	conn = pymongo.Connection()
	db = conn[db_name]

	q = [unicode(b) for b in bigrams]
	for doc in db.tweets.find({'bigram': {'$all': q}}, {'body':1}):
		print doc['body']

if __name__ == '__main__':
	search_by_bigram(['東北', '北大', '大学'])