# Demander à l'utilisateur de saisir un entier n
n = int(input("Entrez un entier n (>= 2) : "))

# Initialiser une liste vide pour stocker les diviseurs de n
diviseurs = []

# Vérifier que n est supérieur ou égal à 2
if n < 2:
    print("Erreur : n doit être supérieur ou égal à 2.")
else:
    # Parcourir tous les entiers entre 2 et n-1 inclus
    for i in range(2, n):
        # Vérifier si i est un diviseur de n
        if n % i == 0:
            # Si oui, ajouter i à la liste des diviseurs
            diviseurs.append(i)

    # Vérifier si des diviseurs ont été trouvés
    if not diviseurs:
        # Si la liste est vide, afficher un message indiquant que n est premier
        print("Aucun diviseur trouvé pour n.")
    else:
        # Sinon, afficher la liste des diviseurs
        print("Les diviseurs de", n, "sont :", diviseurs)
