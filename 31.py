#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 15:29
# @Author  : Patrick.hu
# @Site    : 
# @File    : 31.py
# @Software: PyCharm

# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
s = input("first letter:")
if s.lower() == 'm':
    print(list[0])
elif s.lower() == 'w':
    print(list[2])
elif s.lower() == 'f':
    print(list[4])
else:
    s2 = input("second letter:")
    if s.lower() == 't' and s2.lower() == 'u':
        print(list[1])
    elif s.lower() == 't':
        print(list[3])
    elif s2.lower() == 'a':
        print(list[5])
    elif s2.lower() == 'u':
        print(list[6])
    else:
        print("error input")
