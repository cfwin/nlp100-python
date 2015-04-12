#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt.sent.tok | python q36_bigram.py | python q38_condprob.py
"""

import kyotocabinet
import sys
from collections import defaultdict

def read_db(DB):
    """load the kyotocabinet type database DB"""
    db = kyotocabinet.DB()
    if not db.open(DB, kyotocabinet.DB.OWRITER | kyotocabinet.DB.OCREATE):
        sys.stderr.write('ERROR: failed to open: %s\n' % db.error())
    return db
        
def conditional_probability():
	D = defaultdict(lambda : defaultdict(int))
	for line in sys.stdin:
		line = line.strip('\n')
		if line:
			w, z = line.split('\t')
			D[w][z] += 1
	return D

def main():
	DB = 'conditional_probabitily.kch'
	db = kyotocabinet.DB()
	if not db.open(DB, kyotocabinet.DB.OWRITER | kyotocabinet.DB.OCREATE):
		sys.stderr.write('ERORR: failed to open: %s\n' % db.error())
	for w, v in conditional_probability().iteritems():
		for z, v2 in v.iteritems():
			prob = 1.0 * v2 / sum(v.values())
			db.set('(%s,%s)' % (w, z), str(prob))
	if not db.close():
		sys.stderr.write('ERROR: failed to close: %s\n' % db.error())

if __name__ == '__main__':
	main()
