#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:57:41 2020

@author: parsotak
"""

import numpy as np

## filename

f = '/home/students/parsotak/wx272/data.csv'

wxdata1 = np.loadtxt(f, delimiter = ",", skiprows = 1)

## Print the max wind speed
windmax = np.max(wxdata1[:,1])

print(windmax)

#Find min pressure

mslpmin = np.min(wxdata1[:,2])

print(mslpmin)

## Average temps

avgTemp = np.mean(wxdata1[:,4])
    
print(avgTemp)
    
meddewpoint = np.median(wxdata1[:,3])
    
print(meddewpoint)
    
##write the output to a file
    
out = open('parsotak_ica2.txt', 'w')

out.write('Maximum wind speed: '+str(windmax)+'\nMinimum MSLP: '+str(mslpmin)+'\nAverage Tempature: '+str(avgTemp)+'\nMedian Dewpoint: '+str(meddewpoint)+'\n')
