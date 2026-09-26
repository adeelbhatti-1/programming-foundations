# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:31:10 2022

@author: Student
"""
n=6
arr=np.zeros((6,6))
#for i in range(n):
 #   for j in range(n):
  #     if i==j:
   #        arr[i,j]=1
    ##      x=y
A=arr.reshape(1,36)
print(A)
A[0][0:36:7]=np.array([1,1,1,1,1,1])
C=A.reshape((6,6))
print(C)