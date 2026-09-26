# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:31:36 2022

@author: Adeel
"""
import numpy as np
inc=np.array([ 5000 , 15000 , 10000 , 22000 , 38000 , 50000 , 30000 ])
if( np.any(inc) <= 10000 ):
    tax=0.1*inc
elif( np.any(inc) > 10000 & np.any(inc) <= 20000 ):
    tax= 1000 + 0.2*( inc - 10000 )
elif(np.any(inc) > 20000 & np.any(inc) <= 40000):
    tax=3000+0.3*( inc - 20000 )
else:
    tax=9000+0.5*(inc-40000)
print(tax)