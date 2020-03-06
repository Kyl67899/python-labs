#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:20:21 2020

@author: parsotak
"""
# import datasets
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

#Define input file

infile = '/wx/storage/halpea17/wx272/20170909_erai.nc'

#Read in the file

f = Dataset(infile, 'r')

#read in geo height contours at 00z 1000-500mb

gpot_1000mb = f['HGT_GDS0_ISBL'][2, 3, :, :]

gpot_500mb = f['HGT_GDS0_ISBL'][2, 3, :, :]

#Read in lat. and long.

lats = f['g0_lat_1'][:]

lons = f['g0_lon_2'][:]

print(lats.shape)

print(lons.shape)

#getting the thickness of the two mb Convert mb to dams

thkns = (gpot_500mb - gpot_1000mb)/ 10 

#Using the heights to find the temps. from 1000-500mb at 12z and convert to C

tempsK = (10 * thkns) / 29.3 * (np.log(1000/500))

tempsC = tempsK - 273.15

#calculate the average temp from 1000 mb to 500 mb

#temp_avg = np.mean()

#from 1D to 2D to plot to a map

lon2d, lat2d = np.meshgrid(lons, lats)

#Define a figure

fig = plt.figure(figsize = (12,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Define basemap 

m = Basemap(llcrnrlon = 200., llcrnrlat = 20., urcrnrlon = 320., urcrnrlat = 65., resolution = 'l', projection = 'merc', ax = ax)

xi, yi = m(lon2d, lat2d)

m.drawcoastlines()

m.drawstates()

m.drawcountries()

#lat are 20 N - 65 N every 10 ;lons are 160 W - 40 W every 20.

m.drawparallels(np.arange(-80., 81., 10.), labels = [1, 0, 0, 0], fontsize = 12)

m.drawmeridians(np.arange(0., 359., 20.), labels = [0, 0 ,0, 1], fontsize = 12)

#range of temps avg

range_tempsavg = np.arange(-30, 21, 5)

#range for the avg contour 

range_contour = np.arange(510, 601, 6)

#contours for temps

contour_temps1 = m.contourf(xi, yi, tempsC, range_tempsavg) # range_tempsavg is either not being read in and not being averaged 
#not printing contours 

#contours for the thinkness

contour_thkns = m.contour(xi, yi, thkns, range_contour)

#contour thinkness less than equal to 540 blue


#contour thinkness greater than 540 red

#Add colorbar for temps 

cbar = plt.colorbar(contour_temps1, orientation = 'horizontal', pad = 0.05, shrink = 0.75, ax = ax, ticks = range_tempsavg)

#plot contours from each range with the color to define the differences in thinkness levels


#increase size of labels 

cbar.ax.tick_params(labelsize = 14)

cbar.set_label('1000-500 mb average temperature ($^{o}$C)', fontsize = 14)

#add a title 

ax.set_title('1000-500 mb thickness (dam) and average temperature $^{o}$C on 20151107 at 00Z', fontsize = 12)

#save png

plt.savefig("parsotak_lab4_thkn.png")

plt.show()