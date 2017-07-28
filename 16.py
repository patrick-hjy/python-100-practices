#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 17:51
# @Author  : Patrick.hu
# @Site    : 
# @File    : 16.py
# @Software: PyCharm

# 题目：输出指定格式的日期。

import time,datetime

print(time.time())

print(time.localtime())

print(time.asctime())

print(time.strftime('%Y-%m-%d %H:%M:%S'))