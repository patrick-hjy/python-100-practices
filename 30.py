#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 15:27
# @Author  : Patrick.hu
# @Site    : 
# @File    : 30.py
# @Software: PyCharm

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
n = str(input("Input a number:"))
if n == n[::-1]:
    print("YES")
else:
    print("NO")
    