#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 16:30
# @Author  : Patrick.hu
# @Site    : 
# @File    : 42.py
# @Software: PyCharm


# 题目：学习使用auto定义变量的用法。


num = 2


def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1


for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()
