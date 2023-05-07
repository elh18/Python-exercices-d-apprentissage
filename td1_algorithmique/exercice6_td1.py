# Saisie des informations pour la personne A
prenom_a = input("Entrez le prénom de la personne A : ")
taille_a = float(input("Entrez la taille de la personne A en cm : "))
poids_a = float(input("Entrez le poids de la personne A en kg : "))

# Saisie des informations pour la personne B
prenom_b = input("Entrez le prénom de la personne B : ")
taille_b = float(input("Entrez la taille de la personne B en cm : "))
poids_b = float(input("Entrez le poids de la personne B en kg : "))

# Vérification si A est plus corpulent que B
a_plus_corpulent_que_b = taille_a > taille_b and poids_a > poids_b

# Affichage du résultat 
print(f"{prenom_a} est plus corpulent que {prenom_b} : {a_plus_corpulent_que_b}")
