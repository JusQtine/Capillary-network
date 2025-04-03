#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 00:25:34 2025

@author: justine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 23:17:34 2025

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
            plt.plot(contour[:, 0], contour[:, 1], label=f'Contour {i+1}', linewidth=2)
    
    plt.title('Contours détectés (Eau vs Air)')
    plt.xlabel('Pixels X')
    plt.xlim(80,120)
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


