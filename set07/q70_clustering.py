#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def order(x, y):
	return (x, y) if x < y else (y, x)

def reader():
	D = {}
	V = set()
	for line in sys.stdin:
		d, x, y = line.strip('\n').split('\t')
		x, y = order(x, y)
		d = 1.0 - float(d)
		D[(x,y)] = d
		V.add((x,))
		V.add((y,))
	return D, list(V)

def max_distance(D, c1, c2):
	d_max = -1.0
	for x in c1:
		for y in c2:
			z = order(x, y)
			if z in D:
				d_max = D[z] if D[z] > d_max else d_max
	d_max = 100.0 if d_max == -1.0 else d_max
	return d_max

def clustering(D, cluster):
	while True:
		d_min = 100
		for i in xrange(len(cluster) - 2):
			cur = cluster[i]
			for rest in cluster[i+1:]:
				d = max_distance(D, cur, rest)
				if d < d_min:
					x = cur
					y = rest
					d_min = d

		if d_min > 0.2:
			break
		cluster.remove(x)
		cluster.remove(y)
		cluster.append(x+y)
	return cluster

def main():
	D, cluster = reader()
	clustered = clustering(D, cluster)
	for c in clustered:
		for item in c:
			print item,
		print


if __name__ == '__main__':
	main()
