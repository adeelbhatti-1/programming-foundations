# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:50:09 2022
@author: Adeel
"""
# Fabnocci Number Sequence
import numpy as np
n=7
'''x=np.zeros(n)
x[1]=1
x[2]=1
x[3]=2
for i in range(1,n):
    if i > 3:
        x[i]=x[i-1]+x[i-2]
    else:
        x[i]=x[i]
    print('value of %d number = %d' %(i,x[i]))'''
#factorial
y=np.arange(1,n+1,1)
k=1
print(y)
for i in range(1,n):
    k=k*y[i]
    y[i]=k
    print('factorial of %.2f = %.2f' %(i+1,y[i]))