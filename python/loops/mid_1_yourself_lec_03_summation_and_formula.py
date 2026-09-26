# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:25:06 2022

@author: Student
"""
from math import exp
n=0
N=1000
add=0.
for n in range(1,N+1):
    add=add+(1/n**2)*exp(-n)
print(n, " ",add)