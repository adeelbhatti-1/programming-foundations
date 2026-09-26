# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:23:50 2022

@author: Adeel
Name : Adeel Bhatti
CMS ID: 143-21-0006
"""
#Qno.12
import numpy as np
A=np.zeros((50,50)) #taking a 50x50 matrix
A[1:49,1:49]=1  #making all entries 1 leaving first row and coloumn and last row and coloumn
A[2:48,2:48]=0  #making all entries 0 leaving from 1st to 3rd row and coloumn and last to 3rd last row and coloumn   
print(A)