# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:54:52 2022
@author: Adeel
"""
temp= dict(Rajab=12 , Khairpur=788, dist=4)
temp #prints dict in console manager or previewer
type(temp)
temp= {'Rajab':12,'Khairpur':777}
#temp['Rajab'] in console section
tem= dict(Raja=0)
temps={'Sukkur':22,'Larkana':29,'Karachi':31}
#for city in temps:
#    print('city = %s,temp = %g ' %(city,temps[city]))
for i in temps:
    print('city = %s,temp = %g ' %(i,temps[i]))
A={'Ahmed':77,'Ali':88}
for j in A:
    print('Name %s = %.2f' %(j,A[j]))