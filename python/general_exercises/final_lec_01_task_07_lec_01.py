# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:30:51 2022

@author: Adeel
"""

import matplotlib.pyplot as plt
import numpy as np
def f(q):
    return q**4
N=10
x=np.linspace(0,N,N+2)
l=x-1
h=x-l
Dn=(f(x+h)-f(x))/h
plt.plot(x,f(x),'-g')
plt.plot(x,4*x**3,'-b')
plt.plot(x,Dn,'.r')
plt.ylabel('seq term')