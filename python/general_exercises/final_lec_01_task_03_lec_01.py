# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:57:49 2022

@author: Adeel
"""
import numpy as np
N=9
import matplotlib.pyplot as plt
n=np.linspace(1,N,N)
seqn=(7+1/n)/(3-1/n**2)
plt.scatter(n,seqn)
print(np.sum(seqn))