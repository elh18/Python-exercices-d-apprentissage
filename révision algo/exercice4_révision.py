# Déclaration
nb = int(input("Saisir le nombre d'étudiants : "))
TabNotes = [0.0]*nb
Max = 0.0
Num = 0
Somme = 0.0
Moyenne = 0.0

# Lecture de toutes les notes
for i in range(nb):
    TabNotes[i] = float(input(f"Saisir la note de l'étudiant {i+1}: "))

# Affichage des notes de l'étudiant N° 3
print(f"La note de l'étudiant N°3 est : {TabNotes[2]}")

# Affichage des notes de n'importe quel étudiant
Num = int(input("Donnez le numéro de l'étudiant : "))
print(f"La note de l'étudiant N°{Num} est : {TabNotes[Num-1]}")

# Affichage des 5 meilleures notes
sorted_notes = sorted(TabNotes, reverse=True)
print("Les cinq meilleurs notes sont :")
for i in range(5):
    print(f"L'étudiant N°{TabNotes.index(sorted_notes[i])+1} a eu la note : {sorted_notes[i]}")

# Affichage de la moyenne des notes
Somme = sum(TabNotes)
Moyenne = Somme/nb
print(f"La moyenne du groupe est : {Moyenne}")

# Affichage de la plus haute note
Max = max(TabNotes)
k = TabNotes.index(Max)+1
print(f"La plus haute note est : {Max} de l'étudiant N°{k}")
