# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:09:19 2022

@author: Adeel
"""
import numpy as np
#def an(n):
#    series_sum=0
#    k=1
#    ((-1)**(k+1))/(2*k-1)
#    for k in range(1,n):
#        series_sum = series_sum +  ((-1)**(k+1))/(2*k-1)
#    return 4*series_sum
n=90
#print(an(n))
#a=np.array([1,2,3])
#np.sum(a)
k=np.linspace(1,n,n)
seq=((-1)**(k+1))/(2*k-1)
b=4*np.sum(seq)
print(b)
import matplotlib.pyplot as plt
plt.plot(k,seq,'-')
plt.plot(k,seq,'.')
plt.ylabel('seq term')
plt.show()
