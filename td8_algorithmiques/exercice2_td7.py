import os
from mon_module import lire_valeurs

# spécifier le répertoire de travail si nécessaire
os.chdir("C:/... votre dossier...")

# demander le nom du fichier à l'utilisateur
nom_fichier = input("Nom du fichier : ")

# lire les valeurs du fichier
valeurs = lire_valeurs(nom_fichier)

# afficher les valeurs
print("Les valeurs sont :", valeurs)

# calculer et afficher la moyenne
moyenne = sum(valeurs) / len(valeurs)
print("La moyenne est :", moyenne)
