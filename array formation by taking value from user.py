# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 07:20:18 2021

@author: Admin
"""

import numpy as np
y=int(input('enter length of array :- '))
ar = np.zeros ([y], dtype=np.int64)
s=0
for i in range(0,y):
    ar[i]=int(input('enter your data:'))
    s=s+ar[i]

print(ar)
print('sum of elements of the array:',s)