#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_histogram():
	histo = []
	for line in sys.stdin:
		word, freq = line.strip('\n').split('\t')
		histo.append(int(freq))

	plt.hist(histo, 100, range=(1,100))
	plt.xlabel('frequency')
	plt.ylabel('distinct number of words')
	plt.title('histogram of frequency')
	plt.axis([0, 100, 0, 400])
	plt.savefig('049.png')

if __name__ == '__main__':
	plot_histogram()