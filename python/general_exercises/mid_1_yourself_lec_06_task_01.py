# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:35:33 2022

@author: Student
"""

def newtonmethod(a,b,eps,f):
    if f(a)*f(b)>0:
        print('error: function does not change sign')
        return
    i=0
    while(b-a)>eps:
        i=i+1
        m=(a+b)/2
        if f(a)*f(m)<=0:
            b=m
        else:
            a=m
        print('iteration %.d: [%.5f,%.5f]' %(i,a,b))
    print('the answer is : %.2f' %(m))
    return m
def f(x):
    return x**2+x-6
a=-3
b=4
eps=1e-5
newtonmethod(a,b,eps,f)