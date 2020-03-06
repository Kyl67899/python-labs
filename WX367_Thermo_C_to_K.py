#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:40:21 2020

@author: parsotak
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

tempsC = range(-40,101)
tempsK = []

def TCtoTK(TK):
    TK = 273.15 + tempsC
    return TK

for i in tempsC:
    
    tempsK.append(TCtoTK(i))
    
plt.plot(tempsC,tempsK, color= "red", linewidth=3)
plt.xlabel("Temperature (C)")
plt.ylabel("Temperature (K)")
plt.title("Temps in C vs K")
plt.ylim(ymin=-40)
plt.xlim(xmax=100)
plt.grid()
plt.savefig("WX367_Thermo_plot_C_to_K")
plt.close()