#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 16:02
# @Author  : Patrick.hu
# @Site    : 
# @File    : 34.py
# @Software: PyCharm

# 题目：练习函数调用。

def first():
    print("Hello world!")

def three():
    for i in range(3):
        first()

if __name__ == '__main__':
    three()