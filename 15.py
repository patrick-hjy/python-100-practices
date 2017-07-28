#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 17:35
# @Author  : Patrick.hu
# @Site    : 
# @File    : 15.py
# @Software: PyCharm

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = int(input("score:"))
if score>=90:
    print("A")
elif 90>score>=60:
    print("B")
elif score<60:
    print("C")
else:
    print("Error Score")