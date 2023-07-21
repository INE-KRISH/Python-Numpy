# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:24:16 2021

@author: Admin
"""

#creation of a 2-d array size of array and element are entered by user at runtime.
import numpy as np
x=int(input('Enter number of rows:'))
y=int(input('enter number of columns:'))
td=np.zeros([x,y],dtype=np.int32)
print(td)
s=0
for r in range(x):
    for c in range(y):
        td[r,c]=int(input('enter data to added in the new array:'))
        s=s+td[r,c]
print(td)
print('sum of the entered array is:',s)