import chaines

mot = input("Entrez un mot : ").upper()
decalage = int(input("Entrez un décalage : "))

mot_crypte = chaines.chiffre_cesar(mot, decalage)

print("Le mot crypté est : ", mot_crypte)
