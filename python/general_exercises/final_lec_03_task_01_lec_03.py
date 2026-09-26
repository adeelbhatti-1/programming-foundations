# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:03:13 2022

@author: Adeel
"""

#tips for quiz summation , numpy , vectorizaion , numpy , only using vectorization and coloun
#np.linspace(0,10,100) np.arange(0,10,0.1)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(3, 3, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(3, 3, 2)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 3)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 4)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 5)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 6)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 7)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 8)
plt.plot(x,y)

x=np.array([1,2,3,4])
y=np.array([11,13,15,17])
plt.subplot(3, 3, 9)
plt.plot(x,y)

plt.show()