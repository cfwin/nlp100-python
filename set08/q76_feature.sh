#! /bin/sh

for i in `seq 0 4`
do
	gzcat data0${i}.genia.gz | python set08/q75_feature.py > data0${i}.f
done