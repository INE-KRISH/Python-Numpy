# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:52:15 2021

@author: Admin
"""


import numpy 
arr =numpy.zeros([10],dtype=numpy.int64)

for i in range(0,5):
    arr[i]= int(input('Enter data:'))
print(arr)

n=int(input('enter your range'))
for i in range(0,n):
     if arr[i]%2 == 1:
     
         arr[5]=arr[5]+1
         
         
         arr[6]=arr[6]+arr[i]
         
          
     if arr[i]%2 == 0:
         
         arr[7]=arr[7]+1
         
         
         arr[8]=arr[8]+arr[i]
         
  
         arr[9]=arr[6]+arr[8]
    
print(arr)