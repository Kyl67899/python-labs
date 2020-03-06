#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:08:43 2020

Re-create the thermo plots using matplotlib

@author: parsotak
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

tempsC = range(-40,101)
tempsF = []

def TCtoTF(TC):
    TF = 1.8 * TC + 32
    return TF

for i in tempsC:
    
    tempsF.append(TCtoTF(i))
    
plt.plot(tempsC,tempsF, color= "red", linewidth=3)
plt.xlabel("Temperature (C)")
plt.ylabel("Temperature (F)")
plt.title("Temps in C vs F")
plt.ylim(ymin=-40)
plt.xlim(xmax=100)
plt.grid()
plt.savefig("WX367_Thermo_plot")
plt.close()