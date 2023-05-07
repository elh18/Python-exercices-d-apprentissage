import os

# Définir une fonction qui calcule la somme du produit croisé entre deux vecteurs
def calculer_produit_croise(X, Y):
    # Vérifier si les deux listes ont la même longueur
    if len(X) != len(Y):
        print("Les deux listes n'ont pas la même longueur.")
        return None
    
    # Initialiser la somme à zéro
    S = 0
    
    # Parcourir les deux listes et calculer le produit croisé
    for i in range(len(X)):
        S += X[i] * Y[i]
    
    return S

# Définir une fonction qui écrit deux listes dans un fichier séparées par ';'
def ecrire_fichier(nom_fichier, X, Y):
    # Ouvrir le fichier en mode écriture
    with open(nom_fichier, 'w') as f:
        # Écrire chaque paire de valeurs sur une ligne séparée par ';'
        for i in range(len(X)):
            f.write(f"{X[i]};{Y[i]}\n")
    
    print(f"Les vecteurs X et Y ont été enregistrés dans le fichier {nom_fichier}.")

# Demander à l'utilisateur le nombre d'éléments
n = int(input("Entrez le nombre d'éléments : "))

# Initialiser deux listes vides pour stocker les entrées de l'utilisateur
X = []
Y = []

# Boucle pour saisir les éléments des deux listes
for i in range(n):
    x = int(input(f"Entrez l'élément {i+1} de la liste X: "))
    y = int(input(f"Entrez l'élément {i+1} de la liste Y: "))
    X.append(x)
    Y.append(y)

# Afficher la somme du produit croisé
S = calculer_produit_croise(X, Y)
if S is not None:
    print(f"La somme du produit croisé entre les deux vecteurs est : {S}")

# Demander à l'utilisateur le nom du fichier où écrire les vecteurs
nom_fichier = input("Entrez le nom du fichier où enregistrer les vecteurs : ")

# Écrire les deux listes dans un fichier séparées par ';'
ecrire_fichier(nom_fichier, X, Y)
