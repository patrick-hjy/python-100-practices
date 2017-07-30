#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 17:52
# @Author  : Patrick.hu
# @Site    : 
# @File    : 49.py
# @Software: PyCharm

# 题目：使用lambda来创建匿名函数。
num = float(input("input a number"))
f = lambda x: x**2
print("number's square is {}".format(f(num)))
