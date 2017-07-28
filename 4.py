#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 14:35
# @Author  : Patrick.hu
# @Site    : 
# @File    : 4.py
# @Software: PyCharm

# 输入某年某月某日，判断这一天是这一年的第几天？

m_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = 0
year = int(input('year:'))
month = int(input('month:'))
if year < 0:
    print("Error Data")
    year = int(input('year:'))
else:
    if year % 4 == 0 and year % 100 != 0 and month > 2:
        leap = 1
    elif year % 400 == 0 and month > 2:
        leap = 1
if month < 1 or month > 12:
    print("Error Data")
    month = int(input('month:'))

day = int(input('day:'))
if day > m_list[month - 1] + leap:
    print("Error Data")
    day = int(input('day:'))
else:
    while month > 1:
        day += m_list[month - 1]
        month -= 1
        day += leap
    print(day)
