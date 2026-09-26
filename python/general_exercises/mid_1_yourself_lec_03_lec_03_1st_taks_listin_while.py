# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:20:03 2022

@author: Student
"""
#Step 01 Initialization
dl=0.1 #interval
li=0 #initial limit
lf=5 #ending limit
N=int((lf-li)/dl) #total iterations
#initialization
i=0 
j=0
s=0
l=[] #creating an empty list

#Step 02 : Generator the number of the list
while(i<=N):
    s=s+dl
    l.append(s)
    i=i+1
    #print(s)
#print('%.2f',l)

#Step 03 : Printing
for i in range(N):
    print('list[%.d]=%.2f' %(i,l[i]))