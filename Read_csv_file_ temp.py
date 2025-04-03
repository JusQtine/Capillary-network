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
tab_temp = pd.read_csv(file_path, sep=';')

# Affiche les premières lignes du DataFrame pour vérifier que tout est bien chargé
print(tab_temp.head())

