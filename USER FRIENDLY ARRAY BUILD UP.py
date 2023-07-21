# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:06:05 2021

@author: Admin
"""

import numpy as np
l1=[500,400,300,200]
ar= np.array(l1)
n=len(l1)
print(ar)
x= int(input('enter a value to be replaced'))
for ind in range(0,n):
   ind= int(input('please enter your index'))
   break
ar[ind]=x
print(ar)