#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:35:16 2020

@author: parsotak
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

height = range(0,11000,100)

pressure = []

def MtohPA(z):
    
    p1 = 1013.25 * (np.e**((-9.8 * z) / (287 * 252.4)))
    
    return p1

for i in height:
    
       pressure.append(MtohPA(i))
    
plt.plot(pressure, height, color= "blue", linewidth=4)
plt.xlabel("Pressure (hPa)")
plt.ylabel("Meter (M)")
plt.title("Pressure vs height")
plt.ylim(ymin=0)
plt.ylim(ymax=12000)
plt.xlim(xmin=200)
plt.xlim(xmax=1000)
plt.xscale('log')
plt.grid()
plt.savefig("parsotak_lab2_pvsz.png")
plt.close()

    