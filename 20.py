#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 21:51
# @Author  : Patrick.hu
# @Site    : 
# @File    : 20.py
# @Software: PyCharm

# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


def ball(n):
    height = 100
    sum_length = -100
    while n > 0:
        sum_length += height*2
        height = height / 2
        n -= 1
    print(sum_length, height)

if __name__ == '__main__':
    ball(10)
    ball(1)