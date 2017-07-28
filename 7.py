#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 15:21
# @Author  : Patrick.hu
# @Site    : 
# @File    : 7.py
# @Software: PyCharm

# 题目：将一个列表的数据复制到另一个列表中。

a = [1, 2, 3]
b = a[:]
c = a.copy()
d = [i for i in a]
print(a,b,c,d)