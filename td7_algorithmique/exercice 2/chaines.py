def compter(mot, lettre):
    """
    Retourne le nombre d'apparitions de la lettre dans le mot.
    """
    # Initialisation du compteur
    nb_app = 0
    # Parcours des lettres du mot
    for l in mot:
        # Vérification si la lettre courante est égale à celle recherchée
        if l.upper() == lettre.upper():
            # Incrémentation du compteur
            nb_app += 1
    # Retour du résultat
    return nb_app


def distincts(mot):
    """
    Retourne les lettres distinctes du mot sous forme de chaîne de caractères.
    """
    # Initialisation de la liste des lettres distinctes
    lettres_distinctes = []
    # Parcours des lettres du mot
    for l in mot:
        # Test pour voir si la lettre n'est pas déjà présente dans la liste des lettres distinctes
        if l.upper() not in lettres_distinctes:
            # Ajout de la lettre à la liste des lettres distinctes
            lettres_distinctes.append(l.upper())
    # Tri de la liste des lettres distinctes 
    lettres_distinctes.sort()
    # Retour de la chaîne de caractères composée des lettres distinctes
    return ''.join(lettres_distinctes)
