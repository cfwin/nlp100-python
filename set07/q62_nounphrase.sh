#! /bin/sh

srcs=chapter7cabocha
for file in `ls chapter7cabocha`
do
	dst=chapter7np/${file}.n
	cat ${srcs}/${file} | python set07/q62_nounphrase.py > ${dst}
done

