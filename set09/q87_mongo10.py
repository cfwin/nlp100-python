#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: python q87_mongo10.py [username]

#test_username: tenkijp
"""

import pymongo

db_name = 'nlp100_pizzaboi'

def most_retweeted(username):
	conn = pymongo.Connection()
	db = conn[db_name]

	for t in db.tweets.finf({'user:username'}).sort('rtd', -1).limit(10):
		print t['rtf'] + '\t' + t['body']

	conn.disconnect()

if __name__ == '__main__':
	most_retweeted(sys.argv[1])