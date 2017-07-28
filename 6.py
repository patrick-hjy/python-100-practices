#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 15:12
# @Author  : Patrick.hu
# @Site    : 
# @File    : 6.py
# @Software: PyCharm

# 题目：斐波那契数列

def fib(x):
    if 0 < x < 3:
        print(1)
    else:
        a = 1
        b = 1
        while x > 2:
            a, b = b, a + b
            x -= 1
        print(b)


fib(10)
