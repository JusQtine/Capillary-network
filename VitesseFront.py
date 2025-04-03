#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 15:11:40 2025

@author: justine
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


pos_front = np.array([246.062,211.000,189.062,171.000,155.000,141.125,128.125,115.188,105.062,93.250,84.062,74.062,67.000])*(2/130)
frame = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])*5
name = '25_03_27_2_droite_gel1'

#pos_front = np.array([212.000,190.083,158.083,139.167,124.917,112.083,101.083,90.083,81.167,72.083,63.083,54.167,48.000,40.000,33.000,27.167])*(2*130)
#frame = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])*5
#name = '25_03_27_1_droite_gel1'








pos_front = -pos_front + np.ones(np.shape(pos_front)) * pos_front[0]

"""
plt.figure()
plt.plot(frame, pos_front)
plt.title("Position Front vs Frame")
plt.xlabel("Tps (s)")
plt.ylabel("Position Front (mm)")
plt.show()
"""

# Définir la fonction pour le fit en racine carrée
def sqrt_fit(x, a, b):
    return a * np.sqrt(x) + b

# Limiter les données à celles où 'frame' est inférieur ou égal à 25
mask = frame <= 25
frame_limited = frame[mask]
pos_front_limited = pos_front[mask]

# Données limitées
params, covariance = curve_fit(sqrt_fit, frame_limited, pos_front_limited)

# Paramètres ajustés
a, b = params
print(f"Paramètres ajustés : a = {a}, b = {b}")


plt.scatter(frame, pos_front, label="Données", color='b', marker='o')


x_fit = np.linspace(min(frame_limited), 25, 100)  # Limiter l'intervalle d'ajustement à x = 25
y_fit = sqrt_fit(x_fit, *params)
plt.plot(x_fit, y_fit, label=f'Fit en racine carrée : y={round(a, 2)}t + {round(b, 2)}', color='r', linestyle='--')


plt.title(f'Position Front vs Frame avec Fit, {name}' )
plt.xlabel("Tps (s)")
plt.ylabel("Position Front (mm)")
plt.legend()


plt.show()
