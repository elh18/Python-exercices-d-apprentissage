# Créer un dictionnaire vide
dictionnaire = {}

# Boucle de saisie
while True:
    # Demander une saisie pour la clé
    cle = input("Entrez une clé (ou 'STOP' pour arrêter) : ")
    
    # Sortir de la boucle si la saisie est 'STOP'
    if cle == 'STOP':
        break
    
    # Vérifier si la clé existe déjà dans le dictionnaire
    if cle in dictionnaire.keys():
        print("Erreur : cette clé existe déjà")
        continue   # Passer à l'itération suivante
    
    # Demander une saisie pour la valeur
    valeur = input("Entrez une valeur : ")
    
    # Ajouter le couple "clé - valeur" dans le dictionnaire
    dictionnaire[cle] = valeur

# Afficher les résultats s'il y a des éléments dans le dictionnaire
if len(dictionnaire) > 0:
    # Afficher la liste des clés
    print("Liste des clés : ")
    for cle in dictionnaire.keys():
        print(cle)
    
    # Afficher la liste des valeurs
    print("Liste des valeurs : ")
    for valeur in dictionnaire.values():
        print(valeur)
    
    # Afficher la liste des couples "clé - valeur"
    print("Liste des couples 'clé - valeur' : ")
    for cle, valeur in dictionnaire.items():
        print(f"{cle} - {valeur}")
