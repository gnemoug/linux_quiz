#!/usr/bin/python
#-*-coding:utf-8-*-

result = {}

with open("test.txt") as rf:
    for temp in rf.readlines():
        temp_value = result.setdefault(temp.strip(),0)
        result[temp.strip()] = temp_value + 1

for k,v in result.items():
    print v,k
