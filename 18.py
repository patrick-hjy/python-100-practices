#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 18:43
# @Author  : Patrick.hu
# @Site    : 
# @File    : 18.py
# @Software: PyCharm

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
def sumup(n, a):
    num = 0
    m = n
    while n > 0:
        num += n * a * 10 ** (m - n)
        n -= 1
    print(num)

if __name__ == '__main__':
    n = int(input("n:"))
    a = int(input("m:"))
    sumup(n, a)

