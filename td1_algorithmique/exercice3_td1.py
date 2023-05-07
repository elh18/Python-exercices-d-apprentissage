prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
annee_naissance = int(input("Entrez votre année de naissance : "))

age = 2021 - annee_naissance  # Calcul de l'âge
message = f"Bonjour {nom} {prenom}, vous avez {age} ans."  # Création du message

print(message)
