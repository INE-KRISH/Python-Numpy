# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:29:31 2021

@author: Admin
"""

import numpy 
arr =numpy.zeros([10],dtype=numpy.int64)
for i in range(0,5):
    arr[i]= int(input('Enter data:'))
#print(arr)
n=int(input('enter range:'))
for i in range(0,n):
     if arr[i]%2 == 1:
     
         arr[5]=arr[5]+1
         print('no of odd number:',arr[5])
         
         arr[6]=arr[6]+arr[i]
         print('sum of odd number:',arr[6])
          
     if arr[i]%2 == 0:
         
         arr[7]=arr[7]+1
         print('no of even number:',arr[7])
         
         arr[8]=arr[8]+arr[i]
         print('sum of even number:',arr[8])
         
     arr[9]=arr[6]+arr[8]
     print('total:',arr[9])
    
print(arr)
     
     
         
     