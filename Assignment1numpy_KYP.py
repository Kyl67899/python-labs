#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:25 2020

@author: parsotak
"""


#a = np.random.randint(100, size=(5,5))

#multiply each element by 2

#a*2

#add 40 to each element

#a+40

#Add 50 to each element in the first column

#a[:,0]+50

#Take the mean of all elements in the array

#np.mean(a)

#Take the mean of all elements in the column index 1

#np.mean(a[:, 1])

#Take the mean of all the elements in row index 4

#print(np.mean(a[4, :]))

#Find the mean of each column

#np.mean(a,axis=0)

#Find the mean of each row

#np.mean(a,axis=1)

import numpy as np

b = np.random.randint(20, size=(3,3))

print("Array :", (b))

#A the entire array

print("array max :", np.max(b))

print("array min :", np.min(b))

print("array median :", np.median(b))

#B row index 2

print("Row in index2 max:", np.max(b[:, 2]))

print("Row in index 2 min:", np.min(b[:, 2]))

print("Row in index 2 median:", np.median(b[:, 2]))

#C column index 0

print("Column index 0 max :", np.max(b,axis=0))

print("Column index 0 min :", np.min(b,axis=0))

print("Column index 0 median :", np.median(b,axis=0))


#D for each row

print("For each row Max :", np.max(a,axis=1))

print("For each row min :", np.min(a,axis=1))

print("For each row median :", np.median(a,axis=1))
