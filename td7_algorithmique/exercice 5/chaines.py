def compter(mot, lettre):
    """
    Permet de compter le nombre d'apparition d'une lettre dans un mot.

    Args:
        mot (str): Le mot dans lequel on doit chercher la lettre.
        lettre (str): La lettre à chercher dans le mot.

    Returns:
        int: Le nombre de fois que la lettre apparaît dans le mot.
    """
    compteur = 0
    for l in mot:
        if l == lettre:
            compteur += 1
    return compteur
