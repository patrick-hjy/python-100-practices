#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 17:59
# @Author  : Patrick.hu
# @Site    : 
# @File    : 50.py
# @Software: PyCharm

# 题目：输出一个随机数。

import random

print(random.random())  # 输入0-1之间的随机数
print(random.uniform(10, 20))  # 输出10-20之间的随机数
print(random.randint(10, 20))  # 输出10-20之间的随机整数
