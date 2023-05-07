def calcul_imc(poids, taille):
    """Calcule l'IMC à partir du poids (kg) et de la taille (cm)"""
    taille_m = taille / 100  # convertir en mètres
    return poids / (taille_m ** 2)

# Demander le nombre de personnes à traiter
nb_personnes = int(input("Combien de personnes voulez-vous traiter ? "))
personnes = []

# Saisir les informations pour chaque personne
for i in range(nb_personnes):
    print(f"\nPersonne {i+1}")
    nom = input("Nom : ")
    taille = float(input("Taille (en cm) : "))
    poids = float(input("Poids (en kg) : "))
    imc = calcul_imc(poids, taille)
    personnes.append({
        "nom": nom,
        "taille": taille,
        "poids": poids,
        "imc": imc
    })

# Afficher la liste des personnes avec leur IMC
print("\nListe des personnes et leur IMC :")
for personne in personnes:
    print(f"{personne['nom']} - taille : {personne['taille']:.2f} cm - poids : {personne['poids']:.2f} kg - IMC : {personne['imc']:.2f}")

# Indiquer la personne qui présente l'IMC le plus faible
min_imc_personne = min(personnes, key=lambda p: p["imc"])
print(f"\nLa personne avec l'IMC le plus faible est {min_imc_personne['nom']} avec un IMC de {min_imc_personne['imc']:.2f}")
