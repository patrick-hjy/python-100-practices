#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 17:23
# @Author  : Patrick.hu
# @Site    : 
# @File    : 44.py
# @Software: PyCharm

# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

import numpy as np

x = np.array(X)
y = np.array(Y)
print(x + y)

L2 = []
for i in range(len(X)):
    L = []
    for j in range(len(X[i])):
        L.append(X[i][j]+Y[i][j])
    L2.append(L)
print(L2)
