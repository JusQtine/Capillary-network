#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:02:24 2025

@author: justine
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#file_path = r'C:\Volumes\Expansion\Reseau\Manips\x15_03_07_2\Position_front_388_411_droite.csv'


#df = pd.read_csv(file_path)


#print(df)


pos_front = np.array([246.062,211.000,189.062,171.000,155.000,141.125,128.125,115.188,105.062,93.250,84.062,74.062,67.000])
frame = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])

pos_front = -pos_front + np.ones(np.shape(pos_front))*246


plt.figure()
plt.plot(frame,pos_front)
plt.show()



# Définir la fonction pour le fit en racine carrée : y = a * sqrt(x) + b
def sqrt_fit(x, a, b):
    return a * np.sqrt(x) + b

# Effectuer l'ajustement des données
params, covariance = curve_fit(sqrt_fit,frame ,pos_front )

# Extraire les paramètres ajustés
a, b = params
print(f"Paramètres ajustés : a = {a}, b = {b}")

# Tracer les données
plt.scatter(frame, pos_front, label="Données", color='b', marker='o')

# Tracer la courbe ajustée (fit) en racine carrée
pos_front_fit = np.linspace(min(pos_front), max(pos_front), 100)  # Créer des valeurs de x pour le fit
y_fit = sqrt_fit(pos_front_fit, *params)  # Calculer les valeurs y correspondantes
plt.plot(pos_front_fit, y_fit, label="Fit en racine carrée", color='r', linestyle='--')

# Ajouter des labels et un titre
plt.title("Position Y vs Position X avec Fit en Racine Carrée")
plt.xlabel("Position X")
plt.ylabel("Position Y")
plt.legend()

# Afficher le graphique
plt.show()