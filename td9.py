import json
import csv

# Définition de la liste globale de personnes
personnes = []

# Fonction pour ajouter une personne dans la liste globale
def ajouter_personne():
    nom = input("Entrez le nom de la personne : ")
    age = int(input("Entrez l'âge de la personne : "))
    taille = int(input("Entrez la taille en cm de la personne : "))
    personne = {"nom": nom, "age": age, "taille": taille}
    personnes.append(personne)

# Fonction pour afficher toutes les personnes de la liste globale
def afficher_personnes():
    if len(personnes) == 0:
        print("La liste de personnes est vide.")
    else:
        for personne in personnes:
            print(personne)

# Fonction pour sauvegarder la liste globale dans un fichier CSV ou JSON
def sauvegarder_personnes():
    nom_fichier = input("Entrez le nom du fichier de sauvegarde : ")
    extension = nom_fichier.split(".")[-1]
    if extension == "csv":
        with open(nom_fichier, mode='w', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["nom", "age", "taille"])
            for personne in personnes:
                writer.writerow([personne["nom"], personne["age"], personne["taille"]])
    elif extension == "json":
        with open(nom_fichier, mode='w') as fichier:
            json.dump(personnes, fichier, indent=4)
    else:
        print("Extension de fichier invalide. Utilisez CSV ou JSON.")

# Fonction pour charger une liste de personnes depuis un fichier CSV ou JSON
def charger_personnes():
    nom_fichier = input("Entrez le nom du fichier à charger : ")
    extension = nom_fichier.split(".")[-1]
    personnes.clear()
    if extension == "csv":
        with open(nom_fichier, mode='r') as fichier:
            reader = csv.DictReader(fichier)
            for row in reader:
                personnes.append(row)
    elif extension == "json":
        with open(nom_fichier, mode='r') as fichier:
            personnes.extend(json.load(fichier))
    else:
        print("Extension de fichier invalide. Utilisez CSV ou JSON.")

# Boucle principale du programme
while True:
    print("Menu principal :")
    print("0. Quitter")
    print("1. Ajouter une personne")
    print("2. Afficher les personnes")
    print("3. Sauvegarder les personnes dans un fichier")
    print("4. Charger les personnes depuis un fichier")
    choix = input("Entrez votre choix : ")
    if choix == "0":
        print("Merci et au revoir.")
        break
    elif choix == "1":
        ajouter_personne()
    elif choix == "2":
        afficher_personnes()
    elif choix == "3":
        sauvegarder_personnes()
    elif choix == "4":
        charger_personnes()
    else:
        print("Choix invalide. Veuillez entrer un chiffre entre 0 et 4.")
