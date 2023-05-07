# Demander à l'utilisateur de saisir un entier n
n = int(input("Entrez un entier : "))

# Initialiser une variable booléenne pour indiquer si n est premier
est_premier = True

# Parcourir tous les entiers entre 2 et n-1 inclus
for i in range(2, n):
    # Vérifier si i est un diviseur de n
    if n % i == 0:
        # Si oui, n'est pas premier
        est_premier = False
        break

# Afficher le résultat
if est_premier:
    print(n, "est premier.")
else:
    print(n, "n'est pas premier.")
