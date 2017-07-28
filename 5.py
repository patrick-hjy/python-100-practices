#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 15:03
# @Author  : Patrick.hu
# @Site    : 
# @File    : 5.py
# @Software: PyCharm
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

x= int(input("x:"))
y= int(input("y:"))
z= int(input("z:"))
list = [x,y,z]
print(sorted(list))