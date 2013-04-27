#!/usr/bin/python
#-*-coding:utf-8-*-

from pprint import pprint

with open("filename") as rf:
    result = [i.strip() for i in rf.readlines() if "48" not in i]
    pprint(result)
