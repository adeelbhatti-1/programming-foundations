# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:12:21 2022

@author: Adeel
"""

import numpy as np
N=10
import matplotlib.pyplot as plt
n=np.linspace(1,N,N)
seqn=(np.sin(2**-n))/(2**-n)
plt.plot(n,seqn,'-o')  #- , -o , : , s , > , < , d , ^ , are all linestyles with which we can plot
print(np.sum(seqn))   # matplotlab to see all the sympbols to use the raph