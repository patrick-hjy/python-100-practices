#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 16:48
# @Author  : Patrick.hu
# @Site    : 
# @File    : 43.py
# @Software: PyCharm

# 题目：模仿静态变量(static)另一案例。


class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)


if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()
