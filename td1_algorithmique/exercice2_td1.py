# Demander à l'utilisateur le nombre de jours et le kilométrage
jours = int(input("Nombre de jours : "))
kilometres = float(input("Kilomètres parcourus : "))

# Calculer le prix de la location
prix_location = 0.5 * kilometres + 60 * jours

# Afficher le résultat au format €uros
print("Le prix de la location est de : {:.2f}€".format(prix_location))
