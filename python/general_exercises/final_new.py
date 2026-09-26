# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:21:35 2022

@author: Adeel
"""

import numpy as np
n=np.arange(0,501,1)
an=np.cos(10*n)*(10+np.exp(n/20))/(1+10*np.exp(n/20))
a=np.sum(an)
print(an)
print(a)