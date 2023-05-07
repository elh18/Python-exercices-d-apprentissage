import os
import mymodule

# Définir le répertoire de travail
os.chdir('/chemin/vers/le/dossier')

# Demander l'utilisateur veut utiliser quel fichier
file_name = input("Entrez le nom du fichier: ")

# Charger les valeurs depuis le fichier texte
values = mymodule.load_values(file_name)

# Construire les listes de valeurs
x_values, y_values = mymodule.build_lists(values)

# Afficher les listes de valeurs
print("Liste des valeurs de X:", x_values)
print("Liste des valeurs de Y:", y_values)

# Calculer la somme des produits croisés
sum_cross = mymodule.cross_products_sum(x_values, y_values)
print("Somme des produits croisées:", sum_cross)
