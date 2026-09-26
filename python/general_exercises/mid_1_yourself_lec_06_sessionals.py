# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:09:17 2022

@author: Student
"""
N=5
n=5
a=0
b=0
dx=0.1
dy=0.1 #ctn@f2022
x=[]    
y=[]
h=[] #created another list for the rows 
k=[] #created another list for the rows
i=0
j=0
for i in range(0,N+1):
    for j in range(0,n):
        s=-i*dy
        h.append(s)
    y.append(h)
    h=[]
i=0
j=0
t=0
for i in range(0,n):
    for j in range(0,N):
        t=j*dx
        k.append(t)
    t=0
    x.append(k)
    k=[]
i=0
j=0
for i in range(0,N):
    for j in range(0,n):
        print(x[i])
for i in range(0,N):
    for j in range(0,n):
        print(y[i])