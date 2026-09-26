# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:45:06 2022

@author: Adeel
"""

import numpy as np
n=np.arange(4,101,1)
su=((-1)**(n+2)*(1-n))/(3*n-n**2)
a=np.sum(su)
print(a)