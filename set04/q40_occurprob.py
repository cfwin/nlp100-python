#! /usr/bin/python
# -*- coding: utf-8 -*-

import kyotocabinet
import math

def read_db(DB):
    """load the kyotocabinet type database DB"""
    db = kyotocabinet.DB()
    if not db.open(DB, kyotocabinet.DB.OWRITER | kyotocabinet.DB.OCREATE):
        sys.stderr.write('ERROR: failed to open: %s\n' % db.error())
    return db

def occurance_probability(sentence):
	db = read_db('conditional_probabitily.kch')
	sentence = sentence.split(' ')
	p = 1.0
	for i in xrange(len(sentence) - 1):
		bigram = db.get('(%s,%s)' % (sentence[i], sentence[i+1]))
		if not bigram:
			p = 0.0
			break
		else:
			p *= float(bigram)
	print p

if __name__ == "__main__":
	occurance_probability('this paper is organized as follows')
	occurance_probability('is this paper organized as follows')
