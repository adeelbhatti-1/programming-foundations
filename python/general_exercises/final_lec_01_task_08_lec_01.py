# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:54:20 2022

@author: Adeel
"""

import matplotlib.pyplot as plt
import numpy as np
def f(q):
    return q**2
df=np.array([])
N=10
x=np.linspace(0,N,N+1)
y=3*x**2
h=x[1]-x[0]
df=(f(y[1:N])-f(y[0:N-1]))/h
#Dn=(f(x+h)-f(x))/h
plt.plot(x[0:9],f(x[0:9]),'-g')
plt.plot(x[0:9],2*x[0:9],'-b')
plt.plot(x,df,'-r')
plt.ylabel('seq term')
print(df)