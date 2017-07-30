#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 15:03
# @Author  : Patrick.hu
# @Site    : 
# @File    : 29.py
# @Software: PyCharm

# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

n = str(input("Input a number:"))
x=len(n)
print(x)
print(n[::-1])