#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 16:09
# @Author  : Patrick.hu
# @Site    : 
# @File    : 38.py
# @Software: PyCharm

# 题目：求一个3*3矩阵对角线元素之和。

"""
    1  2  3
    4  5  6
    7  8  9
"""

import numpy as np

x = np.arange(1, 10)
y = x.reshape((3, 3))
r = 0
for i in range(len(y)):
    r+=y[i][i]
print(r)