# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 05:32:20 2022

@author: Student
"""
#functions should be defined within the file not on another file
#we can import functions from file like from FUnction import myname,exponent
from math import sin,cos,tan
#called function
def myname(x,y):
    z1=sin(x)*cos(y)
    z2=tan(x)*sin(y)
    z=[z1,z2]
    return z
#    return z1,z2
#we can store both values in list
#below is calling main function
x=1
y=2
z=myname(x,y)
print('z1=%.2f z2=%.2f' %(z[0],z[1]))

def exponent(x,y):
    z=y**x
    return z
x=5
y=6
z=exponent(x,y)
print('Answer is : %.2f' %(z))