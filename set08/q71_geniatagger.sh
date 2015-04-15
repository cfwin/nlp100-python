#! /bin/sh

for i in `seq 0 4`
do
	gzcat data0${i}.txt.gz | python set03/q22_split.py | geniatagger > data0${i}.genia.gz
done