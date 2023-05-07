import os

def product_vectors(x, y):
    """
    Calcul la somme du produit croisé de deux vecteurs x et y
    
    Args:
    x -- une liste de valeurs numériques
    y -- une liste de valeurs numériques
    
    Returns:
    La somme du produit croisé des deux vecteurs donnés en entrée
    """
    if len(x) != len(y):  # Les deux listes doivent être de même longueur
        raise ValueError("Les deux listes doivent avoir la même longueur.")

    s = 0
    for i in range(len(x)):
        s += x[i] * y[i]
    
    return s

def save_vectors_to_file(x, y, file_name):
    """
    Écrit les deux vecteurs x et y dans un fichier texte séparés par des points-virgules (;).
    
    Args:
    x -- une liste de valeurs numériques
    y -- une liste de valeurs numériques
    file_name -- le nom du fichier dans lequel les vecteurs seront écrits (extension .txt)
    """
    with open(file_name, 'w') as file:
        for i in range(len(x)):
            file.write(str(x[i]) + ';' + str(y[i]) + '\n')

if __name__ == '__main__':
    os.chdir('C:/Users/nom_utilisateur/chemin_vers_le_dossier/')  # Mettre ici votre propre chemin d'accès au dossier si nécessaire
