# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:39:23 2022

@author: Adeel
"""

import matplotlib.pyplot as plt
import numpy as np
'''
x = np.array(["A", "B", "C", "D"])
y = np.array([15,25,35,43,50,60,70,80])
x=np.random.normal(200,100,500)
plt.hist(x)
plt.show()
'''
x=np.array([25,35,10,30])
mylabels=["Ahmed","Ali","You","Me"]
myexplode=[0.2,0,0,0]
mycolours=['blue','green','yellow','k']
plt.pie(x,labels=mylabels,startangle=90,explode=myexplode,shadow= True,colors=mycolours)
plt.legend(title="Four Names")
plt.show()