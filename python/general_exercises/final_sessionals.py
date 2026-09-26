"""
Created on Thu Dec  1 13:30:58 2022

@author: Adeel
"""
global n
n=900
import numpy as np
def verify():      # this is the verify function
    g=np.exp(4)-np.exp(0)
    return g
def f(x):           #the function whose integral we have to find
    return np.exp(x)
def csr(a,b,f):     #Composite Simpsons's Rule
    j1=np.arange(1,(n+1)/2-1,1)
    j2=np.arange(1,(n/2+1),1)
    h=(b-a)/n
    x1=a+2*j1*h
    x2=a+(2*j2-1)*h
    x1=np.sum(f(x1))
    x2=np.sum(f(x2))
    a=(h/3)*(f(a)+2*x1+4*x2+f(b))
    d=np.sum(a)
    return d
def ctr(a,b,f):     #Composite Trapzoidal Rule
    j=np.linspace(1,n-1,n-1)
    h=(b-a)/n
    x=a+j*h
    x=np.sum(f(x))
    c=(h/2)*(f(a)+2*x+f(b))
    d=np.sum(c)
    return d
def cmr(a,b,f):     #Composite Mid Point Rule
    j=np.arange(0,(n+1)/2,1)
    h=(b-a)/(n+2)
    x=a+(2*j+1)*h
    c=2*h*f(x)
    d=np.sum(c)
    return d
a=0
b=4
d=csr(a,b,f)        #Calling all three functions
y=ctr(a,b,f)
z=cmr(a,b,f)
print(d)        #printing them
print(y)
print(z)
print(verify())