
import cv2
import os
import matplotlib.pyplot as plt

# Fonction pour charger toutes les images d'un répertoire
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

# Fonction pour afficher les images une par une
def display_images(images):
    for i, img in enumerate(images):
        # Convertir l'image BGR en RGB pour qu'elle soit affichée correctement avec matplotlib
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Afficher l'image
        plt.imshow(img_rgb)
        plt.title(f"Image {i+1}")
        plt.axis('off')  # Ne pas afficher les axes
        plt.show()

# Répertoire contenant vos images
folder = "/Volumes/Expansion/Reseau/Manips/25_03_07_2/zoom_droit" # Remplacez par le chemin de votre dossier d'images

# Charger les images
images = load_images_from_folder(folder)

# Afficher les images
display_images(images)


#%%

import cv2
import os
import matplotlib.pyplot as plt

# Fonction pour charger toutes les images d'un répertoire
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        # Vérifier si le fichier est une image JPEG
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
    return images

# Fonction pour afficher l'image originale et ses canaux HSV
def display_hsv_channels(images):
    for i, image in enumerate(images):
        # Convertir l'image en espace de couleur HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Séparer les canaux H (Teinte), S (Saturation) et V (Valeur)
        hue, saturation, value = cv2.split(hsv_image)

        # Afficher l'image originale et les composants H, S, V
        plt.figure(figsize=(12, 8))

        # Afficher l'image originale
        plt.subplot(2, 2, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f"Image originale {i+1}")
        plt.axis('off')

        # Afficher le canal Hue (Teinte)
        plt.subplot(2, 2, 2)
        plt.imshow(hue, cmap='hsv')
        plt.title(f"Canal Hue (Teinte) {i+1}")
        plt.axis('off')

        # Afficher le canal Saturation
        plt.subplot(2, 2, 3)
        plt.imshow(saturation, cmap='gray')
        plt.title(f"Canal Saturation {i+1}")
        plt.axis('off')

        # Afficher le canal Value (Valeur)
        plt.subplot(2, 2, 4)
        plt.imshow(value, cmap='gray')
        plt.title(f"Canal Value {i+1}")
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
    # Afficher les canaux HSV pour chaque image
    display_hsv_channels(images)

#%%




