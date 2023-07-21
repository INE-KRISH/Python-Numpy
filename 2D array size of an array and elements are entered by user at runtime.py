# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:52:54 2021

@author: admin
"""

#Creation of 2D array size of an array and elements are entered by user at runtime.
import numpy as np
x=int(input("Enter number of Rows : "))
y=int(input('Enter number of Columns : '))
td=np.zeros([x,y],dtype=np.int32)
print(td)
s=0
for r in range(x):
    for c in range(y):
        td[r,c]=int(input('Enter Data to be added in an array : '))
        s=s+td[r,c]
print(td)
print('Sum of the Entered elements of an array is : ',s)
#Slicing
print(td[0:1])
#print(td[:2,:3])
#print(td[:3,::2])
#print(td[::-1,::-1])
#print(td[:,0])
#print(td[0])
td1=np.zeros([x,y],dtype=np.int32)



#Transpose the Matrix
p=x-y
if p==0:
    for r in range(x): 
        for c in range(y):
            td1[r,c]=td[c,r]
    print('transpose is as followed:')
    print(td1)

else :
    print('transpose not possible')    


