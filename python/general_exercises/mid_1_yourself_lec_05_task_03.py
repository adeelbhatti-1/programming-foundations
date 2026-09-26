# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:32:04 2022

@author: Student
"""

from math import pi,sin
def f(x):
    if 0<=x<=pi:
        y=sin(x)
    else:
        y=0
    return y
x=(90*pi)/180
y=f(x)
print('y=%.2f at x=%.2f' %(y,x))