# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:35:23 2022

@author: Adeel
Name : Adeel Bhatti
CMS ID : 143-21-0006
"""
#Q!!:
import numpy as np
def matrixproduct(A,B): #defining a function in which two matrix are taken as input
    m=len(A)
    n=len(B[0])
    k=0
    C=[]
    l1=[]
    i=0
    j=0
    c=0
    if len(A[0])!=len(B):       #if multiplication is not possible then it willl print out incorrent input
        return "Incorrent Input"
    else:                       #if it is possible then process will continue
        for i in range(m):
            for j in range(n):
                while k<n:
                    c=c+A[i][k]*B[k][j] #here it follows the simple process of multiplication,
                    k=k+1   # a counter k is started
                k=0
                l1.append(c) # this is row for the resulting matrix
                c=0
            C.append(l1)    #row is added to the original matrix
            l1=[]       # row is made empty and again the elements are inserted
        return C
A=[[1,0,9],[1,6,3],[8,3,4]]
B=[[1,0,0],[0,1,0],[0,0,1]]
C=matrixproduct(A,B)
print(C)