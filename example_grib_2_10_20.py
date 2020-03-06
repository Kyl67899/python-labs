#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:02:51 2020

@author: parsotak
"""

import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

#Define input file

infile = '/wx/storage/halpea17/wx272/20170909_erai.nc'

#Read in the file

f = Dataset(infile, 'r')

#read in mslp data (3D : time, lat, lon.)

mslp = f['PRMSL_GDS0_SFC'][:]

#3-D array 

mslp00 = mslp[0, :, :]

print(mslp00.shape)

#Read in lat. and long. and printing it

lats = f['g0_lat_1'][:]

lons = f['g0_lon_2'][:]

print(lats.shape)

print(lons.shape)

#from 1D to 2D to plot to a map

lon2d, lat2d = np.meshgrid(lons, lats)

#Define a figure

fig = plt.figure(figsize = (12,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Define basemap

m = Basemap(llcrnrlon = 240., llcrnrlat = 5., urcrnrlon = 350., urcrnrlat = 55., resolution = 'l', projection = 'merc', ax = ax)

xi, yi = m(lon2d, lat2d)

m.drawcoastlines()

m.drawstates()

m.drawcountries()

m.drawparallels(np.arange(-80., 81, 10.), labels = [1, 0, 0, 0], fontsize = 12)

m.drawmeridians(np.arange(0., 359., 20.), labels = [0, 0 ,0, 1], fontsize = 14)

#Define range of MSLP values to be printed

clevs = np.arange(960, 1041, 4)

#Add contour tick marks

cticks = np.arange(960, 1041, 8)

#Define MSLP values as a color filler

mslpfill = m.contourf(xi, yi, mslp00, clevs, cmap = 'rainbow')

#Add a color bar

cbar = plt.colorbar(mslpfill, orientation = 'horizontal', pad = 0.05, shrink = 0.75, ax = ax, ticks = cticks)

#increase size of labels 

cbar.ax.tick_params(labelsize = 14)

cbar.set_label('MSLP (mb)', fontsize =  14)

mslplines = m.contour(xi, yi, mslp00, clevs, colors = 'k')

mslplab = plt.clabel(mslplines, clevs, inline = True, fontsize = 12, fmt = '%1.0f')

# add a title 

ax.set_title('Test plot of MSLP (mb) from netCDF file')

plt.show()