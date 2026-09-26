
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:21:58 2022

@author: Student
"""
from math import pi,sin
t=0.5
T=4*pi
n=1000
i=1
a=0
for i in range(1,n+1):
    a=a+(1/(2*i-1))*(sin(2*(2*i-1)*pi*t)/T)
print(a)
a = (4./pi)*a
#print('n=%d and a=%.6f' %(i,a))
print(a)
#answer 1.5                             