#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:58:08 2020

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

infile = '/home/students/parsotak/wx272/parsotak_lab3_data1.csv'

#reading in csv txt files

wxdata = np.loadtxt(infile, delimiter = "," , skiprows = 1)

#define a figure

fig = plt.figure(figsize=(8,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Plot temps data 
ax.plot(wxdata[:,0],wxdata[:,2],color='r',label = 'Temperature')

#Plot Dewpoint data 

ax.plot(wxdata[:,0],wxdata[:,1],color='g',label = 'Dewpoint')

#Plot the axis label x and y

ax.set_xlabel('Date/time (UNIX)', fontsize = 14, fontweight= 'bold')

ax.set_ylabel('[Dewpoint] Tempature (0^F)', fontsize = 12)

ax.grid()

ax.legend()

ax.set_title('WxStem temperature and dewpoint data', fontsize = 14, fontweight= 'bold')

plt.savefig("parsotak_lab3_unix.png")

plt.show()