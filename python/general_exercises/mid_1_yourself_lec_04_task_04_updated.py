# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 07:18:26 2022

@author: Student
"""
#from math import log,e,sin,cos
#def L(x,n):
#    i=1
#    z=0
#    while(i<=n):
#        z=z+((1/i)*(x/(1+x))**i)
#        i=i+1;
#    return z;
#n=20
#x=1.2
##z=L(x,n)
#print('z=%.16f' %(z))
#exact = log(1+x)
#appro = L(x,n=1000)
#print('exact : ',exact)
#print('approximation : ',appro)

f1=lambda x:x**2+4
f2=lambda x,y:sin(y)*cos(x)
print(f1(3.1))
print(f2(0.1,2.3))