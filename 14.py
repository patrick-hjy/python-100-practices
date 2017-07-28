#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 17:18
# @Author  : Patrick.hu
# @Site    : 
# @File    : 14.py
# @Software: PyCharm

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
list1 = []


def divide_num(n):
    m = n
    for i in range(2, n):
        while n % i == 0:
            list1.append(i)
            n = n // i
    if list1:
        print(str(m) + '=' + '*'.join([str(x) for x in list1]))
    else:
        print("输入的数不可分解")


if __name__ == '__main__':
    divide_num(1000)
