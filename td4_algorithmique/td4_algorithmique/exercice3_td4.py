# Définition du dictionnaire des valeurs des lettres
valeurs_lettres = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2, 'N': 1, 'O': 1, 'P': 3,
    'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10,
    'Y': 10, 'Z': 10
}

# Demande à l'utilisateur de saisir un mot en majuscules
mot = input("Entrez un mot en majuscules : ")

# Initialise la valeur scrabble à 0
valeur_scrabble = 0

# Parcours chaque lettre du mot
for lettre in mot:
    # Vérifie si la lettre est dans le dictionnaire des valeurs des lettres
    if lettre in valeurs_lettres:
        # Ajoute la valeur de la lettre à la valeur scrabble totale
        valeur_scrabble += valeurs_lettres[lettre]

# Affiche la valeur scrabble du mot
print("La valeur scrabble du mot", mot, "est de", valeur_scrabble, "points.")
