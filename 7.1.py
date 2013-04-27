#!usr/bin/python
#-*-coding:utf-8-*-

with open('test.txt','r+') as rwf:
    new_content = list(set(rwf.readlines()))
    rwf.seek(0)
    rwf.writelines(new_content)
    rwf.truncate(rwf.tell())
