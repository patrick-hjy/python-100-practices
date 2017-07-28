#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 17:13
# @Author  : Patrick.hu
# @Site    : 
# @File    : 13.py
# @Software: PyCharm

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for m in range(100, 1000):
    list_m = list(str(m))
    sumup = 0
    for i in list_m:
        sumup += int(i) ** 3
    if m == sumup:
        print(m)
