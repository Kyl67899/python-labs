#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:03:27 2020

@author: parsotak
"""

#import data sets

import pygrib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

## print inventory

#grib.seek(0)
#for grb in grib:
#   print(grb)

#set input file

f = '/wx/storage/halpea17/wx272/lab5/gfs-data.grb2'

#open file

grib = pygrib.open(f)

#define grib objects/lines to be read in

uinfo = grib.select(name = 'U component of wind', level = 500)[0]

vinfo = grib.select(name = 'V component of wind', level = 500)[0]

gheight = grib.select(name = 'Geopotential Height', level = 500)[0]

#Create arrays with data

u = uinfo.values

v = vinfo.values

gpot = gheight.values/10

#Calculates wind speeds

wind = np.hypot(u,v)

lat, lon = uinfo.latlons()

#Define a figure

fig = plt.figure(figsize = (12,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Define basemap

m = Basemap(llcrnrlon = 240., llcrnrlat = 5., urcrnrlon = 350., urcrnrlat = 55., resolution = 'l', projection = 'merc', ax = ax)

m.drawparallels(np.arange(0.,81.,10), labels = [1,0,0,0], fontsize = 10, zorder = 12)

m.drawmeridians(np.arange(0.,351.,10), labels = [0,0,0,1], fontsize = 10, zorder = 12)

m.drawcoastlines()

m.drawstates()

m.drawcountries()

#convert from lat/lon to map plot coordinates

xi, yi = m(lon, lat)

#range for wind speeds

windint = np.arange(0,101,5)

#range for geo heights



# plot wind: add label a colorbar

windplot = m.contourf(xi, yi, wind, windint, cmap = 'Blues')

windcbar = plt.colorbar(windplot, orientation = 'horizontal', ax = ax, ticks = windint, shrink = 0.75, pad = 0.05)

windcbar.set_label('Wind speed m s$^{-1}$')

windcbar.ax.tick_params(labelsize = 12)

ax.set_title('Example plotting GRIB data: 500 mb wind speed (m/s)')

plt.show()

