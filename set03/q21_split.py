#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def split_by_period():
	for line in sys.stdin:
		for sentence in line.strip('\n').split('. '):
			print sentence

if __name__ ==  "__main__":
	split_by_period()
