#!/usr/bin/env python
# -*- coding: utf-8 -*-


import codecs

filename = 'date.txt'

start = raw_input(u"1.录入2.测试").decode('utf-8')
i = 0 #统计正确率
j = 0 #统计答题数

def test(filename):
     f  = codecs.open(filename,'r','utf-8')
     texts = f.readlines()
     for text in texts:

         info = text.strip().split(',')
         print info[0]
         nh = raw_input(u"日文：").decode('utf-8')
         if info[1]==nh:
             print u"正确"
         else:
             print u"回答不正确"
             print u"正确为："+ info[1]
             continue

while True:

    if start =='1':

        f  = codecs.open(filename,'a','utf-8')
        zw = raw_input(u"中文:").decode('utf-8')
        rw = raw_input(u"日文:").decode('utf-8')
        if zw<>'':
            f.write(u"%s,%s\n"%(zw,rw))
        else:
            f.close()
            break
    elif start =='2':
        f  = codecs.open(filename,'r','utf-8')
        test(filename)
        break

f.close()

