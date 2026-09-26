# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 07:37:02 2022

@author: Student
"""

from math import sin , cos
l1=[]
l2=[]
l3=[]
n=10
i=0
d=0.1
for i in range(n+1):
    s=3+i*d
    l1.append(s)
for i in range(n+1):
    t=i*d
    l2.append(t)  
j=0
for j in range(n+1):
    h=sin(l2[j])*cos(l1[j])
    l3.append(h)
    h=0
k=0
for k in range(n+1):
    print('[sin(%.2f)*cos(%.2f) %.2f ]' %(l1[k],l2[k],l3[k]))