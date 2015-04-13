#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat japanese.txt.mecab | python set05/q47_parser.py
OPTION:
	unigram -o pos=動詞
	bigram -o pos=名詞 pos=名詞
	trigram -o pos=名詞 surface=の pos=名詞
・半角スペース区切りで項目を指定
・半角イコール区切りで内容を指定（surface, pos, pos1, base）

TODO:
ドキュメントの追加
各項目に対して複数の条件 (e.g. pos=名詞|pos1=サ変接続)
ngramを自動で判定 (if文をqの長さで自動生成)
"""

import argparse
import sys

def readiter():
	sentence = []
	for line in sys.stdin:
		line = line.strip('\n')
		if line == 'EOS':
			yield sentence
			sentence = []
		else:
			surface, feature = line.split('\t')
			features = feature.split(',')
			names = ('surface', 'base', 'pos', 'pos1')
			attrs = (surface, features[6], features[0], features[1])
			sentence.append(dict(zip(names, attrs)))

def extract_unigram(args):
	attr, value = args.option.split('=')
	for S in readiter():
		for token in S:
			if token[attr] == value:
				print token[args.target]

def extract_bigram(args):
	q = [option.split('=') for option in args.option]
	for S in readiter():
		for i in xrange(len(S) - 1):
			if S[i][q[0][0]] == q[0][1] and S[i+1][q[1][0]] == q[1][1]:
				print S[i][args.target] + S[i+1][args.target]

def extract_trigram(args):
	q = [option.split('=') for option in args.option]
	for S in readiter():
		for i in xrange(len(S) - 2):
			if S[i][q[0][0]] == q[0][1] and S[i+1][q[1][0]] == q[1][1] and S[i+2][q[2][0]] == q[2][1]:
				print S[i][args.target] + S[i+1][args.target] + S[i+2][args.target]

def parse_args():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers()

	parser_unigram = subparsers.add_parser('unigram')
	parser_unigram.add_argument('-o', '--option', type=str, default='pos=動詞')
	parser_unigram.add_argument('-t', '--target', type=str, default='surface')
	parser_unigram.set_defaults(func=extract_unigram)

	parser_bigram = subparsers.add_parser('bigram')
	parser_bigram.add_argument('-o', '--option', type=str, action='append', default=['pos=名詞', 'pos=名詞'])
	parser_bigram.add_argument('-t', '--target', type=str, default='surface')
	parser_bigram.set_defaults(func=extract_bigram)

	parser_trigram = subparsers.add_parser('trigram')
	parser_trigram.add_argument('-o', '--option', type=str, action='append', default=['pos=名詞', 'surface=の', 'pos=名詞'])
	parser_trigram.add_argument('-t', '--target', type=str, default='surface')
	parser_trigram.set_defaults(func=extract_trigram)

	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	args.func(args)

