#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 22:47
# @Author  : Patrick.hu
# @Site    : 
# @File    : 23.py
# @Software: PyCharm

# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def diamond(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'*'*(2*i-1)+' '*(n-i))
    for i in range(1,n):
        print(' '*i+'*'*(2*n-2*i-1)+' '*i)


if __name__ == '__main__':
    diamond(4)
