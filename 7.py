#!/usr/bin/python
#-*-coding:utf-8-*-

unique_content = []

with open("test.txt") as rf:
    unique_content = list(set(rf.readlines()))

with open("test.txt",'w') as wf:
    wf.writelines(unique_content)
