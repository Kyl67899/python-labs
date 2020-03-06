#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:00:32 2020

@author: parsotak
"""

## Using pandas to read data with date time and float 

import pandas as pd
import numpy as np
import datetime
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt

#Importing files

infile = '/home/students/parsotak/wx272/wxstem.ex2.csv'

#reading in csv txt files

wxdata = pd.read_csv(infile, delimiter = ',')

## print data mean for thermometer

print(wxdata['Thermometer'].mean())

## Convert date/time data in the timestamp column from 
#string to datetime objects

wxdata['Timestamp'] = pd.to_datetime(wxdata['Timestamp'],
      format = '%Y-%m-%d %H:%M:%S')

#4 5 20

#define a figure

fig = plt.figure(figsize=(8,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Plot temps data as functions of time

ax.plot(wxdata['Timestamp'],wxdata['Thermometer'],color='r',label = 'Temperature')

#Plot the axis label

ax.set_xlabel('Date/time (Local)', fontsize = 14, fontweight= 'bold')

ax.set_ylabel('Temperature (F)', fontsize = 12)

#Define the date format for the x-axis

dFmt = mdates.DateFormatter('%m/%d/%y')

ax.xaxis.set_major_formatter(dFmt)

#Specify that the date/time should be printed once every 5 days

majlocs = mdates.DayLocator(interval = 5)

ax.xaxis.set_major_locator(majlocs)

ax.grid()

ax.legend()

                                                                  #.min would work too

ax.set_title('Wxstem Temperature data from ' + str(wxdata['Timestamp'][0]) + ' to ' + str(wxdata['Timestamp'].max()))


plt.show()