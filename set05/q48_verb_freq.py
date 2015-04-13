#cat japanese.txt.mecab | python set05/q47_parser.py unigram -o pos=動詞 -t base > verbs.lst
#python set01/set01.py --src=verbs.lst q10 -c1