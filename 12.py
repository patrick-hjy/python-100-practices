#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 16:50
# @Author  : Patrick.hu
# @Site    : 
# @File    : 12.py
# @Software: PyCharm

# 题目：判断101-200之间有多少个素数，并输出所有素数。
list1 = []
for i in range(101,201):
    for j in range(2,101):
        if i%j == 0:
            break
    else:
        list1.append(i)
print(list1)