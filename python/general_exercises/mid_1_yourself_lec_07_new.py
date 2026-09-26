# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:29:35 2022

@author: Adeel
"""

A=np.zeros((6,6))
A=A.reshape(1,36)
A[0][0:36:7]=1
A[0][5:36:5]=1
A=A.reshape(6,6)
print(A)