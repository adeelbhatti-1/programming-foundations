# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:51:55 2022

@author: Adeel
"""
import numpy as np
n=80
k=np.linspace(1,n,n)
seq=4*((-1)**(k+1))/(2*k-1)
b=np.sum(seq)
c=np.cumsum(seq)
print(b)
import matplotlib.pyplot as plt
plt.plot(k,np.cumsum(seq),'-')
plt.plot(k,seq,'-')
plt.ylabel('seq term')
plt.show()