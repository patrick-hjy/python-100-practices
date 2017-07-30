#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 14:05
# @Author  : Patrick.hu
# @Site    : 
# @File    : 24.py
# @Software: PyCharm

# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def fib(n):
    a,b = 1,1
    while n>1:
        a,b = b, a+b
        n-=1
    return b

if __name__ == '__main__':
    r= 0
    for i in range(1,21):
        r = r + fib(i+1)/fib(i)
    print(r)