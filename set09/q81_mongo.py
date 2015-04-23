#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: gzcat tweets100.tsv.gz | python q81_mongo.py

$ mongo
> use [dbname]
> db.stats()
"""

import pymongo
import sys

db_name = 'nlp100_pizzaboi'

def tweet2dict(line):
	names = ('url','data','user','name','body','rt','rep','qt','rtf','repf','qtf')
	line = line.strip('\n').split('\t')
	if len(line) == 11:
		D = dict(zip(line, names))
	return D

if __name__ == '__main__':
	conn = pymongo.Connection()
	db = conn[db_name]
	col = db['tweets']

	for line in sys.stdin:
		col.insert( tweet2dict(line) )

