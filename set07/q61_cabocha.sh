#! /bin/sh

srcs=chapter7
for file in `ls ${srcs}`
do
	dst=chapter7cabocha/${file}
	nkf -w ${srcs}/${file} | sed 's/。/。\\n/g' | cabocha -f1 > dst
done
