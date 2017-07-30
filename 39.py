#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 16:14
# @Author  : Patrick.hu
# @Site    : 
# @File    : 39.py
# @Software: PyCharm

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

L = [1,2,3,4,5,6,7,8,9,10]
n = int(input("input a number:\n"))
for i in range(len(L)):
    if n<L[i]:
        L.insert(i-1,n)
        break
else:
    L.append(n)
print(L)