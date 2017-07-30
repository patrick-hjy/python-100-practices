#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 16:06
# @Author  : Patrick.hu
# @Site    : 
# @File    : 36.py
# @Software: PyCharm

# 题目：求100之内的素数。

l =[]
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        l.append(i)
print(l)