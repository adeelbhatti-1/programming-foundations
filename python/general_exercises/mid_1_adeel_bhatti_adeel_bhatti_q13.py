# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:26:50 2022

@author: Adeel
Name: Adeel Bhatti
CMS ID: 143-21-0006
"""
#Q.No.13
import numpy as np
A=np.zeros((50,50))
A=A.reshape(1,2500)  #making it a single dimensional matrix in which there is a single row with all entries
A[0][102:2398:51]=-0.5  #making it's 51st entry -0.5 leaving frist and last two rows and coloumns
A[0][147:2353:49]=-0.5  #making it's 49th entry -0.5 leaving first and last two rows and coloumns
A=A.reshape(50,50)  #making it again a 50x50 matrix
print(A)