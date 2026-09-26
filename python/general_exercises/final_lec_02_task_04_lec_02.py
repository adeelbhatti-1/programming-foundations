# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:12:09 2022

@author: Adeel
"""
import numpy as np
batchess = dict(Fall2021=22,Fall2022=29,Spring2021=16)
batches={'Fall 2021':np.zeros(5),'Fall 2022':[2,3,4,8],'Spring 2021':(4,5,6,3,14)}
# no two strings can have different values a string can only have a single value
#print(batches.get('Fall 2022'))
#A={0:2,1:5} # it is dictionary with a number assignment not a string
#print(A)
#type(A)
#print(batchess.items()) #returns in the form of tuples
batches['Fall 2021']=5
batches.update({'Fall 2022':20})
batches.popitem()
#batches.clear()
print(batches)
