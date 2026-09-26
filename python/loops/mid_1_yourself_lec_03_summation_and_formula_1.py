# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:25:06 2022

@author: Student
"""
from math import exp
n=1
N=1000
add=0.
#for n in range(1,N+1):
while(n<=N-1):
    add=add+(1/n**2)*exp(-n)
    n=n+1
print(n, " ",add)