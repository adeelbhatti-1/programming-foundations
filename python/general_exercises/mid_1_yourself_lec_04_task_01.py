# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 05:10:58 2022

@author: Student
"""
#Task to make a function that will take list and give out ordered pairs
l = [[2,3,4,5,3],[2.4,3.5,4.7,5.5,4]]
i=0
def newli(l):
    for j in range(len(l[0])):
        #for i in range(len(l)-1):
        print("[%0.1f, %0.1f]" %(l[i][j],l[i+1][j]) )
l = [[2,3,4,5,3],[2.4,3.5,4.7,5.5,4]] 
newli(l)
#for 3 lists
def newli(l):
    for j in range(len(l[0])):
        #for i in range(len(l)-1):
        print("[%0.1f, %0.1f %.1f] " %(l[0][j],l[1][j],l[2][j]) )
l = [[2,3,4,5],[2.4,3.5,4.7,5.5],[1,2,3,4]]
newli(l)