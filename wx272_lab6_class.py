#import necessary modules
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#set input file
infile = '/wx/storage/halpea17/wx272/lab6/20151108_erai.nc'

#read netCDF data and assign to arrays
f      = Dataset(infile, 'r')
mslp   = f['PRMSL_GDS0_SFC'][2,:,:]
z      = f['HGT_GDS0_ISBL'][2,1,:,:] / 10
lats   = f['g0_lat_1'][:]
lons   = f['g0_lon_2'][:]

#create 2D lat/lon array from 1D lat/lon arrays in netCDF file
lon, lat = np.meshgrid(lons,lats)

#define figure; add axes
fig = plt.figure(figsize = (12,8))
ax  = fig.add_axes([0.1,0.1,0.8,0.8])

#define basemap; draw appropriate lines
m = Basemap(boundinglat = 25,lon_0 = 260,resolution = "l",projection = "npstere", ax = ax)
m.drawparallels(np.arange(-80.,81.,10.), labels = [1,0,0,0], fontsize = 12)
m.drawmeridians(np.arange(0.,359.,20.), labels = [0,0,0,1], fontsize = 12)
m.drawcoastlines()
m.drawstates()
m.drawcountries()

#convert lat/lon data to plot coordinates
xi, yi = m(lon,lat)

#plot 500 mb geopotential height data
#include colorbar
zlevs   = np.arange(486, 601, 6)
z500    = m.contourf(xi, yi, z, zlevs, cmap = 'rainbow')
cbar    = plt.colorbar(z500, orientation = 'vertical', pad = 0.05, shrink = 0.7, ax = ax, ticks = zlevs)
cbar.set_label('500 mb geopotential height (dam)',fontsize = 14)
cbar.ax.tick_params(labelsize = 12)

#plot MSLP data; label contour lines
clevs   = np.arange(960, 1040, 4)
cmslp   = m.contour(xi, yi, mslp, clevs, colors= 'k')
clab    = plt.clabel(cmslp, inline = True, fontsize = 12, fmt='%1.0f')

#add figure title
ax.set_title("500 mb geopotential height (dam) and MSLP (mb) on 2015-11-08 at 12Z",fontsize=14)

#save figure; close plot
plt.savefig('parsotak_wx272_lab6.png')
plt.show()