#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 14:17
# @Author  : Patrick.hu
# @Site    : 
# @File    : 27.py
# @Software: PyCharm

# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def strr(s):
    print(s[-1])
    if len(s) > 1:
        strr(s[:-1])

strr(input('Input a string:'))