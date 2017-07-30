#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 17:44
# @Author  : Patrick.hu
# @Site    : 
# @File    : 46.py
# @Software: PyCharm

# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    num = float(input("input a number:\n"))
    r = num ** 2
    if r < 50:
        quit()
    else:
        print(r)