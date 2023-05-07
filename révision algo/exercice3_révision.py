# Initialisation de la liste de stock à 0
stock = [0] * 200

# Remplissage de la liste
for i in range(200):
    quantite = int(input("Saisir la quantité du produit N°{} : ".format(i + 1)))
    stock[i] = quantite

# Affichage des produits en stock minimum
for i in range(200):
    if stock[i] <= 15:
        print("Le produit N°{} est en stock minimum, sa quantité est de {}.".format(i + 1, stock[i]))
