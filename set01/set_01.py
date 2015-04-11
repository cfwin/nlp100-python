#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Functions dealing with some basic text processings

Most functions are NOT practical: There are more practical UNIX commands.
Note: This program should be written by functions."""

import argparse

def count_lines(args):
	"""count the number of lines in [src]"""
	print sum(1 for line in open(args.src))

def replace(args):
	"""replace [old] with [new] in [src]"""
	for line in open(args.src):
		print line.strip('\n').replace('\t', ' ')

def extract_field_values(args):
	"""extract [target]th field value from [src]"""
	for line in open(args.src):
		print line.strip('\n').split(args.sep)[args.target - 1]

def merge_field_values(args):
	"""merge [file_1], [file_2], ..., [file_N] vertically, separated by [sep]"""
	fin = [open(src) for src in args.target]
	while True:
		lines = map(lambda x: x.readline(), fin)
		if not all(lines):
			break
		print args.sep.join([line.strip('\n') for line in lines])

def first_n(args):
	"""print the first [n] lines"""
	count = 0
	for line in open(args.src):
		count += 1
		if count > args.n:
			break
		print line.strip('\n')

def last_n(args):
	"""print the last [n] lines"""
	bf = []; p = 0
	for line in open(args.src):
		if len(bf) < args.n:
			bf.append(line)
		else:
			bf[p] = line
		p = (p + 1) % args.n

	R = range(len(bf)) if len(bf) < args.n else range(p, args.n) + range(0, p)
	for i in R:
		print bf[i].strip('\n')

def count_distinct(args):
	"""count the distinct number of the strings in the [n]th field"""
	D = set()
	for line in open(args.src):
		D.add(line.strip('\n').split(args.sep)[args.column - 1])
	print len(D)

def sort_by_dict(args):
	"""sort lines by dictionary order of the [n]th field"""
	D = [line.strip('\n').split(args.sep) for line in open(args.src)]
	for item in sorted(D, key=lambda x: x[args.column - 1]):
		print args.sep.join(item)

def sort_by_dict_reverse(args):
	"""sort lines by reverse dictionary order of the [n]th field, and the [n]th field"""
	D = [line.strip('\n').split(args.sep) for line in open(args.src)]
	for item in sorted(D, key=lambda x: (x[args.column1 - 1], x[args.column2 - 2])):
		print args.sep.join(item)

def freq_and_sort(args):
	"""generate a ranked list of strings in the [n]th field"""
	from collections import defaultdict
	D = defaultdict(int)
	for line in open(args.src):
		D[line.strip('\n').split(args.sep)[args.column - 1]] += 1
	count = 0
	for k, v in sorted(D.iteritems(), key=lambda x: x[1], reverse=True):
		count += 1
		if count > args.top:
			break
		print args.sep.join((k, str(v)))

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--src', type=str, default='address.txt')

	subparsers = parser.add_subparsers()

	parser_q1 = subparsers.add_parser('q1')
	parser_q1.set_defaults(func=count_lines)

	parser_q2 = subparsers.add_parser('q2')
	parser_q2.add_argument('-o', '--old', type=str, default= '\t')
	parser_q2.add_argument('-n', '--new', type=str, default=' ')
	parser_q2.set_defaults(func=replace)

	parser_q3 = subparsers.add_parser('q3')
	parser_q3.add_argument('-t', '--target', type=int, default=1)
	parser_q3.add_argument('-s', '--sep', type=str, default='\t')
	parser_q3.set_defaults(func=extract_field_values)

	parser_q4 = subparsers.add_parser('q4')
	parser_q4.add_argument('-t', '--target', type=str, action='append', default=['col1.txt', 'col2.txt'])
	parser_q4.add_argument('-s', '--sep', type=str, default='\t')
	parser_q4.set_defaults(func=merge_field_values)

	parser_q5 = subparsers.add_parser('q5')
	parser_q5.add_argument('-n', type=int, default=10)
	parser_q5.set_defaults(func=first_n)
	
	parser_q6 = subparsers.add_parser('q6')
	parser_q6.add_argument('-n', type=int, default=10)
	parser_q6.set_defaults(func=last_n)

	parser_q7 = subparsers.add_parser('q7')
	parser_q7.add_argument('-c', '--column', type=int, default=1)
	parser_q7.add_argument('-s', '--sep', type=str, default='\t')
	parser_q7.set_defaults(func=count_distinct)

	parser_q8 = subparsers.add_parser('q8')
	parser_q8.add_argument('-c', '--column', type=int, default=2)
	parser_q8.add_argument('-s', '--sep', type=str, default='\t')
	parser_q8.set_defaults(func=sort_by_dict)

	parser_q9 = subparsers.add_parser('q9')
	parser_q9.add_argument('-c', '--column1', type=int, default=2)
	parser_q9.add_argument('-d', '--column2', type=int, default=1)
	parser_q9.add_argument('-s', '--sep', type=str, default='\t')
	parser_q9.set_defaults(func=sort_by_dict_reverse)

	parser_q10 = subparsers.add_parser('q10')
	parser_q10.add_argument('-c', '--column', type=int, default=2)
	parser_q10.add_argument('-s', '--sep', type=str, default='\t')
	parser_q10.add_argument('-t', '--top', type=int, default=99999)
	parser_q10.set_defaults(func=freq_and_sort)

	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	args.func(args)