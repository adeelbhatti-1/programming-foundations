# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:41:28 2022

@author: Adeel
"""
import matplotlib.pyplot as plt
import numpy as np
n=9
x=[0,1,2,3,4,5,6,7,8,9]
x[1]=np.array([20,10,30,5])
x[2]=np.array([21,12,33,14])
x[3]=np.array([15,25,13,34])
x[4]=np.array([15,29,13,40])
x[5]=np.array([20,10,30,5])
x[6]=np.array([21,12,33,14])
x[7]=np.array([15,25,13,34])
x[8]=np.array([15,29,13,40])
x[9]=np.array([15,29,13,40])
i=1
while i<=n:
    plt.subplot(3,3,i)
    plt.scatter(x[i])
    i=i+1
plt.show()