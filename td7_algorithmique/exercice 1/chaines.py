def compter(mot, lettre):
    """Fonction qui compte le nombre d'apparition d'une lettre dans un mot"""
    mot = mot.upper()  # Conversion en majuscules
    lettre = lettre.upper()
    count = 0
    for char in mot:
        if char == lettre:
            count += 1
    return count
