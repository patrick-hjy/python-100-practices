#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 15:57
# @Author  : Patrick.hu
# @Site    : 
# @File    : 10.py
# @Software: PyCharm

# 题目：暂停一秒输出，并格式化当前时间。

import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))