#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 21:23
# @Author  : Patrick.hu
# @Site    : 
# @File    : 19.py
# @Software: PyCharm

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
list2 = []
for i in range(1, 1000):
    list1 = []
    for j in range(1, i):
        if i % j == 0:
            list1.append(j)
    if i == sum(list1):
        list2.append(i)
print(list2)
