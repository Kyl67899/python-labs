#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:01:50 2020

@author: parsotak
"""

#import data sets

import pygrib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#set input file

f = '/wx/storage/halpea17/wx272/lab5/gfs-data.grb2'

#open file

grib = pygrib.open(f)

#print inventories

#grib.seek(0)
#for grb in grib:
#   print(grb)

#read in mslp (mb) data contour #1

MSL_con1 = grib.select(name = 'Pressure reduced to MSL', level = 0)[0]

#convert from Pa to mb

MSL_con1_mb = MSL_con1.values / 100

#read in geo heights thickness from 1000-500 mb convert to dam contour #2

Geo_con2_500 = grib.select(name = 'Geopotential Height', level = 500)[0] 

Geo_con2_1000 = grib.select(name = 'Geopotential Height', level = 1000)[0]

#convert each height to mb from Pa

Geo_con2_500mb = Geo_con2_500.values / 10

Geo_con2_1000mb = Geo_con2_1000.values / 10

#thkn difference at pressure level

thkn_level = Geo_con2_500mb - Geo_con2_1000mb

#read in the total precps contourfill

totprecip_contf = grib.select(name = 'Total Precipitation', level = 0)[0]

#array for total precips (inches). contourfill

totprecip_cont = totprecip_contf.values / 25.4

#define lat and lon

lat, lon = MSL_con1.latlons()

#Define a figure

fig = plt.figure(figsize = (12,8))

ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Define basemap lat:  20 N - 52 N every 10; long: 130 W - 60 W merc project

m = Basemap(llcrnrlon = 230., llcrnrlat = 20., urcrnrlon = 300., urcrnrlat = 55., resolution = 'l', projection = 'merc', ax = ax)

m.drawparallels(np.arange(0.,81.,10), labels = [1,0,0,0], fontsize = 10, zorder = 12)

m.drawmeridians(np.arange(0.,351.,10), labels = [0,0,0,1], fontsize = 10, zorder = 12)

m.drawcoastlines()

m.drawstates()

m.drawcountries()

#convert from lat/lon to map plot coordinates

xi, yi = m(lon, lat)

#range for MSLP

mslp_Cont1 = np.arange(936, 1056, 4)

#range for thkn 1000 - 500 mb one for less than equal 

thkn_Contour = np.arange(474, 606, 6)

thkn_Contour2 = np.arange(546, 606, 6)

#contour #1 mslp range 936-1054 every 4 mb solid line gray inline labels size 10 whole numbers 

Contour_MSLP1 = m.contour(xi, yi, MSL_con1_mb, mslp_Cont1, cmap = 'Greys')

#MSLP contour labels

thknlab1 = plt.clabel(Contour_MSLP1, mslp_Cont1, inline = True, fontsize = 10, fmt = '%1.0f')

#contour #2 thinkness 1000 - 500 mb in dam range 474 - 606 every 6 dam dashed lines and have inline labels size 10 whole numbers

Contour_thkn500mb = m.contour(xi, yi, thkn_level, thkn_Contour, colors = 'Blue', linestyles = 'dashed')

Contour_thkn1000mb = m.contour(xi, yi, thkn_level, thkn_Contour2, colors = 'Red', linestyles = 'dashed')

#plotting the inline labels for each contour thkn level

thknlab = plt.clabel(Contour_thkn500mb, thkn_Contour, inline = True, fontsize = 10, fmt = '%1.0f')

thknlab1 = plt.clabel(Contour_thkn1000mb, thkn_Contour2, inline = True, fontsize = 10, fmt = '%1.0f')

# total precip ticks range

ttprecip = [0.01, 0.1, 0.25, 0.5, 0.75, 1]

#contourfill total precip inches interval = [0.01, 0.1, 0.25, 0.5, 0.75, 1] colormap = 'GuBu'

totprecipplot = m.contourf(xi, yi, totprecip_cont, ttprecip, cmap = 'GnBu')

#total precip colorbar

totprecipcbar = plt.colorbar(totprecipplot, orientation = 'horizontal', ax = ax, ticks = ttprecip, shrink = 0.75, pad = 0.05)

totprecipcbar.set_label('Total Precipitation (in.)')

totprecipcbar.ax.tick_params(labelsize = 12)

ax.set_title('MSLP (mb), 1000 - 500 mb thickness (dam), and Total precipitation (inches). Forecast valid 2020-02-18 at 06Z.')

plt.savefig("parsotak_lab5_MSLP_Geo-H_totprecip.png")

plt.show()