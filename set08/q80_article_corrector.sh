#! /bin/sh

echo $1 | geniatagger | python set08/q75_feature.py | classias-tag -m model.txt -st -f -k