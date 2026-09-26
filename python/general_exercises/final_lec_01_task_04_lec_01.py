# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:06:14 2022

@author: Adeel
"""
import numpy as np
N=99
import matplotlib.pyplot as plt
n=np.linspace(1,N,N)
seqn=(np.sin(2**-n))/(2**-n)
plt.plot(n,seqn)
c=np.cumsum(seqn)
print(np.sum(seqn))