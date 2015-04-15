#! /usr/bin/python
# -*- coding: utf-8 -*-

import math
import os
from collections import defaultdict

"""
USAGE: python q63_tfidf.py
NOTE:
noun phrase extracted file needed. (execute q62_nounphrase.sh)
"""

def tfidf(srcs):
	N = 0 #number of documents
	tf = defaultdict(int)
	df = defaultdict(int)

	for src in os.listdir(srcs):
		N += 1
		V = set() #vocabulary

		#term frequency;
		#the number of times the term appeared in all documents
		for line in open(srcs + src):
			term = line.strip('\n')
			tf[term] += 1
			V.add(term)

		#document frequency;
		#number of documents in which the term appeared
		for term in V:
			df[term] += 1

	#calculate tf*idf = freq(w) * log(N / df(w))
	#tf*idf reflects how important a term is to a document in a corpus
	for term, tf in tf.iteritems():
		tfidf = tf * math.log(N / float(df[term]))
		print '%s\t%f\t%d\t%d' % (term, tfidf, tf, df[term])

if __name__ == '__main__':
	tfidf('chapter7np/')
