#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 15:24
# @Author  : Patrick.hu
# @Site    : 
# @File    : 8.py
# @Software: PyCharm

# 题目：输出 9*9 乘法口诀表。

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print(str(i) + '*' + str(j) + '=' + str(i * j), '\t', end='')

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("{}*{}={}".format(i, j, i * j), '\t', end='')
