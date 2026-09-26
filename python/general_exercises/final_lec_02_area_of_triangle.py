# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:53:17 2022

@author: Adeel
"""
import numpy as np
from math import sqrt
#example 6.15
'''def distance(vert):
    s=0
    t=0
    u=0
    s=sqrt((vert.get(1)[0]-vert.get(2)[0])**2+(vert.get(1)[1]-vert(2)[1])**2)
    t=sqrt((vert.get(1)[0]-vert.get(3)[0])**2+(vert.get(1)[1]-vert(3)[1])**2)
    u=sqrt((vert.get(2)[0]-vert.get(3)[0])**2+(vert.get(2)[1]-vert(3)[1])**2)
    return s,t,u'''
vert={1:(5,0),2:(0,3),3:(1,0)}
A=0.5*(vert.get(1)[0]*(vert.get(2)[1]+vert.get(3)[1])+vert.get(2)[0]*(vert.get(3)[1] \
            +vert.get(1)[1])-vert.get(3)[0]*(vert.get(1)[1]-vert.get(2)[1]))
print(abs(A))
#s,t,u=distance(vert)
#print(s,t,u)

#example 6.16
A=np.zeros(101)
A[0]=-0.5
A[100]=2
K= {0 : -0.5,100 : 2}
x=1.05
s=0
i=0
k=0
for i in range(0,1005):
    if i in K:
        s=s+K[i]*x**i
    else:
        s=s
for i in range(len(A)):
    k=k+A[i]*x**i
print(k)