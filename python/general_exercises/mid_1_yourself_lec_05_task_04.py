# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:44:05 2022

@author: Student
"""

def f(x):
    if x<0:
        y=0
    elif 0<=x<1:
        y=x
    elif 1<=x<2:
        y=2-x
    else:
        y=0
    return y
x=-1
while(x<=3):
    y=f(x)
    #print('f(%.d)=%.2f' %(x , f(x))
    print('f(%.1f)=%.1f' %(x,f(x)))
    x=x+0.2