#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat medline.txt.sent.tok | python q36_bigram.py
"""

import sys

def word_bigram():
	sentence = []
	for line in sys.stdin:
		line = line.strip('\n')
		if not line:
			for i in xrange(len(sentence) - 1):
				print '\t'.join(sentence[i:i+2])
			print
			sentence = []
		else:
			sentence.append(line.split('\t')[1])

if __name__ == "__main__":
	word_bigram()