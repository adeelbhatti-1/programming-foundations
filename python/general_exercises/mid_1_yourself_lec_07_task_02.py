# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 08:19:37 2022

@author: Student
"""

import numpy as np
x=np.array([1,2,3,4,5,6])

print(x)
type(x)         # np.type(x)   np.shape(x)
x=[1,2,3,4,5]   # we can contain alist in a array , and find shape , length of list
arr=np.array(x) 
y=np.array([[1,2],[3,1]])
np.shape(y)
#z=np.array([[[1,3],[2,3],[1,2]],[[3,3],[3,3],[1,2]],[[2,3],[3,3],[1,2]]])
#u=np.array([[[[1,2],[1,2]],[1,2],[1,2]],[[[1,2],[1,2]],[1,2],[1,2]]]
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])           
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,1:4])