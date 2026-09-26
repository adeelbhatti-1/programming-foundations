# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:00:35 2022

@author: Student
"""
from math import exp
#def y(x):
#    y=exp(x)
#    return y
def df(h,y):
    return ( y[1] - y[0] ) / 1.0*h
def dff(h,x,y):
    return (y[0]-2*y[1]+y[2])/1.0*h**2
h=1
x=[0,1,2,3,4]
y=[exp(0),exp(1),exp(2),exp(3),exp(4)]
ds=[]
i=0
for i in range(len(x)-2):
    z=df(h,y[i:i+2])
    ds.append(z)
    print('df=[%d]=%.5f' %(x[i],z))
i=0
for i in range(len(x)-3):
    z=dff(h,x[i:i+3],y[i:i+3])
    ds.append(z)
    print('dff=[%d]=%.5f' %(x[i],z))