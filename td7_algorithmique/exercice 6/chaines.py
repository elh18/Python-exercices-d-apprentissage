def chiffre_cesar(mot,decalage):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mot_crypte = ""
    for lettre in mot:
        # On cherche la position de la lettre dans l'alphabet
        position = alphabet.find(lettre)
        # Si la lettre n'est pas dans l'alphabet, on l'ajoute telle quelle au mot crypté
        if position == -1:
            mot_crypte += lettre
        else:
            # On calcule la position de la lettre décalée dans l'alphabet
            nouvelle_position = (position + decalage) % 26
            # On ajoute la lettre décalée au mot crypté
            mot_crypte += alphabet[nouvelle_position]
    return mot_crypte
