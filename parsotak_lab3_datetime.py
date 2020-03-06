#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:51:44 2020

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

infile = '/home/students/parsotak/wx272/scripts/parsotak_lab3_data2.csv'

#reading in csv txt files

wxdata = pd.read_csv(infile, delimiter = ',')

### Convert date/time data in the timestamp column from 
##string to datetime objects

wxdata['Timestamp'] = pd.to_datetime(wxdata['Timestamp'],
      format = '%Y-%m-%d %H:%M:%S')

#define a figure size

fig = plt.figure(figsize=(8,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Plot timestamp for temps., dewpoints, and barometer

ax.plot(wxdata['Timestamp'],wxdata['Thermometer'],color='r',label = 'Temperature')

ax.plot(wxdata['Timestamp'],wxdata['Dewpoint'],color='g',label = 'Dewpoint')

#Looked up how to plot the numbers for the pressure 
#correctly on the right side: https://stackoverflow.com/questions/11640243/pandas-plot-multiple-y-axes

ax2 = ax.twinx()

ax2.plot(wxdata['Timestamp'],wxdata['Barometer'],color='b',label = 'Pressure')

#Plot the x-, y- axis label

ax.set_xlabel('Date/time (Local)', fontsize = 14, fontweight= 'bold')

ax.set_ylabel('Temperature (F)', fontsize = 14, fontweight= 'bold')

#added a second y-axis for pressure ("Hg)
#Had to look up url: https://stackoverflow.com/questions/14762181/adding-a-y-axis-label-to-secondary-y-axis-in-matplotlib/14762601
#https://stackoverflow.com/questions/11640243/pandas-plot-multiple-y-axes

#ax.secondary_yaxis('right')

ax2.set_ylabel('Pressure (" Hg)', fontsize = 14, fontweight= 'bold')

#Define the date format for the x-axis

dFmt = mdates.DateFormatter('%m/%d/%y')

ax.xaxis.set_major_formatter(dFmt)

#Specify that the date/time should be printed once every 4 days

majlocs = mdates.DayLocator(interval = 4)

ax.xaxis.set_major_locator(majlocs)

#x and y line 

ax.grid()

#showing what line is what and the color
#Legend for temps. and dewpoint

fig.legend(loc = 'upper right', bbox_to_anchor(0.9,0.9))

#Legend for pressure

ax2.legend()

#Title of the graph

ax.set_title('WxStem Temperature data from ' + str(wxdata['Timestamp'][0]) + ' to ' + str(wxdata['Timestamp'].max()))

#save png

plt.savefig("parsotak_lab3_datetime.png")

#showing the graph

plt.show()