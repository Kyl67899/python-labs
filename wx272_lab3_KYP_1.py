#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:29:02 2020

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

#reading in csv txt files and skipping row 1

wxdata = pd.read_csv(infile, delimiter = ',', skiprows = 1)

fig = plt.figure(figsize=(8,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])





