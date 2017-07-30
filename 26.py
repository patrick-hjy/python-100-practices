#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 14:14
# @Author  : Patrick.hu
# @Site    : 
# @File    : 26.py
# @Software: PyCharm

# 题目：利用递归方法求5!。

def mul(n):
    if n>1:
        return n*mul(n-1)
    else:
        return 1

if __name__ == '__main__':
    print(mul(5))