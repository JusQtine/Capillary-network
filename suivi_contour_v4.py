#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:26:02 2025

@author: justine
"""


import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

# Fonction pour charger toutes les images d'un répertoire
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
    return images

# Fonction pour extraire le canal vert, appliquer un seuil et détecter les contours
def detect_water_air_boundary(images):
    all_contours = []  # Liste pour stocker les contours de toutes les images
    
    for i, image in enumerate(images):
        # Extraire les canaux B, G, R de l'image
        (b, g, r) = cv2.split(image)
        
        # Appliquer un seuil pour identifier les zones d'eau par le canal vert
        _, thresh = cv2.threshold(g, 120, 255, cv2.THRESH_BINARY)
        
        # Appliquer un flou pour réduire le bruit (facultatif)
        blurred = cv2.GaussianBlur(thresh, (5, 5), 0)
        
        # Détecter les contours de l'eau
        contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Enregistrer les contours dans la liste
        all_contours.append(contours)

    # Retourner tous les contours détectés
    return all_contours

# Fonction pour afficher les contours dans une figure vide
def plot_contours(all_contours):
    plt.figure(figsize=(8, 8))
    
    for i, contours in enumerate(all_contours):
        for contour in contours:
            # Dessiner chaque contour
            contour = contour.squeeze()  # S'assurer que c'est un tableau 2D
            plt.plot(contour[:, 0], contour[:, 1],marker = '.', label=f'Contour {i+1}')
    
    plt.title('Contours détectés (Eau vs Air)')
    plt.xlabel('Pixels X')
    plt.xlim()
    plt.ylabel('Pixels Y')
    plt.gca().invert_yaxis()  # Inverser l'axe Y pour correspondre aux coordonnées de l'image
    plt.legend(loc='best')
    plt.show()
    



# Répertoire contenant vos images
folder = "/Volumes/Expansion/Reseau/Manips/25_03_07_2/zoom_droit"

# Charger les images depuis le dossier
images = load_images_from_folder(folder)

# Vérifier si des images ont été chargées
if len(images) == 0:
    print("Aucune image trouvée dans le répertoire spécifié.")
else:
    # Détecter les contours de la zone d'eau et de l'air pour chaque image
    contours_list = detect_water_air_boundary(images)
    
    # Afficher les contours dans une figure vide
    plot_contours(contours_list)


#%%
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour comparer le premier tableau avec le deuxième tableau du premier tuple
def compare_first_tuple(contours_list):
    # Prendre le premier tuple dans contours_list
    first_tuple = contours_list[0][0]

    # Récupérer le premier et le deuxième tableau de contours
    array_0 = first_tuple[0][0]
    array_1 = first_tuple[1][0]
    diff = array_0 - array_1
    diffx = diff[0]
    diffy = diff[1]

    # Tableau pour stocker les différences
    difference = []
    differencex = []
    differencey = []
    
    difference.append(diff)
    differencex.append(diffx)
    differencey.append(diffy)
    
    for i in range(0, np.shape(contours_list[0])[1] - 1):
        diff = contours_list[0][0][i][0] - contours_list[0][0][i + 1][0]
        
        difference.append(diff)
        differencex.append(diff[0])
        differencey.append(diff[1])
        
    # Retourner les différences pour une utilisation ultérieure
    return (difference, differencex, differencey)

# Appel de la fonction
difference = compare_first_tuple(contours_list)

#%%

#Plot seulement l'interface gauche de la première frame


# Extraire les coordonnées X et Y pour chaque contour
x = contours_list[0][0][:, 0, 0]  # Les coordonnées x
y = contours_list[0][0][:, 0, 1]  # Les coordonnées y

plt.figure(figsize=(15,15))
plt.axis('equal')  # Assurer que l'échelle des axes soit égale

# Tracer les points pour chaque contour
plt.plot(x, y, label=f'Contour 1')  # Tracer le contour, avec un label

# Ajouter des numéros et les coordonnées (x, y) aux points
for j in range(len(x)):
    # Déplacer le texte légèrement pour éviter le chevauchement
    offset_x = 0.02  # Décalage en x
    offset_y = 0.02  # Décalage en y
    if j % 2 == 0:
        offset_x = -0.02  # Décalage inverse pour les points pairs (afin d'éviter le chevauchement des textes)
        offset_y = -0.02  # Décalage inverse pour les points pairs
        
    # Placer les coordonnées et les numéros des points
    plt.text(x[j] + offset_x, y[j] + offset_y, f'{j+1}\n({x[j]:.2f}, {y[j]:.2f})', fontsize=8, ha='center', color='red')

# Ajouter des labels et un titre
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

