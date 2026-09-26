# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:21:23 2022

@author: Adeel
Very Important Sir pointed towards it
"""
import numpy as np
import matplotlib.pyplot as plt
#x = np.array([0, 1, 2, 3])
#y = np.array([10, 40, 15, 30])

#plt.scatter(x,y)
#plt.show()


#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
#colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
color=np.array({10,20,30,40,50,60,70,80,90,100,95,85,75})
plt.scatter(x, y, c=color,cmap='viridis')
plt.show()