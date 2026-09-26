# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:44:19 2022

@author: Adeel
"""
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    #y=x*(np.pi/180)
    return x**4
n=40
x=np.arange(-n,n+1,1)
seq=f(x)
plt.plot(x,seq,'-')
plt.show()