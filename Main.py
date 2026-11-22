# Parking Intelligent - Smart Parking

Projet DS - Application Python

## Fonctionnalité 1 - Détection de la voiture
- Ouvrir la caméra
- Capturer une image
- Détecter la présence d'une voiture
- Afficher un rectangle autour de la voiture

## Fonctionnalité 2 - Lecture de la plaque
- Localiser la plaque d'immatriculation
- Extraire la zone de la plaque
- Améliorer la qualité de l'image
- Utiliser un OCR pour lire les caractères

## Fonctionnalité 3 - Pointage automatique
Entrée : Lire plaque, vérifier si déjà enregistré, enregistrer date et heure d'entrée
Sortie : Lire plaque, rechercher dernier pointage, enregistrer sortie, calculer durée

## Interface
Tkinter - Tableau de bord, Caméras, Historique, Pointages, Rapports

## Technologies
Python, Tkinter, OpenCV, EasyOCR, SQLite

## Comment lancer
pip install opencv-python pillow easyocr
python main.py
