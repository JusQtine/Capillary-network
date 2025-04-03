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
    for i, image in enumerate(images):
        # Extraire les canaux B, G, R de l'image
        (b, g, r) = cv2.split(image)
        
        # Appliquer un seuil pour identifier les zones d'eau par le canal vert
        # Vous pouvez ajuster cette valeur de seuil pour mieux capturer l'eau
        _, thresh = cv2.threshold(g, 120, 255, cv2.THRESH_BINARY)
        
        # Appliquer un flou pour réduire le bruit (facultatif)
        blurred = cv2.GaussianBlur(thresh, (5, 5), 0)
        
        # Détecter les contours de l'eau
        contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Créer une copie de l'image originale pour afficher les contours
        contour_image = image.copy()

        # Dessiner les contours sur l'image
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)

        # Afficher l'image originale et les contours de l'eau
        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f"Image originale {i+1}")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
        plt.title(f"Contours (Eau vs Air) {i+1}")
        plt.axis('off')

        plt.tight_layout()
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
    detect_water_air_boundary(images)
