#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import operator

filename = sys.argv[1]

result = {}

with open(filename) as rf:
    for temp in rf.readlines():
        temp_value = result.setdefault(temp.strip(),0)
        result[temp.strip()] = temp_value + 1

result = sorted(result.items(), key=operator.itemgetter(1))
result = result[::-1]
for k,v in result:
    print v,k
