def lire_valeurs(nom_fichier):
    """
    Lit les valeurs entières du fichier donné en paramètre et les retourne 
    sous forme de liste.
    """
    with open(nom_fichier, "r") as f:
        lignes = f.readlines()

    valeurs = []
    for ligne in lignes:
        # enlever les caractères \n en fin de ligne
        valeur = int(ligne.rstrip("\n"))
        valeurs.append(valeur)

    return valeurs
