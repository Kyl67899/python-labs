#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:20:39 2020

@author: parsotak
"""

import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
# Looked up how to do standar deviation : https://www.geeksforgeeks.org/python-statistics-stdev/
# Importing statistics module 
import statistics as stats 

#Define input file

infile = '/wx/storage/halpea17/wx272/20170909_erai.nc'

#Read in the file

f = Dataset(infile, 'r')

#read in geo height contours at 00z 1000-500mb

gpot_1000mb = f['HGT_GDS0_ISBL'][0, 3, :, :]

gpot_500mb = f['HGT_GDS0_ISBL'][0, 1, :, :]

#Read in lat. and long.

lats = f['g0_lat_1'][:]

lons = f['g0_lon_2'][:]

print(lats.shape)

print(lons.shape)

#Convert mb to dams

gpot_1000dams = gpot_1000mb/10

gpot_500dams = gpot_500mb/10

#getting the thickness of the two mb Convert mb to dams

thkns = (gpot_500mb - gpot_1000mb)/ 10 

#calculate the standard dev. for thickness

thkns = (gpot_500mb - gpot_1000mb)/ 10 

thkns_std = (540 - thkns)

#from 1D to 2D to plot to a map

lon2d, lat2d = np.meshgrid(lons, lats)

#Define a figure

fig = plt.figure(figsize = (12,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#contours is the same thing as from question two and basemap

#Define basemap 

m = Basemap(llcrnrlon = 200., llcrnrlat = 20., urcrnrlon = 320., urcrnrlat = 65., resolution = 'l', projection = 'merc', ax = ax)

xi, yi = m(lon2d, lat2d)

m.drawcoastlines()

m.drawstates()

m.drawcountries()

#lat are 20 N - 65 N every 10 ;lons are 160 W - 40 W every 20.

m.drawparallels(np.arange(-80., 81., 10.), labels = [1, 0, 0, 0], fontsize = 12)

m.drawmeridians(np.arange(0., 359., 20.), labels = [0, 0 ,0, 1], fontsize = 12)

#contours for the thickness

contour_thkns = m.contour(xi, yi, thkns, )

#contour thickness less than equal to 540 blue



#contour thickness greater than 540 red



#plot contours thickness dev

thnk_rang = np.arange(-48, 48, 6)

#Add colorbar for thickness dev from standard

cbar = plt.colorbar(contour_thkns, orientation = 'horizontal', pad = 0.05, shrink = 0.75, ax = ax, ticks = thnk_rang)

#increase size of labels 

cbar.ax.tick_params(labelsize = 14)

cbar.set_label('1000-500 mb thickness deviation from standard (dam)', fontsize = 14)

#add a title 

ax.set_title('1000-500 mb thickness (dam) and thinkness deviation from standard (dam) on 20151107 at 00Z', fontsize = 12)

#save png

plt.savefig("parsotak_lab4_thkndev.png")

plt.show()