#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 13:35
# @Author  : Patrick.hu
# @Site    :
# @File    : 3.py
# @Software: PyCharm
# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

for m in range(1,168):
    for n in range(m):
        if (m-n)*(m+n) == 168:
            print(n*n-100)
