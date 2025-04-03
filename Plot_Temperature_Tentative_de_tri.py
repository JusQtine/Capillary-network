#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:00:24 2025

@author: justine
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# Spécifie le chemin du fichier CSV
file_path = '/Volumes/Expansion/Reseau/ThermosensorsDatas/25_03_07_2_Thermosensors1.csv'

# Charge le fichier en utilisant le séparateur ';'
df = pd.read_csv(file_path, sep=';')

# Affiche les premières lignes du DataFrame pour vérifier que tout est bien chargé
print(df.head())



import matplotlib.pyplot as plt
import pandas as pd

#df le DataFrame

# Créer une nouvelle figure
plt.figure()

# Tracer chaque colonne séparément
plt.plot(df.iloc[:, 1], '.', label='Device 1')
#plt.plot(df.iloc[:, 2], '.', label='Device 2')
#plt.plot(df.iloc[:, 3], '.', label='Device 3')
#plt.plot(df.iloc[:, 4], '.', label='Device 4')
#plt.plot(df.iloc[:, 5], '.', label='Device 5')

# Ajouter des labels et une légende
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('Thermo captors 1 to 5')

# Afficher le graphique
plt.show()

