# Saisir n1 et n2
n1 = int(input("Entrez la valeur de n1 : "))
n2 = int(input("Entrez la valeur de n2 : "))

# Vérification que n1 est supérieur à n2
if n2 <= n1:
    print("Erreur : n2 doit être strictement supérieur à n1.")

# Lister les nombres compris entre n1 et n2
else:
    for i in range(n1+1, n2):
        print(i, end=" ")
