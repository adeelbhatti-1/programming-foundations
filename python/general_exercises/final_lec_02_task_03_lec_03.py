# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:44:01 2022

@author: Adeel
"""
import numpy as np
batchess = dict(Fall2021=22,Fall2022=29,Spring2021=16)
batches={'Fall 2021':np.zeros(5),'Fall 2022':[2,3,4,8],'Spring 2021':(4,5,6,3,14)}
#print(batchess)
#i=0
#for i in batches:
#    print(' Number of students in %s = %g ' %( i , batches[i] ))
#print(batchess.values())
#print(batchess.keys())
#we can use get command
print(batchess)
print(batches['Fall 2022'][1])
batches['Fall 2022'][1]=5
print(batches['Fall 2022'][1])
#batches.get('Fall2022')