n = int(input("Entrez un entier : "))

# Vérification que n est supérieur ou égal à 2
if n < 2:
    print("Erreur : l'entier doit être supérieur ou égal à 2.")
else:
    est_premier = True
    plus_petit_diviseur = n
    plus_grand_diviseur = 2
    
    # On teste les diviseurs potentiels de n
    for diviseur in range(2, n):
        if n % diviseur == 0:
            est_premier = False
            if diviseur < plus_petit_diviseur:
                plus_petit_diviseur = diviseur
            if diviseur > plus_grand_diviseur:
                plus_grand_diviseur = diviseur
    
    # Affichage des résultats
    if est_premier:
        print(n, "est premier.")
    else:
        print(n, "n'est pas premier.")
        print("Plus petit diviseur :", plus_petit_diviseur)
        print("Plus grand diviseur :", plus_grand_diviseur)
