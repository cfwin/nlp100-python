#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pymongo

"""
USAGE: python q86_mongourl.py [url]

#test_url: http://twitter.com/tenkijp/statuses/46096978970550273
"""

db_name = 'nlp100_pizzaboi'

def serach_by_url(url):
	conn = pymongo.Connection()
	db = conn[db_name]

	for tweet in db.tweets.find({'url':url}):
		print t['body']

	conn.disconnect()

if __name__ == '__main__':
	serach_by_url(sys.argv[1])