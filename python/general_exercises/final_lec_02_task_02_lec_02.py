# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:31:37 2022

@author: Adeel
"""
temps={'Sukkur':22,'Larkana':29,'Karachi':31,'Dadu':22}
#for city in temps:
#    print('city = %s,temp = %g ' %(city,temps[city]))
#for i in temps:
#   print('city = %s,temp = %g ' %(i,temps[i]))
if 'Dadu' in temps:
    print(' Dadu= %g ' %(temps['Dadu']))
else:
    print('no temperature data found')
#'dadu' in temps True
#temps.keys()  temps.values()
A = sorted(temps)
print(A)
#del A deletes the entire dictionary