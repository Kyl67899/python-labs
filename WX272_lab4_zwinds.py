#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:18:20 2020

@author: parsotak
"""

#import datasets

import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

#To display data file variables

#f.variables

#Define input file

infile = '/wx/storage/halpea17/wx272/lab4/20151107_erai.nc'

#Read in the file

f = Dataset(infile, 'r')

#read in geo height contours from meters to decameters

gpot = f['HGT_GDS0_ISBL'][0, 1, :, :] 

#convert geo heights mb to dams

gpot_h = gpot/10

#Read in the wind u

wind_u = f['U_GRD_GDS0_ISBL'][:]

wind_v = f['V_GRD_GDS0_ISBL'][:]

#Read in lat. and long.

lats = f['g0_lat_1'][:]

lons = f['g0_lon_2'][:]

print(lats.shape)

print(lons.shape)

#Read in wind u (x) and v (y)

wind_u = f['U_GRD_GDS0_ISBL'][0, 1, :, :]

wind_v = f['U_GRD_GDS0_ISBL'][0, 1, :, :]

#getting components for the winds for 2d plot

num = ((wind_u)**2 + (wind_v)**2)

num = np.sqrt(num)

# convert from m/s to knots

win_kts = num * 1.94384

#from 1D to 2D to plot to a map

lon2d, lat2d = np.meshgrid(lons, lats)

#Define a figure

fig = plt.figure(figsize = (12,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Define basemap

m = Basemap(projection = 'npstere', boundinglat = 20, lon_0 = 260, resolution = 'l')

xi, yi = m(lon2d, lat2d)

m.drawcoastlines()

m.drawstates()

m.drawcountries()

m.drawparallels(np.arange(-80., 81, 10.), labels = [1, 0, 0, 0], fontsize = 12)

m.drawmeridians(np.arange(0., 359., 20.), labels = [0, 0 ,0, 1], fontsize = 14)

#Define range of wind speed to be plotted

range_wind = np.arange(0, 150, 10)

#Define the range of Geopotenital heights values 

range_geop_H = np.arange(500, 610, 6)

#Add contour fills wind speed values

contour_windFill = m.contourf(xi, yi, win_kts, range_wind, cbar = 'blue')# changing the color for the contours to show is not working properly

#Add contour fills for geo heights values 500 mb

contour_heightFill = m.contour(xi, yi, gpot_h, range_geop_H, cbar = 'blue')# changing the color for the contours to show is not working properly

#Label geo height contour lines #error: index 18 is out of bounds for size 18

contour_labels = plt.clabel(contour_heightFill, inline = True, fontsize = 12, fmt = '%1.0f')

#Add colorbar for wind speed and tick marks

cbar = plt.colorbar(contour_windFill, orientation = 'vertical', ax = ax, ticks = range_wind)

#increase size of labels 

cbar.ax.tick_params(labelsize = 14)

cbar.set_label('Wind speed (kts)', fontsize =  14)

# add a title 

ax.set_title('500 mb geopotential height (dam) and wind speed (kt) from ERAI on 20151107 at 00Z', fontsize = 12)

#save png

plt.savefig("parsotak_lab4_zwinds.png")

plt.show()