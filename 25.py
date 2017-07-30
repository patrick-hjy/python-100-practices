#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 14:11
# @Author  : Patrick.hu
# @Site    : 
# @File    : 25.py
# @Software: PyCharm

# 题目：求1+2!+3!+...+20!的和。

r = 0
for i in range(1,21):
    r_i = 1
    while i>1:
        r_i *= i
        i-=1
    r +=r_i
print(r)