import os

def saisie_tableau(n):
    tableau = []
    for i in range(n):
        valeur = int(input("Entrez la valeur numéro {}: ".format(i+1)))
        tableau.append(valeur)
    return tableau

os.chdir('C:/… votre dossier…')  #assurez-vous de spécifier votre propre répertoire de travail!
nombre_elements = int(input("Entrez le nombre d'éléments du tableau: "))

tableau = saisie_tableau(nombre_elements)
print("Le tableau est: {}".format(tableau))

nom_fichier = input("Entrez un nom de fichier pour sauvegarder le contenu: ")
with open(nom_fichier, 'w') as f:
    for element in tableau:
        f.write("%s\n" % str(element))
    print("Contenu sauvegardé dans le fichier {}!".format(nom_fichier))
