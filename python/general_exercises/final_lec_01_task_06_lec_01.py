# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:19:32 2022

@author: Adeel
"""
import matplotlib.pyplot as plt
import numpy as np
def f(q):
    return np.sin(q)
def Dn(f,x,N):
    k=np.linspace(0,N,N+1)
#    k=k[:N]
    h=2**-k
    Dn=(f(x+h)-f(x))/h
    #plt.plot(k,D)
    #c=np.sum(D)
    return Dn,k
N=80
#x=np.pi
x=0
seqn,k=Dn(f,x,N)
plt.plot(k,seqn,'-')
plt.ylabel('seq term')
