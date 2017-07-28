#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 16:36
# @Author  : Patrick.hu
# @Site    : 
# @File    : 11.py
# @Software: PyCharm

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

"""等同斐波那契数列"""


def fib(n):
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    print(fib(30))
