# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = [2,4,6,8,10]

print(a[1:4])

for i in range(2,273,2):
    if i != 136:
        print(i)
        

list1 = range(1,273)

list2 = []

for i in list1:
    if i % 3 == 0:
        list2.append(i)


def TF_to_TC(TF):
    TC = (TF-32) / 1.8
    return TC