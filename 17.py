#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 18:27
# @Author  : Patrick.hu
# @Site    : 
# @File    : 17.py
# @Software: PyCharm

s = input("input a string:\n")
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print("char = {},space = {},digit = {},others = {}".format(letters, space, digit, others))
