 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:05:36 2020

@author: parsotak
"""
## 1 and 2

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as

height = range(0,11001,100)

P = []

T = []

D = []

for H in height:
    
    print(H)

def HeighttoT(H):
    
    T = 288 - (0.0065 * H) 
    
    return T

def HeighttoP(height, T):
    
    P1 = 101325 * (np.e**((-9.8 * height) / (287 * T)))
    
    return P1

def PtoT(Pressure, Temps ):
    
    D = (Pressure / (287 * Temps))
    
    return D

## appending temps, height and desnities from the function 
    
for H in height:
    
    Temps = HeighttoT(H)
    
    T.append(HeighttoT(H))
    
    Pressure = HeighttoP(H,Temps)
    
    P.append(Pressure/100)
    
    density = PtoT(Pressure, Temps)
    
    D.append(density)
    
    
plt.plot(D, P, color= "green", linewidth=4)
plt.xlabel("Density (kg m$(-3)$)")
plt.ylabel("Pressure (mb)")
plt.title("Standard Atmospheric density vs pressure")
plt.ylim(ymin=1050)
plt.ylim(ymax=200)
plt.xlim(xmin=0.2)
plt.xlim(xmax=1.3)
plt.yscale('log')
plt.gca().yaxis.set_minor_formattermticker.ScalarFormatter()
plt.gca().yaxis.set_minor_formatter().set_scientific(False)
plt.gca().yaxis.set_minor_formatter().set_useOffset(False)
plt.gca().yaxis.set_major_formatter(mticker.Scalar)
plt.gca().yaxis.set_major_formatter
plt.gca().yaxis.set_major_formatter
plt.grid(which='both')
plt.savefig("parsotak_lab2_density.png")
plt.close()
